#!/usr/bin/env python3
import argparse
from pathlib import Path
import sys
from typing import List
from ruamel.yaml import YAML

yaml=YAML(typ='safe')

def gather_sigma_rules(paths: List[Path]):
    sigma_rules = set()
    for path in paths:
        sigma_rules.add(path) if path.is_file() else [ sigma_rules.add(p) for p in path.rglob("*.yml") ]
    return { r: yaml.load(r) for r in sigma_rules}


def main(rules: List[Path]):
    """ Logsource is defined here: https://github.com/SigmaHQ/sigma/wiki/Specification#log-source
    category - examples: firewall, web, antivirus
    product - examples: windows, apache, check point fw1
    service - examples: sshd, applocker
    """
    logsources = {
        "categories": set(),
        "products": set(),
        "services": set()
    }
    for _, sigma_rule in gather_sigma_rules(rules).items():
        logsource = sigma_rule["logsource"]
        if not "category" in logsource and not "product" in logsource:
            print(f"BROKEN rule {sigma_rule}")
        if "category" in logsource:
            logsources["categories"].add(logsource["category"])
        if "product" in logsource:
            logsources["products"].add(logsource["product"])
        if "service" in logsource:
            logsources["services"].add(logsource["service"])
    crlf = '\n\t'
    print(f"Products:\n\t{crlf.join(logsources['products'])}")
    print(f"\ncategories:\n\t{crlf.join(logsources['categories'])}")
    print(f"\nservices:\n\t{crlf.join(logsources['services'])}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Sigma rules to Splunk Alerts savedsearches.conf configuration.')
    parser.add_argument('rules', action='store', metavar='R', nargs='+', help='folder or file containing the Sigma rules')
    args = parser.parse_args()

    ############################################
    # Check arguments
    ############################################
    rules = [Path(rule) for rule in args.rules]
    for rule in rules:
        if not rule.exists():
            print(f"[ERROR] rule path `{rule.absolute()}` does not exists.")
            sys.exit(1)

    main(rules)