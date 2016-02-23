with open('dump.xml') as r:
    test = r.read()
    for line in test.split('\n'):
        formatted_line = line.strip('\t')
        if formatted_line.startswith('<!--'):
            # This is a row analyze it
            num_occur = formatted_line.count("<v>")
            if num_occur != 4:
                print formatted_line