user_str = input('Please enter a string: ')
str_list = []
stack = []
for letter in user_str:
    str_list.append(letter)


done = False
while not done:
    action = input('Please select and action: q (quit) ... b (back) ... f (forward): ')
    print("")
    if action == 'q':
        done = True
    elif action == 'b':
        if len(stack) <= 0:
            print("Can't go back anymore\n")
        else:
            str_list.append(stack.pop())
    elif action ==  'f':
        print(len(str_list))
        if len(str_list) <= 0:
            print("Can't go forward anymore")
        else:
            stack.append(str_list.pop())

    print(f"{str_list}\n")



