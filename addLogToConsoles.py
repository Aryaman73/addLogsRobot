# Open the file with read only permit
f = open('sample.txt')
f2 = open('output.txt', 'w')
line = f.readline()

addLogs = False
while line:
    if "Test Cases" in str(line):
        print("Starting...")
        addLogs = True
    if "Keywords" in str(line):
        print("Ending...")
        addLogs = False

    f2.write(str(line))

    if addLogs and line.startswith(('    ')):
        f2.write("\tlog to console    " + str(line))

    line = f.readline()

f.close()
f2.close()