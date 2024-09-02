from PacCommerce import *
from tabulate import tabulate

def main():
    first_row = ["Number", "Feature"]
    num = [1, 2, 3, 4, 5, 6]
    feature = ["Input member",
               "Show membership benefit",
               "Show membership requirements",
               "Predict membership",
               "Calculate price of item",
               "Exit"]
    
    menu = [num, feature]
    menu = list(map(list, zip(*menu)))
    table_menu = tabulate(menu, headers=first_row, tablefmt="grid", colalign=("center",))
    
    print("Main Menu\n")
    print(table_menu)

    user = None  # Initialize user variable outside the loop

    while True:
        try:
            choice = int(input("What feature do you want to use (1/2/3/4/5/6)? "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            username = input("Please input username: ")
            user = MembershipUser(username=username)
            print(f"{username} is a {user.user_member} member")
        elif choice in [2, 3, 4, 5] and user is None:
            print("Please input a member first.")
        elif choice == 2:
            user.show_benefit()
        elif choice == 3:
            user.show_requirenments()
        elif choice == 4:
            try:
                monthly_expense = int(input("Please input monthly expense: "))
                monthly_income = int(input("Please input monthly income: "))
                user.predict_membership(monthly_expense, monthly_income)
            except ValueError:
                print("Please enter valid numerical values for expense and income.")
        elif choice == 5:
            try:
                list_item = list(map(int, input("Enter the list of item prices separated by space: ").split()))
                total_price = user.calculate_price(list_item)
                print(f"The total price after discount is: {total_price}")
            except ValueError:
                print("Please enter valid item prices.")
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Please choose a valid option.")

if __name__ == "__main__":
    main()
