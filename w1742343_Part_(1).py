credits_total = 0
credits_pass = 0
credits_defer = 0
credits_fail = 0

for i in range(28):
        while True:
            try:
                credits_pass = int(input('Enter number of pass: '))
                break
            except ValueError:
                print('Integers required')
        while True:
            try:
                credits_defer = int(input('Enter number of defer: '))
                break
            except ValueError:
                print('Integers required')
        while True:
            try:
                
                credits_fail = int(input('Enter number of fail: '))
                break
            except ValueError:
                print('Integers required')

        credits_total = credits_pass + credits_defer + credits_fail
        if credits_total != 120: 
         print('Total incorrect', 'if the total of the pass, defer and fail credit is not 120')
         continue
    
        if credits_pass % 10 != 0:
             print(credits_pass,'Range error')
      
        if credits_defer % 10 != 0:
             print(credits_defer,'Range error')
        
        if credits_fail % 10 != 0:
             print(credit_fail,'Range error')

        if credits_total != 120: 
             print('Total incorrect', 'if the total of the pass, defer and fail credit is not 120')
             continue
    
        elif credits_pass == 120 and credits_defer == 0 and credits_fail == 0:
             print('Progress')
             continue
        elif credits_pass == 100 and credits_defer <= 20 and credits_fail <= 20:
             print('Progress - module trailer')
             continue
        elif credits_pass <= 80 and credits_defer <= 120 and credits_fail <= 60:
             print('Do not progress - module retriever')
             continue
        else:
             (credits_pass <= 40 and credits_defer <= 20 and credits_fail <= 120)
             print('Exclude')
             continue



















    
