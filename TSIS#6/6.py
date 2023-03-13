import os

letters = ['A' , 'B', 'C' , 'D' , 'E' , 'F' , 'G' , 'H' ,'I' , 'J' , 'K', 'l' , 'M' , 'N', 'O', 'P' , 'Q' , 'R' ,'S' ,'T' , 'U' , 'V' , 'W' , 'X' ,'Y' , 'Z']
for i in letters:
    print(i , end = " ")

directory = "C:/PP2-22B030493/TSIS#6/dir-and-files/2"

fpath = os.path.join(directory , "{}.txt".format(letters[0]))

for i in letters:
    f = open('{}.text'.format(i), "PP2-22B030493/TSIS#6/dir-and-files/2") # "x"
f.close()




