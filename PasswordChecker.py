# Program checks the validity of a password, i.e password should be minimum 8 characters long and can contain any character.

import re

valid_password = r"[a-zA-Z0-9]{7,}[^abc]"
password_forvalidation = input("Enter your password (min: 8 characters:")

matches = re.finditer(valid_password, password_forvalidation, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    print("This password is valid ")
    print(f"This character has {match.end()} characters")
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
