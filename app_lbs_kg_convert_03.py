# Python Exercise:
# Convert weight values between 'lbs' and 'kg' units

const_lb_kg = 0.453592  # 1 lb = 0.453592 kg
counter = 0
pgm_finish = False


while not pgm_finish:
    # Step 1: Input the weight value
    invalid_weight_input = True

    while invalid_weight_input:
        weight_str = input('Enter weight numerical value, or "f" to finish the program > ').strip().replace(",", ".")

        if weight_str == "f":
            invalid_weight_input = False
            pgm_finish = True
            break

        try:
            weight_flt = float(weight_str)
        except ValueError:
            print("Invalid weight input... Please enter a valid numerical value")
        else:
            if weight_flt < 0:
                print("Negative weight input... Please enter a positive numerical value")
            else:
                invalid_weight_input = False

    # Step 2: Input the weight unit code and convert the weight value
    invalid_unit_input = True

    while invalid_unit_input and not pgm_finish:
        weight_unit = input('Enter weight unit code: "l" for lbs, "k" for kg, or "f" to finish the program > ').strip().lower()

        if weight_unit in ["l", "k"]:
            invalid_unit_input = False
            counter += 1

        match weight_unit:
            case "l":
                weight_conv = round(weight_flt * const_lb_kg, 3)
                print(f"{weight_flt} lbs = {weight_conv} kg")
            case "k":
                weight_conv = round(weight_flt / const_lb_kg, 3)
                print(f"{weight_flt} kg = {weight_conv} lbs")
            case "f":
                invalid_unit_input = False
                pgm_finish = True
            case _:
                print("Weight unit code not defined! Please enter it again.")

    print("")

# Step 3: Print the final message and finish the program
print(f"Completed {counter} conversion(s). The program will finish now, see you next time!")
print("")
