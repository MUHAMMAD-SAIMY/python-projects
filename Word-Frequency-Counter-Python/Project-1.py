result=None
while True:
    while True:
        print("\nEnter the read file name:")
        filename=input()
        txt='.txt'
        if filename.endswith('.txt'):
            continue
        else:
            filename=filename+txt
        try:
            with open(filename, 'r') as file:
                content = file.read()
                content = content.replace(' ', '')
                result=len(content)
            print("\nThe number of characters in the file is:", result)
            break
        except FileNotFoundError:
            print("\nFile not found.")
            print("\nDo you want to try again? (y/n)")
            answer=input()
            if answer.lower() == 'y':
                continue
            else:
                break
    if result !=None:
            try:  
                print("\nEnter the save file name:")
                save=input()
                save=save+txt
                with open(save, 'w') as file:
                    file.write('\nThe number of characters in the '+filename+' file is: '+str(result))
                    print("\nFile saved successfully.")
                    break
            except FileNotFoundError:
                print("\nFile not found.")
    print("\nDo you want to process another file? (y/n)")
    answer=input()
    if answer.lower() == 'y':
        result=None
        continue
    else:
        break