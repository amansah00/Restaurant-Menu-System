print("(1) Chicken Biryani \t=============> Rs.350 Only.")
print("(2) Chicken Palao \t=============> Rs.300 Only.")
print("(3) Chicken Rice \t=============> Rs.400 Only.")
print("(4) Chicken Burgar \t=============> Rs.250 Only.")
print("(5) Nawabi Pizza \t=============> Rs.355 Only.")
print("(6) 2.5 Litre Coke \t=============> Rs.138 Only.")
print("============================================================")


try:
    order=int(input("Please Select Order Number:"))
except ValueError:
    print("No Order Found")

try:
    dealsNo=int(input("Please Enter The Number of Deals:"))
except ValueError:
    print("No Deals Found") 

try:
    if order==1:
        print("Order : Chicken Biryani")
        print(f"Number of deals:{dealsNo}")
        print(f"Total Price: {350*dealsNo} Only")
        print("~~~~~~~~~~~~~Thank You For Coming~~~~~~~~~~~~~")

    elif order==2:
        print("Order : Chicken Palao")
        print(f"Number of deals:{dealsNo}")
        print(f"Total Price: {300*dealsNo} Only")
        print("~~~~~~~~~~~~~Thank You For Coming~~~~~~~~~~~~~")

    elif order==3:
        print("Order : Chicken Rice")
        print(f"Number of deals:{dealsNo}")
        print(f"Total Price: {400*dealsNo} Only")
        print("~~~~~~~~~~~~~Thank You For Coming~~~~~~~~~~~~~")

    elif order==4:
        print("Order : Chicken Burgar")
        print(f"Number of deals:{dealsNo}")
        print(f"Total Price: {250*dealsNo} Only")
        print("~~~~~~~~~~~~~Thank You For Coming~~~~~~~~~~~~~")

    elif order==5:
        print("Order : Nawabi Pizza")
        print(f"Number of deals:{dealsNo}")
        print(f"Total Price: {355*dealsNo} Only")
        print("~~~~~~~~~~~~~Thank You For Coming~~~~~~~~~~~~~")

    elif order==6:
        print("Order : 2.5 Litre Coke")
        print(f"Number of deals:{dealsNo}")
        print(f"Total Price: {138*dealsNo} Only")
        print("~~~~~~~~~~~~~Thank You For Coming~~~~~~~~~~~~~")

    else:
        print("No Order Found")
except:
    print("Run This Program Again")
