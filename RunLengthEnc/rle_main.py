import binary, zero_one_count

def rle():
    message = input("Enter the message you want to code:")
    zero= zero_one_count.count_zero(message)
    binary_code = binary.to_binary(zero)
    print(binary_code)

if __name__ == "__main__":
    rle()