import binary, zero_one_count

def rle():
    message = input("Enter the message you want to code:")

    zero= zero_one_count.count_zero(message)
    print("The number of zeros in the message is:", zero)
    new_message = str(message)[zero::]

    binary_code = binary.to_binary(zero)
    final_code = str(binary_code) + ' ' + new_message
    print(final_code)

if __name__ == "__main__":
    rle()