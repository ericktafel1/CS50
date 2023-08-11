## re.findall function returns a list of matches to a regular expression. It requires two parameters. The first is the string containing the regular expression pattern, and the second is the string you want to search through.

import re
re.findall("ts", "tsnow, tshah, bmoreno")

 ## \w matches with any alphanumeric character.

import re
re.findall("\w", "h32rb17")

## \d matches to all single digits [0-9]

import re
re.findall("\d", "h32rb17")

import re
re.findall("\d+", "h32rb17")

import re
re.findall("\d*", "h32rb17")

import re
re.findall("\d{2}", "h32rb17 k825t0m c2994eh")

import re
re.findall("\d{1,3}", "h32rb17 k825t0m c2994eh")

import re
pattern = "\w+:\s\d+"
employee_logins_string = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"
print(re.findall(pattern, employee_logins_string))
