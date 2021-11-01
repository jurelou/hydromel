# HYDROMEL

Splunk application for SIGMA

# Generate savedsearches.conf

```
python3 -m venv env
source env/bin/activate
pip install .
python sigma2splunk.py ./rules/
```
# TODO
- timeline via https://splunkbase.splunk.com/app/4370/ OU https://splunkbase.splunk.com/app/3120/
- schedule savedsearches via https://splunkbase.splunk.com/app/4692/
- process tree / connections tree via https://splunkbase.splunk.com/app/4438/
- quickwins:

        - '$DoIt'
        - 'harmj0y'
        - 'mattifestation'
        - '_RastaMouse'
        - 'tifkin_'
        - '0xdeadbeef'
        - "AdjustTokenPrivileges"
        - "IMAGE_NT_OPTIONAL_HDR64_MAGIC"
        - "Microsoft.Win32.UnsafeNativeMethods"
        - "ReadProcessMemory.Invoke"
        - "SE_PRIVILEGE_ENABLED"
        - "LSA_UNICODE_STRING"
        - "MiniDumpWriteDump"
        - "PAGE_EXECUTE_READ"
        - "SECURITY_DELEGATION"
        - "TOKEN_ADJUST_PRIVILEGES"
        - "TOKEN_ALL_ACCESS"
        - "TOKEN_ASSIGN_PRIMARY"
        - "TOKEN_DUPLICATE"
        - "TOKEN_ELEVATION"
        - "TOKEN_IMPERSONATE"
        - "TOKEN_INFORMATION_CLASS"
        - "TOKEN_PRIVILEGES"
        - "TOKEN_QUERY"
        - "Metasploit"
        - "Mimikatz"
        - '\mimikatz'
        - 'mimikatz.exe'
        - '\mimilib.dll'
        - '<3 eo.oe'
        - 'eo.oe.kiwi'
        - 'privilege::debug'
        - 'sekurlsa::logonpasswords'
        - 'lsadump::sam'
        - 'mimidrv.sys'
        - ' p::d '
        - ' s::l '
        - 'gentilkiwi.com'
        - 'Kiwi Legit Printer'


## Doc

- https://patzke.org/a-guide-to-generic-log-sources-in-sigma.html
- https://github.com/dstaulcu/TA-Sigma-Searches
- https://medium.com/@olafhartong/cobalt-strike-remote-threads-detection-206372d11d0f

# Credits
Insprired by [Sigma2SplunkAlert](https://github.com/P4T12ICK/Sigma2SplunkAlert) developed by Patrick Bareiss (Twitter: [@bareiss_patrick](https://twitter.com/bareiss_patrick)).


