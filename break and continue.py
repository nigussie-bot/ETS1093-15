#describe break in python using forloop
for x in range(8):
    if x==5:
      break #this break will make the output only up to 4
   
    print(x) #output will be 1 2 3 4
#describe continue in python using forloop
print('\n') #to make new line between break and continue output
for x in range(8):
    
    
    
     if x==5:
        continue # this make 5 not printed
     print(x) #output will be 1 2 3 4 6 7
