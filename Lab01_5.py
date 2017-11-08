x=input('Wprowadz cyfrę ')
y=input('Wprowadz cyfre ')
z=input('Wprowadz cyfrę ')

if(x.isdigit() and len(x)==1 and y.isdigit() and len(y)==1 and z.isdigit() and len(z)==1):

    print(int(x+y+z))

    print(int(x+y+z)**2)
else:
    print ('Trzeba było podać liczbę.')
