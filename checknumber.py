#This will take a number
number = int(input('Please, give me a number: '))

#as we know prime numbers are greater than 1
if number > 1:
    #now, we will check the number
    for biddrup in range(2, number):
        if number % biddrup == 0:
            print(str(number) + ' is not a prime numbe'
                  ' as this is divided by ' + str(biddrup))
            break
    else:
        print(str(number) + ' is a prime number')
#if input is less than 1, that's not a prime number
else:
    print(str(number) + ' is not a prime number')
