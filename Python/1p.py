user_input = input("Enter your string of at least 6 characters:")
print("Your string:", user_input)
input_list = []
input_list[:0] = user_input
print("String as list:", input_list)
input_list.pop(-2)
input_list.pop(3)
print("String with 5th character removed:", input_list)
input_list.reverse()
print("Reversed list:", input_list)

new_string = ""
for char in input_list:
    new_string = new_string + char
print("Resulting string:", new_string)