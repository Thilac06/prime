
x = int(input("Enter the number : "))
i = 0
a = []
while i< x :
    k = x%(i+1)
    i += 1
    a.append(k)
    
y = len(a)
j =0
while j<(y-2):
    if(a[j+1])!= 0:
        print(f"{x} is a prime")
        j +=1
        break
    else:
        print("np")
        break

    
        
