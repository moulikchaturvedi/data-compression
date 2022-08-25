import binary, zero_one_count

def rle():
    exit=1
    while exit:
        choice=int(input("Enter your choice: \n 1. Text Data Encoding: \n 2. Binary Data Encoding: \n 3. Picture Data Encoding: \n 4. Exit"))
        final_code = ''
        if choice == 1:
            message = input("Enter the message you want to code:")
            print(final_code)
            
        elif choice == 2:
            message = input("Enter the message you want to code:")
            i=1
            print(final_code)

            while (len(message)!=0):
                zero= zero_one_count.count_zero(message)
                print("The number of zeros in the ", i, " stack is: ", zero)
                message = str(message)[zero::]
                binary_code = binary.to_binary(zero)
                final_code = final_code + ' ' + str(binary_code)
                if (len(message)!=0):
                    one= zero_one_count.count_one(message)
                    print("The number of ones in the ", i," stack is: ", one)
                    message = str(message)[one::]
                    while (one>0):
                        final_code = final_code + ' ' + '0000'
                        one= one-1

                print(final_code)
        
        elif choice == 3:
            message = input("Enter the message you want to code:")
            print(final_code)

        elif choice == 4:
            exit()

if __name__ == "__main__":
    rle()