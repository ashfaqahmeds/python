# Creating Files in Python:
# first make a file with txt toward make a text file
# Read a text file by open commands.
# syntax
#r = open('file location','mode')

r = open('c:\myfile.txt', 'r')       # r mode is for reading
print(r.read())

# to reprint from start
r.seek(0)                           # type '0' ZERO which goes first line of the file
print(r.read())

# Writing to Files in Python:~
# first create a blank txt file in drive & save it where you want.

r = open('c:\mynewfile.txt', 'w')  # w mode is for writing
r.write('Hello Everyone ,How are you\nHow was the day today')    # '\n' is for the new line or next line
r.close()
r = open('c:\mynewfile.txt', 'r')
print(r.read())