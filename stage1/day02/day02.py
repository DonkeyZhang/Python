# -*-coding:utf-8-*-

##
     print('none not ok')# py_str = 'python'
if 'th' in py_str:
    print('yes')

##
if 'to' in py_str:
    print("'to' in str")
else:
    print("'to' not in str")

##
if -0.0:    #False
    print('str ok')

if ' ':     #True
    print('list  ok')

if []:      #False
    print('list not ok')

if None:   #False

##
a, b = 10, 20
if a <= b:
    s = a
else:
    s = b

##
x, y = 10, 20
small = x if x <= y else y
print(small)


