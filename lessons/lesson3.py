

while True:
    try:
        n = int(input('Enter number :' ))

        count = 1
        while count <= n:
            if count % 3 == 0 and count % 5 == 0:
                print('FizzBuzz')
            elif count % 3 == 0:
                print('Fizz')
            elif count % 5 == 0 :
                print('Buzz')   
            else:       
               print(count)

            count += 1

        break    
    except ValueError: 
        print("Your input is not a number")   