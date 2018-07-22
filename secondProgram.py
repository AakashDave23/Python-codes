# Basic if else and elif functions

x = 41
y = 41
if x<y :
    
    print('x < y : hello world x is {} and y is {}'.format(x,y))

elif x > y :

    print('x > y: x {} and y {}'.format(x,y))

else :
    print ('something')

# While statements and len function

words = ['one', 'two' , 'three' ,'four' , 'five']

n=0
print(len(words))
while (n <= len(words) ) :
    print(n)
    print ( words[n] )

    n += 1

# For loop

words = ('one','two','three')

for i in words :
    print (i)