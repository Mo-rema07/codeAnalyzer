import re


def analyse(code):
    report = "None of the vulnerabilities checked is found in your code"
    if checkSensitive(code):
        report = "Vulnerability found:\n CWE-209: Information Exposure Through an Error Message"
    elif checkControlInclude(code):
        report = "Vulnerability found:\n CWE-98: Improper Control of Filename for Include/Require Statement in PHP " \
                 "Program ('PHP Remote File Inclusion') "
    elif checkOmmittedBreak(code):
        report = "Vulnerability found:\n CWE-484: Omitted Break Statement in Switch"
    return report


def checkSensitive(code):
    pattern = "catch.*?{.*?\n*?echo"
    match = re.search(pattern, code)
    return match is not None


def checkControlInclude(code):
    pattern = "(\\$.*?\\w+.*?).*?(\\$.*?_GET.*?).*?\n*(include\\((\\$.*?)\\.php)"
    match = re.search(pattern, code)
    return match is not None


def checkOmmittedBreak(code):
    num_case = code.count("case")
    num_break = code.count("break")
    return num_case != num_break
