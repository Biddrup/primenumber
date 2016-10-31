#They will take range from user
start = int(input('Please, give me the starting number: '))
end = int(input('And, the ending number: '))

#This is the range
print ('The prime number between '+ str(start)+ ' and '+ str(end)+ ' are: ')

#This will give the range
for num in range(start, end + 1):
    #This will check one by one
    if num > 1:
        #This will check them who are prime
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            #will print prime number
            print (num)
