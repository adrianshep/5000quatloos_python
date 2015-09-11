import re

#open and read a text file
#find various iterations of i (-i-, i + space)
#replace with capital I
#regular expressions?


#variables

    #open input file and read contents
in_file = open('samIAm.txt').read()
    #open output file, set it to 'write'
out_file = open('samIAm_new.txt', 'w')
    #create a replacements object (keys = to be replaced, value = replacement)
replacements = {'-i-':'-I-', 'i ':'I ', 'ham':'spam'}

#iterate through the array and replace each i
for i in replacements.keys():
    in_file = in_file.replace(i, replacements[i])

#replace out file text with in file text
out_file.write(in_file)

out_file.close


# in = open('path/to/input/file').read()
# out = open('path/to/input/file', 'w')
# replacements = {'zero':'0', 'temp':'bob', 'garbage':'nothing'}
# for i in replacements.keys():
#     in = in.replace(i, replacements[i])
# out.write(in)
# out.close


# re.sub(pattern, repl, string, max=0)

# myString = re.sub(r'i', 'I', string)
# print myString
# in_file = open("samIam.txt")
# data = in_file.read()
#
# out_file = open("testfile.txt", "w")
# out_file.write(data)

# file.close()
