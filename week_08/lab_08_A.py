# Input: two hexadecimal numbers
# Output: bitwise XOR in hexadecimal format

hex_2_bin_table = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101",
                   "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011",
                   "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

bin_2_hex_table = {}

for key, value in hex_2_bin_table.items():
    bin_2_hex_table[value] = key


def hex_to_bin(num):
    """
    Takes hexadecimal number less than ff as a string and outputs its binary representation with leading zeros
    """
    num = num.upper() if len(num) == 2 else "0" + num.upper()
    bin_res = ""
    # Convert every hex digit to binary and append to binary string via concatenation
    for digit in num:
        bin_res += hex_2_bin_table[digit]
    # Return binary representation
    return bin_res


def bin_to_hex(num):
    """
    Takes binary number as string of len 8 and outputs its hexadecimal representation with leading zeros
    """
    hex_res = ""
    # Convert every 4 binary digits to hex and append to hexadecimal string via concatenation
    for i in range(0, 5, 4):
        hex_res += bin_2_hex_table[num[0+i:4+i]]
    # Return binary representation
    return hex_res.lower()


def bitwise_xor(num1, num2):
    """
    Takes two binary numbers in string format of equal length and returns their bitwise XOR as binary string
    """
    xor_res = ""
    for i in range(len(num1)):
        if num1[i] == num2[i]:
            xor_res += "0"
        else:
            xor_res += "1"
    return xor_res


hex_1, hex_2 = input().split()

res = bin_to_hex(bitwise_xor(hex_to_bin(hex_1), hex_to_bin(hex_2)))
print(res)
