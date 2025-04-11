# Python Exercise:
# Print a triangle of 'n' rows ('n' in the range 1..9) of descending/ascending integers 1..n, using the nested 'for' loops

# Example output - for input number 5 (n=5):
#     1
#    212
#   32123
#  4321234
# 543212345


# Function: Get a number 'n' from the user
# Check if the input is a number and if it is in the range 1..9 (float value will be automatically converted to integer)
def fn_get_number():
    invalid_input = True
    while invalid_input:
        inp_str = input("Enter a number 1..9 > ").strip().replace(",", ".")
        try:
            inp_num = float(inp_str)  # Try to convert the input string to a float number
        except ValueError:
            print("Input is not a number")
        else:
            inp_num = int(inp_num)  # Convert the float number to integer
            if 1 <= inp_num <= 9:  # Check if the input number is in the range 1..9
                invalid_input = False  # Exit the 'while' loop
            else:
                print("Input is not in the range 1..9")

    return inp_num


# Function: Prepare the triangle string (the bottom line), e.g. for the input number 7: --> "7654321234567"
def fn_prep_t_str(inp_num):
    tmp_str = ""
    for i in range(1, inp_num + 1):
        tmp_str += f"{i}"

    return tmp_str[::-1] + tmp_str[1::]


# Function: Print the final triangle, using the nested 'for' loops
def fn_prt_triangle(inp_num, tr_str):
    for i in range(1, inp_num + 1):
        prt_str = tr_str
        for j in range(i + 1, inp_num + 1):
            prt_str = prt_str.replace(str(j), " ")

        print(prt_str)

    print("")  # Empty line below the bottom of the final triangle


# Main Program
inp_number = fn_get_number()
fn_prt_triangle(inp_number, fn_prep_t_str(inp_number))
