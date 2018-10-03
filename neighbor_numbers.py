input1 = "12,13,15,19,212,556,2146"
input2 = "13,44,432,12,788,246,2146,46"
output = []
output_str = ""

def str_to_int_list(input_str):     # transform string of numbers into list of ints
    str_list = input_str.split(",")
    int_list = []
    for getal in str_list:
        int_list.append(int(getal))
    return int_list


integer_list1 = str_to_int_list(input1)
integer_list2 = str_to_int_list(input2)

for nmbr in integer_list1:      # For each item in first list:
    for numb in integer_list2:  # Compare with each item in second list:
        if nmbr == numb:
            output.append(nmbr)
print(output)

# Transfer a list of ints in a string:
for x in output:
    if output_str == "":
        output_str += str(x)
    else:
        output_str += "," + str(x)
print("Output: \"" + output_str + "\"")


