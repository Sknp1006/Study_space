import re


s = '421221199610060012'
pattern = r'(?P<area>^\d{6})\d{4}\d{2}\d{2}\d{3}\d{1}'
pattern = r'(?P<area>^\d{6})[1000-2000]\d[1-12]\d{2}[1-31]\d{2}'
pattern = r'^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$'
print(re.search(pattern,s).group())