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
        discount = ["15%", "10%", "8%"]
        benefit = ["Benefit Gold + Silver + Cashback max. 30%",
                        "Benefit Silver + Voucher Ojek Online",
                        "Voucher Makanan"]
        
        table_benefit = {"Membership" : self.membership,
                         "Discount" : discount,
                         "Another Benefit" : benefit}
        
        table_benefit = tabulate(table_benefit, headers = "keys", tablefmt="github",
                                 colalign = ["center"] * len(table_benefit))
        
        print("Benefit Membership PacCommerce\n")
        print(table_benefit)

    def show_requirenments(self):
        table_requirements = {"Membership" : self.membership,
                              "Monthly Expense (juta)" : self.member_monthly_ex,
                              "Monthly Income (juta)" : self.member_monthly_in}
        
        #Create table of membership requirements
        table_requirements = tabulate(table_requirements, headers = "keys", tablefmt="github",
                                      colalign = ["center"] * len(table_requirements))
        
        print("Requirements Membership PacCommerce\n")
        print(table_requirements)

    def predict_membership(self, monthly_expense, monthly_income):
        user_data = [monthly_expense, monthly_income]

        #Create nested list of member requirements
        member_data = list(zip(self.member_monthly_ex, self.member_monthly_in))

        #Create list of user dictance membership
        dist = [calc_dist(user_data, member_data[i]) for i in range(len(member_data))]
        
        #Create dictionary of user distance membership
        user_predict = dict(zip(self.membership, dist))

        #Find the nearest memmbership
        self.user_member = self.membership[dist.index(min(dist))]
        
        #Update user member to database
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

