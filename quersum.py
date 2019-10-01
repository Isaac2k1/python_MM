inp="314"
qsum=0
for i in inp:
    qsum += int(i)
    print('digit=%s int.sum=%d' % (i,qsum))  #debug command
print('The queersum of %s is %d' % (inp,qsum))
