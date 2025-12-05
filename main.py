print("Here you can count manuls (Pallas's cat)!")
manul_count = int(input("Enter the number of manuls: "))
while True:
    print("What are you going to do with them?")
    print("1. Add")
    print("2. Subtract")
    action = input("Choose an action (1 or 2): ")
    if action == "1":
        add_count = int(input("How many manuls to add? "))
        manul_count += add_count
        print(f"You now have {manul_count} manuls.")
    elif action == "2":
        sub_count = int(input("How many manuls to subtract? "))
        if sub_count > manul_count:
            print("You cannot have negative manuls!")
        else:
            manul_count -= sub_count
            print(f"You now have {manul_count} manuls.")