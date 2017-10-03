import os, re

yourDir = "/Users/jfuentes/Projects/lincoln-middle-coding.github.io"
reStudentDir = re.compile(".*student.*")
if os.getcwd() == yourDir:
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        if reStudentDir.match(dirpath):
            for filename in filenames:
                if re.match('.*\.html$', filename):
                    print dirpath + '/' + filename
                    f = open(dirpath + '/' + filename, 'w')
                    f.write('<html>\n<h1>Hello there!</h1>\n<h2>My name is [insert name here]. </h2>\n</html>\n')
else:
    print("Err: NOT IN RIGHT FOLDER")
