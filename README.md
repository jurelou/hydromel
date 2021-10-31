# HYDROMEL

Splunk application for SIGMA

# Generate savedsearches.conf

```
python3 -m venv env
source env/bin/activate
pip install .
python sigma2splunk.py ./rules/
```

## Doc

- https://patzke.org/a-guide-to-generic-log-sources-in-sigma.html
- https://github.com/dstaulcu/TA-Sigma-Searches


# Credits
Insprired by [Sigma2SplunkAlert](https://github.com/P4T12ICK/Sigma2SplunkAlert) developed by Patrick Bareiss (Twitter: [@bareiss_patrick](https://twitter.com/bareiss_patrick)).

