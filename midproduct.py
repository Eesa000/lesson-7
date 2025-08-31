#input a number
num = int(input("Enter the number : "))
t = num
numlen = 0
#literate the loop
while t>0:
    numlen = numlen+1
    t = int(t/10)

    if numlen>=4: #condition 1
        numlen = numlen//2
        chk = 0
        while num>0: #literate loop
          rem = num%10
          if chk==numlen:  # nested condition
            midone = rem
