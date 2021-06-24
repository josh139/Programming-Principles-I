credits_total = 0
credits_pass = 0
credits_defer = 0
credits_fail = 0
progress = 0
trailing = 0
retriever = 0
exclude = 0
loop_again = ''

def exclude_stars(exclude):
        for i in range (exclude):
            print('*', end = ' ')
            
def retriever_stars(retriever):
        for i in range (retriever):
                print('*', end = ' ')
                
def progress_moduler(trailing):
        for i in range(trailing):
                print('*', end = ' ')
                
def progress_stars(progress):
        for i in range(progress):
                print('*', end = ' ')

loop = True   
while loop:
        try:
                credits_pass = int(input('Enter number of pass: '))
        except ValueError:
                        print('Integers required')
                        break
                       
        try:    
                credits_defer = int(input('Enter number of defer: '))
        except ValueError:
                        print('Integers required')
                        break
                        
                        
        try:        
                credits_fail = int(input('Enter number of fail: '))
        except ValueError:
                        print('Integers required')
                        break
                        
                        
        
        if credits_pass == 120 and credits_defer == 0 and credits_fail == 0:
            progress = progress+1

        if credits_pass == 100 and credits_defer <= 20 and credits_fail <= 20:
              trailing = trailing+1
          
        if credits_pass <= 80 and credits_defer <= 120 and credits_fail <= 60:
              retriever = retriever+1
          
        if credits_pass <= 40 and credits_defer <= 20 and credits_fail <= 120:
              exclude = exclude+1
        
        
        loop_again = (input('Again? y/n or q to execute: '))
        if loop_again == 'y':
         loop = True
         continue
        elif loop_again == 'n':
         loop = False
         break
        else: loop_again == 'q'
        print('Progress',progress, ':', '\r', end=' '), progress_stars(progress)
        print('Trailing',trailing, ':', '\r', end=' '), progress_moduler(trailing)
        print('Retriever',retriever, ':', '\r', end=' '), retriever_stars(retriever)
        print('Exclude',exclude, ':', '\r', end=' '), exclude_stars(exclude)
        loop = False
        break









    
