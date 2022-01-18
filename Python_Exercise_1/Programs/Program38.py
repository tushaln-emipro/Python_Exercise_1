"""
    Program 38
    Write a program having classes as Product, Order, Customer
        a. Do appropriate inheritance of the above classes
        b. Write appropriate methods / constructors in each classes
        c. Following output is expected
            i. Order No : SO001
            ii. Customer : Sanjay Patel
            iii. Customer Email : sanjay@dummy.com
            iv. Name of the product is 'Pencil'
            v. Product Qty is : 15
            vi. Unit Price is 20
            vii. Order total is : 300
"""


class Product:
    def __init__(self, name, qty, total, unitprice):
        self.Name = name
        self.Qty = qty
        self.UnitPrice = unitprice
        self.Total = total


class Customer():
    def __init__(self, customer, email):
        self.Customer = customer
        self.Email = email


class Order(Customer, Product):
    def __init__(self, orderno, customer, email, name, qty, unitprice, total):
        self.OrderNo = orderno
        Product.__init__(self, name, qty, total, unitprice)
        Customer.__init__(self, customer, email)

    def printname(self):
        print('i. Order No :', self.OrderNo, '\n''ii. Customer :', self.Customer, '\n''iii. Customer Email :',
               self.Email, '\n''iv. Name of the product is :', self.Name, '\n''v. Product Qty is :',
               self.Qty, '\n''vi. Unit Price is :', self.UnitPrice, '\n''vii. Order total is :', self.Total)


x = Order('SO001', 'Sanjay Patel', 'sanjay@dummy.com', 'Pencil', 15, 30, 300)
x.printname()
