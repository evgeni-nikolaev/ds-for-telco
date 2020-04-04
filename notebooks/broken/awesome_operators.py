import requests
import re

awesome_re = re.compile("\[([^\]]+/[^\]]+)\]")
r = requests.get('https://raw.githubusercontent.com/operator-framework/awesome-operators/master/README.md')
operators = awesome_re.findall(r.text)

for operator in operators:
    print(operator)
