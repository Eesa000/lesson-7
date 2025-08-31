        #take input of a word
string = input("Please enter your own word : ")
        #take input of a character
char = input("please enter your own character : ")
i = 0
count = 0
        #loop will to find the occurence of the character while(i < len(string)): #string operation
while(i < len(string)): #string operation

if(string[i] == char):
                count = count + 1
          i = i + 1

        #display the result
print ("The total number of times ",char, " has occurred  = " ,
            count)