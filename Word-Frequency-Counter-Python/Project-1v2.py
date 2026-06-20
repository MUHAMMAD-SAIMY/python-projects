result = None

while True:
    
    while True:
        print("\nEnter the filename to read (include .txt):")
        filename = input()                 
        try:

            with open(filename, 'r') as file: 
                content = file.read()         
            words = content.lower().split()   
            word_count = {}   
                
            for word in words:               
                if word in word_count:        
                    word_count[word] += 1     
                else:
                    word_count[word] = 1   
            print("\nWord frequencies:")       

            for word, count in word_count.items():  
                print(word + ": " + str(count))   
            result = word_count               
            break                             
            
        except FileNotFoundError:
            print("\nFile not found. Try again? (y/n)")
            answer = input()
            if answer.lower() != 'y':       
                break


    if result != None:             
        print("\nEnter the save filename (include .txt):")
        save_filename = input()
        
        with open(save_filename, 'w') as file:  
        
            for word, count in result.items():
                file.write(word + ": " + str(count) + "\n")  

        print("\nSaved to " + save_filename + " successfully.")

    print("\nProcess another file? (y/n)")
    answer = input()
    if answer.lower() != 'y':
        break

    result = None                            