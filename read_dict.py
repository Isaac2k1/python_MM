# path to word list in MacOS: /usr/share/dict/web2
ObjRead = open("/usr/share/dict/web2", "r")

# txtContent = ObjRead.read();
# 
# i=0
# for word in txtContent:
# 	i +=1
# 	print(len(word),hex(int(word)))
# 
# print ("The Content of text file is : ", txtContent)
# print("number of words:",i)
# 
# 
# 
# 

variables = dict()
with open('/usr/share/dict/web2', 'r') as textfile:
    while True:    
        next_line = textfile.readline()
        print(next_line,len(next_line))
        if len(next_line) == 0:
            break

#        key, value = next_line.split()
#        if key == 'NODATA_value':
#            break
#
#        variables[key] = value    
#




#ObjRead.close()