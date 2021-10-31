#!/usr/bin/env python3
import argparse
from pathlib import Path
import sys
from sigma import sigmac
from subprocess import Popen, PIPE
from typing import List
from ruamel.yaml import YAML
import configparser
from jinja2 import Environment, FileSystemLoader

yaml=YAML(typ='safe')

def gather_sigma_rules(paths: List[Path]):
    sigma_rules = set()
    for path in paths:
        sigma_rules.add(path) if path.is_file() else [ sigma_rules.add(p) for p in path.rglob("*.yml") ]
    return { r: yaml.load(r) for r in sigma_rules}

def convert_sigma_to_spl(sigmac_config: Path, rule_path: Path):
    command = ["sigmac", "-t", "splunk", "-c", str(sigmac_config.absolute()), str(rule_path.absolute())]
    stdout, stderr = Popen(command, stdout=PIPE,  stderr=PIPE).communicate()
    if stderr:
        print(f"[ERROR] Could not convert sigma rule {str(rule_path.absolute())}: {stderr}")
        return None
    return stdout.decode()

def transform_splunk_search(config, splunk_rule):
    splunk_rule = f"{config['source_index']} {splunk_rule.split('| table')[0].strip()} | {config['spl_summary']} "
    return splunk_rule

def generate_savedsearches(template_file, searches: list):
    env = Environment(loader=FileSystemLoader(template_file.parent))
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.rstrip_blocks = True

    template = env.get_template(template_file.name)
    with open(template_file.stem, "w+") as f:
        f.write(template.render(searches=searches))

def main(config, sigmac_config: Path, template: Path, rules: List[Path]):
    searches = []
    for sigma_rule_path, sigma_rule in gather_sigma_rules(rules).items():
        splunk_rule = convert_sigma_to_spl(sigmac_config, sigma_rule_path)
        if not splunk_rule:
            continue
        searches.append({
            "query": transform_splunk_search(config, splunk_rule),
            "config": dict(config.items()),
            "sigma_rule": sigma_rule
        })
        print(f"[INFO] Generated rule {sigma_rule['title']}")
    generate_savedsearches(template, searches)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Sigma rules to Splunk Alerts savedsearches.conf configuration.')
    parser.add_argument('rules', action='store', metavar='R', nargs='+', help='folder or file containing the Sigma rules')
    parser.add_argument('--sigmac-config', '-s', action='store', dest='sigmac_config', default="./config/sigmac.yml", help='Sigmac configuration file.')
    parser.add_argument('--template', '-t', action='store', dest='template', default="./config/savedsearches.conf.tmpl", help='Savedsearches.conf template.')
    args = parser.parse_args()

    ############################################
    # Check arguments
    ############################################
    template = Path(args.template)
    if not template.is_file():
        print(f"[ERROR] template path `{template.absolute()}` does not exists.")
        sys.exit(1)

    sigmac_config = Path(args.sigmac_config)
    if not sigmac_config.is_file():
        print(f"[ERROR] sigmac config path `{sigmac_config.absolute()}` does not exists.")
        sys.exit(1)

    rules = [Path(rule) for rule in args.rules]
    for rule in rules:
        if not rule.exists():
            print(f"[ERROR] rule path `{rule.absolute()}` does not exists.")
            sys.exit(1)

    config = configparser.ConfigParser()
    config.read("./config/config.ini")
    main(config["chouchen"], sigmac_config, template, rules)