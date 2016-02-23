import re
target_num = 1456232412

with open('dump.xml') as r:
    test = r.read()
    for line in test.split('\n'):
        formatted_line = line.strip('\t')
        num = re.findall(r"/ \d\d\d\d\d\d\d\d\d\d", test)[0]
        format_num = num[2:]
        if int(format_num) < target_num:
            pass
        else:
            print formatted_line
        # if formatted_line.startswith('<!--'):
        #     # This is a row analyze it
        #     print re.findall(r"/ \d\d\d\d\d\d\d\d\d\d", formatted_line)
