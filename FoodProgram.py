import FoodClass as FC

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]


def customer_info_inputs():
    print("---------- CUSTOMER INFO -----------")
    customerid = int(input("What is the customer ID?: "))
    name = input("What is the customer name?: ")
    address = input("What is the customer address?: ")
    email = input("What is the customer email?: ")
    phone = input("What is the customer phone number?: ")
    temp = input("What is the customer Member Status?: ")
    check = True
    while check:
        if temp == "True" or temp == "true":
            member_status = True
            check = False
        elif temp == "False" or temp == "false":
            member_status = False
            check = False
    return FC.Customer(customerid, name, address, email, phone, member_status)


def main():
    dict = {
        "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
        "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
        "trans3": ["2/15/2023", "The Octoveg", 16, 570],
        "trans4": ["2/15/2023", "The Octoburger", 20, 570],
    }

    order_total = 0

    customer = customer_info_inputs()
    transactions = []
    for key in dict:
        transactions.append(
            FC.Transaction(dict[key][0], dict[key][1], dict[key][2], dict[key][3])
        )
    print("\n=============================================")
    print("Customer Name: ", FC.Customer.get_name(customer))
    print("Phone: ", FC.Customer.get_phone(customer))

    for transaction in transactions:
        if FC.Customer.get_custID(customer) == FC.Transaction.get_custID(transaction):
            print(
                "Order Item: ",
                FC.Transaction.get_item_name(transaction),
                " Order Cost: $",
                FC.Transaction.get_cost(transaction),
            )
            order_total += FC.Transaction.get_cost(transaction)

    print("Total Cost: $", order_total)

    if FC.Customer.get_member_status(customer):
        member_discount = order_total * 0.2
        print("Member Discount: $", member_discount)
        order_total = order_total - member_discount
        print("Total Cost after discount: $", order_total)


main()
