from os import system
import csv
clear = lambda: system("cls")

def lgn_info():
    with open("login_passw.csv", "r") as log_passw:
        return [{line["id"]: {"name": line["name"], "surname": line["surname"],"phone num": line["phone num"],"country": line["country"], "password": line["password"], "balance": int(line["balance"])}} for line in csv.DictReader(log_passw)]
    
def dict_list_to_dict(dict_list):
    user_dict, cycle = {}, 0
    while cycle < len(dict_list):
        user_dict.update(dict_list[cycle])
        cycle += 1

    return user_dict

def main():
    clear()    
    def sign_up_foo():
        user_dict_list = lgn_info()
        
        id_count, field_names = len(user_dict_list) + 1, ["id", "name","surname", "phone num", "country", "password", "balance"]

        print("================== Signing up ====================")
        print(f"This is your id: {id_count}")
        print("-----" * 10)
        print("Please remeber it.")
        print("-----" * 10)
        name_inpt = input("Enter your name: ").title()
        print("-----" * 10)
        surname_inpt = input("Enter your surname: ").title()
        print("-----" * 10)
        country_inpt = input("Enter your country: ").title()
        print("-----" * 10)
        phone_num_inpt = input("Enter your phone number: ").title()
        print("-----" * 10)
        print("Your password has to be at least 8 sybols.")
        print("-----" * 10)
        passw_inpt = input("Enter your password: ")
        while len(passw_inpt) < 7:
            print("-----" * 10)
            print("Your password has to be at least 8 sybols!")
            print("-----" * 10)
            passw_inpt = input("Enter your password: ")
        print("-----" * 10)
        bal_inpt = input("Enter your balance: ")   
        print("=====" * 10) 
        full_info_dict = {"id": id_count, "name": name_inpt, "surname": surname_inpt, "phone num": phone_num_inpt, "country": country_inpt, "password": passw_inpt, "balance": bal_inpt}
        
        with open("login_passw.csv", "a") as log_passw:
            writer = csv.DictWriter(log_passw, fieldnames=field_names)
            writer.writerow(full_info_dict)

        sign_in_up_foo()
    basket_dict = {
        "basket": [],
        "basket_price": 0
        }
    
    def only_basket_foo():
        for basket_prnt in basket_dict["basket"]:
            print("-----" * 10)                       
            print(basket_prnt)

    def sign_in_foo():
        clear()
        print("================== Signing in ====================")
        user_inpt = input("Enter your id: ")
        print("-----" * 10)
        user_dict_list = lgn_info()
        user_dict = dict_list_to_dict(user_dict_list)
        if user_inpt in user_dict:
            passw_inpt = input("Enter your password: ")
            if passw_inpt == user_dict[user_inpt]["password"]:
                clear()
                print("============= Welcome to Swag shop! ==============")
                
                def name_foo():
                    clear()
                    print("=================== Output =======================")
                    print(f"Your name: {user_dict[user_inpt]['name']}")
                    print("=====" * 10)
                    profile_foo()
                
                def surname_foo():
                    clear()
                    print("=================== Output =======================")
                    print(f"Your surname: {user_dict[user_inpt]['surname']}")
                    print("=====" * 10)
                    profile_foo()

                def fullname_foo():
                    clear()
                    print("=================== Output =======================")
                    print(f"Your fullname: {user_dict[user_inpt]['name']} {user_dict[user_inpt]['surname']}")
                    print("=====" * 10)
                    profile_foo()

                def country_foo():
                    clear()
                    print("=================== Output =======================")
                    print(f"Your country: {user_dict[user_inpt]['country']}")
                    print("=====" * 10)
                    profile_foo()

                def phone_num_foo():
                    clear()
                    print("=================== Output =======================")
                    print(f"Your phone number: {user_dict[user_inpt]['phone num']}")
                    print("=====" * 10)
                    profile_foo()
                    
                def profile_foo():
                    opt_dict, opt_bool = {
                        "see name": name_foo,
                        "see surname": surname_foo,
                        "see fullname": fullname_foo,
                        "check phone number": phone_num_foo,
                        "check country": country_foo,
                        }, 1
                    
                    opt_qtty, inpt_opt_qtty = 0, 0
                    while opt_bool == 1:
                        print("\n=================== Options ======================")
                        for key in opt_dict:
                            opt_qtty += 1
                            print(f"{opt_qtty}: {key.title()}")
                        print("Q: Back to menu")
                        print("-----" * 10)
                        cust_input = input("Enter here: ").lower()

                        if cust_input == "q":
                            opt_bool = 0
                            option_foo()

                        for key, foo in opt_dict.items():
                            inpt_opt_qtty += 1
                            key += ":".join([key, str(inpt_opt_qtty)])
                            if cust_input in key:    
                                foo() 

                def balance_foo():
                    clear()
                    print("=============== Customer Balance =================")
                    print(f"Dear Mr./Ms. {user_dict[user_inpt]['name']} your balance is: {user_dict[user_inpt]['balance']} tmt")
                    print("=====" * 10)
                    option_foo()

                def q_basket_foo():
                    clear()
                    with open("login_passw.csv", "r+") as log_passw:
                        quit_dict = [{"id": line["id"], "name": line["name"], "surname": line["surname"], "phone num": line["phone num"], "country": line["country"], "password": line["password"], "balance": int(line["balance"])} for line in csv.DictReader(log_passw)]

                    for info in quit_dict:
                        quit_dict[int(user_inpt) - 1]["balance"] = user_dict[user_inpt]["balance"]

                    field_names = ["id", "name", "surname", "phone num", "country", "password", "balance"]

                    with open("login_passw.csv", "w") as log_passw:
                        writer = csv.DictWriter(log_passw, fieldnames=field_names)
                        writer.writeheader()
                        writer.writerows(quit_dict)

                    if len(basket_dict["basket"]) > 0:
                        print("=================== Basket =======================")
                        print(f"Dear {user_dict[user_inpt]['name']} your basket contains:")
                        only_basket_foo()
                        print("=====" * 10)
                        print("\n=================== Output =======================")
                        print(f"The cost of products will be {basket_dict['basket_price']} tmt")
                        print("-----" * 10)
                        print(f"Your balance: {user_dict[user_inpt]['balance']} tmt")
                        print("-----" * 10)
                        print("Have a nice day!")
                        print("=====" * 10)
                    else:
                        print("=================== Output =======================")
                        print(f"Dear {user_dict[user_inpt]['name']} unfortunately you did't choose any of our product.")
                        print("-----" * 10)
                        print("Have a nice day!")
                        print("=====" * 10)
                    sign_in_up_foo()

                def basket_foo():
                    clear()
                    if len(basket_dict["basket"]) > 0:
                        print("=================== Basket =======================")
                        print(f"Dear {user_dict[user_inpt]['name']} your basket contains:")
                        only_basket_foo()
                        print("=====" * 10)
                        print("\n=================== Output =======================")
                        print(f"The cost of products will be {basket_dict['basket_price']} tmt")
                        print("-----" * 10)
                        print(f"Your balance: {user_dict[user_inpt]['balance']} tmt")
                        print("=====" * 10)
                    else:
                        print("=================== Output =======================")
                        print(f"Dear {user_dict[user_inpt]['name']} unfortunately you did't choose any of our product.")
                        print("=====" * 10)
                    option_foo()
                
                def shop_foo(csv_f):
                    clear()
                    print("================= Shopping time! =================")
                    
                    shop_bool = 1
                    
                    with open(csv_f, "r") as choice_f:
                        prod_dict_list = [{name["id"]: {"name": name["name"], "price": int(name["price"])}} for name in csv.DictReader(choice_f)]

                    prod_dict = dict_list_to_dict(prod_dict_list)

                    while shop_bool == 1:
                        clear()
                        print("=================== Options ======================")
                        print("Please choose one option below:")
                        print("-----" * 10)
                        for name, val in prod_dict.items():
                            print(f"{name}: {val['name'].title()} {val['price']} tmt")
                        print("-----" * 10)
                        print("Q: Back to menu")
                        print("-----" * 10)
                        print("C: Back to category menu")
                        print("-----" * 10)
                        cust_input = input(f"Enter here: ").lower()  

                        if cust_input == "q" and basket_dict["basket_price"] <= 0:
                            clear()
                            print("================= Attention! =====================")
                            print(f"Dear {user_dict[user_inpt]['name']} you didn't choose anything. If you wish to quit press 'Q':")
                            print("-----" * 10)
                            cust_input = input("Q?: ")

                        if cust_input == "c":
                            shop_bool = 0
                            category_foo()

                        if cust_input == "q": 
                            shop_bool = 0
                            option_foo()
                        
                        for choice, price in prod_dict.items():
                            if cust_input in choice:
                                basket_dict["basket_price"] += price["price"]
                                basket_dict["basket"].append(f"{price['name'].title()} {price['price']} tmt")
                                user_dict[user_inpt]["balance"] -= price["price"]
                                
                            if price["price"] > user_dict[user_inpt]["balance"]:
                                shop_bool = 0
                                clear()
                                print("=================== Warning ======================")
                                print("Not enough money! Please make replenishment!")
                                print("=====" * 10)
                                print()
                                bal_replen()

                def category_foo():
                    clear()
                    category_bool = 1
                    
                    with open("prod_category.csv", "r") as choice_f:
                        category_dict_list = [{name["id"]: {"name": name["name"], "file": name["file"]}} for name in csv.DictReader(choice_f)]

                    category_dict = dict_list_to_dict(category_dict_list)

                    while category_bool == 1:
                        print("================== Category ======================")
                        for key, val in category_dict.items():
                            print(f"{key}: {val['name'].title()}")
                        print("Q: Back to menu")
                        print("-----" * 10)
                        cust_input = input("Enter here: ").lower()
                        
                        if cust_input == "q":
                            option_foo()
                            category_bool = 0
                            
                        for key, csv_f in category_dict.items():
                            if cust_input in key:    
                                shop_foo(csv_f['file'])
                    option_foo()
                    
                def bal_replen():
                    print("============ balance replenishment ===============")
                    print(f"Your balance: {user_dict[user_inpt]['balance']} tmt")
                    print("-----" * 10)
                    print("Q: Back to menu")
                    print("-----" * 10)
                    cust_inpt = input("Enter amount of money for replenishment: ").lower()

                    if cust_inpt == "q":
                        option_foo()

                    user_dict[user_inpt]["balance"] += int(cust_inpt)
                    balance_foo()

                def option_foo():
                    opt_dict, opt_bool = {
                        "profile": profile_foo,
                        "check balance": balance_foo,
                        "check basket": basket_foo,
                        "buy product": category_foo,
                        "balance replenishment": bal_replen,
                        }, 1
                    
                    while opt_bool == 1:
                        opt_qtty, inpt_opt_qtty = 0, 0
                        print("\n=================== Options ======================")
                        for key in opt_dict:
                            opt_qtty += 1
                            print(f"{opt_qtty}: {key.title()}")
                        print("Q: Logout")
                        print("-----" * 10)
                        cust_input = input("Enter here: ").lower()

                        if cust_input == "q":
                            opt_bool = 0
                            q_basket_foo()

                        for key, foo in opt_dict.items():
                            inpt_opt_qtty += 1
                            key += ":".join([key, str(inpt_opt_qtty)])
                            if cust_input in key:    
                                foo() 
                option_foo()
            else:
                clear()
                print("==================== Error =======================")
                print("Wrong password!")
                print("=====" * 10)
                user_inpt = input("Press enter to try again: ")
                sign_in_foo()
        else:
            clear()
            print("==================== Error =======================")
            print("This id doesn't exist.")
            print("=====" * 10)
            user_inpt = input("Press enter to try again: ")
            sign_in_up_foo()
    
    def quit_foo(): 
        clear()
        print("================== Goodbye! =======================")
        if len(basket_dict["basket"]) > 0:
            print("Your basket:")
            only_basket_foo()
            print("-----" * 10)
            print("Have a nice day!")
            print("=====" * 10)
        else:
            print("Have a nice day!")
            print("=====" * 10)
        quit()

    def sign_in_up_foo():
        enter_dict, sign_bool = {
            "1: sign up": sign_up_foo,
            "2: sign in": sign_in_foo,
            }, 1
        
        while sign_bool == 1:
            clear()
            print("============= Welcome to Swag shop! ==============")
            for key in enter_dict:
                print(f"{key.split(':')[0]}:{key.split(':')[1].title()}")
            print("Q: Quit")
            print("-----" * 10)
            cust_input = input("Enter here: ").lower()

            if cust_input == "q":
                sign_bool = 0
                quit_foo()

            for key, foo in enter_dict.items():
                if cust_input in key:    
                    foo()
    sign_in_up_foo()

clear()
print("============= Welcome to Swag shop! ==============")
user_inpt = input("Press E/Q to enter or quit: ").lower()

if user_inpt != "q":
    main()
else:
    clear()
    print("================== Goodbye! =======================")
    print("Have a nice day!")
    print("=====" * 10)