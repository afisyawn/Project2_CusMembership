from tabulate import tabulate

def calc_dist(A, B):
    dist = ((A[0] - B[0])**2 + ((A[1] - B[1])**2))**0.5
    dist = round(dist, 2)

    return dist


class MyError(Exception):
    def __init__(self, error, value):
        self.error = error
        self.value = value


class MembershipUser:
    def __init__(self, username = "", monthly_expense = 0, monthly_income = 0):
        self.username = username
        self.monthly_expense = monthly_expense
        self.monthly_income = monthly_income

        self.membership = ["Platinum", "Gold", "Silver"]
        self.member_monthly_ex = [8, 6, 5]
        self.member_monthly_in = [15, 10, 7]

        self.user_database = {'Sumbul': 'Platinum',
                              'Ana': 'Gold',
                              'Cahya': 'Platinum'}
        self.add_user(self.username)
        self.user_member = self.user_database.get(self.username)    
    
    def add_user(self, username):
        if username not in self.user_database.keys():
            self.user_database[username] = "None"
            print("Create new user")
        else:
            print("Username already exist")
        

    def show_benefit(self):
        self.first_row = ["Membership", "Discount", "Another Benefit"]
        self.discount = ["15%", "10%", "8%"]
        self.benefit = ["Benefit Gold + Silver + Cashback max. 30%",
                        "Benefit Silver + Voucher Ojek Online",
                        "Voucher Makanan"]
        self.table_benefit = [self.membership,
                                 self.discount,
                                 self.benefit]
        
        self.table_benefit= list(map(list, zip(*self.table_benefit)))
        table_benefit = tabulate(self.table_benefit,
                                 headers = self.first_row,
                                 tablefmt="github",
                                 colalign = ["center"] * len(self.first_row))
        
        print("Benefit Membership PacCommerce\n")
        print(table_benefit)

    def show_requirenments(self):
        self.first_row = ["Membership", "Monthly Expense (juta)", "Monthly Income (juta)"]
        self.table_requirements = [self.membership,
                                   self.member_monthly_ex,
                                   self.member_monthly_in]
        
        self.table_requirements= list(map(list, zip(*self.table_requirements)))
        table_requirements = tabulate(self.table_requirements,
                                      headers = self.first_row,
                                      tablefmt="github",
                                      colalign = ["center"] * len(self.first_row))
        
        print("Requirements Membership PacCommerce\n")
        print(table_requirements)

    def predict_membership(self, monthly_expense, monthly_income):
        self.monthly_expense = monthly_expense
        self.monthly_income = monthly_income
        user_data = [self.monthly_expense, self.monthly_income]
        member_data = list(zip(self.member_monthly_ex, self.member_monthly_in))

        dist = [calc_dist(user_data, member_data[i]) for i in range(len(member_data))]
        
        user_predict = dict(zip(self.membership, dist))

        self.user_member = self.membership[dist.index(min(dist))]
        
        self.user_database[self.username] = self.user_member

        print(f"Hasil perhitungan Euclidean Distance dari user {self.username} adalah {user_predict}")
        print(self.user_member)

    def calculate_price(self, list_item):
        self.list_item = list_item
        total_item = sum(self.list_item)

        #Platinum membership
        if self.user_member == self.membership[0]:
            discount = 15/100

        #Gold membership
        elif self.user_member == self.membership[1]:
            discount = 10/100
        
        #Silver membership
        elif self.user_member == self.membership[2]:
            discount = 8/100
        
        #Non membership
        else:
            discount = 0
        
        final_price = total_item - (total_item * discount)

        return(final_price)

