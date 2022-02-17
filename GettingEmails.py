import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

"""
[\w\.-]+ соответствует одному или более символу слова, точке или черточке.
"""

str = "Please contact info@sololearn.com for assistance"

match = re.search(pattern, str)
if match:
    print(match.group())
