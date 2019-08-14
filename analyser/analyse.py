import re


def analyse(code):
    report = "None of the vulnerabilities checked is found in your code"
    # if checkSensitive(code):
    #     report = "Vulnerability found:\n CWE-209: Information Exposure Through an Error Message"
    # elif checkUnitializedVariable(code):
    #     report = "Vulnerability found:\n CWE-457: Use of Uninitialized Variable"
    if checkOmmittedBreak(code):
        report = "Vulnerability found:\n	CWE-484: Omitted Break Statement in Switch"
    return report


def checkSensitive(code):
    pattern = "case.*?break"
    match = re.search(pattern, code)
    return match is not None


def checkUnitializedVariable(code):
    return True


# Should return True if there exists a case statement in the code without a break
def checkOmmittedBreak(code):
    pattern = "case.*?break"
    match = re.search(pattern, code)
    return (match is not None) and ("switch" in code)
