# # CHAPTER-10 OBJECT ORIENTED PROGRMMING LANGUAGE
# # FIRST CLASS

# class Person:
#     def __init__(self,name,last_name,age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age

# p1 = Person("Harsh","Singh","24")
# p2 = Person("Akriti","Singh","23")

# print(p1.name)
# print(p2.name)

# # QQ-1 BASED ON FIRST CLASS
# class Laptop:
#     def __init__(self, brand_name, model_name, price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#         self.laptop = brand_name + " " + model_name + " " + price

# l1 = Laptop("HP","Ryzen AMD-5","48,000")
# l2 = Laptop("Lenovo","Ryzen AMD-7","67,700")

# print(l1.model_name)
# print(l2.model_name)
# print(l1.laptop)
# print(l2.laptop)

# #PRINTIN FULL NAME OF PERSON
# class Person:
#     def __init__(self, name,last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#     def fullname(self):
#         return (f"{self.name} {self.last_name}")


# p1 = Person("Harsh","Singh","24")
# p2 = Person("Sonali","Singh","24")
# print(p1.fullname())
# print(p2.fullname())

# # print(p1.name)
# # print(p2.name)


# # PRINTIN FULL NAME OF PERSON
# class Person:
#     def __init__(self, name, last_name,age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#     def fullname(self):
#         return (f"{self.name} {self.last_name}")
#     def is_age_above_18(self):
#         return self.age>18

# p1 = Person("Harsh","Singh",24)
# p2 = Person("Sonali","Singh",17)

# # print(p1.name)
# # print(p1.last_name)

# # print(p2.name)
# # print(p2.last_name)

# print(p1.fullname())
# print(p2.fullname())


# # print(p1.is_age_above_18())
# # print(p2.is_age_above_18())

# #  QQ-1 BASED ON FIRST CLASS
# class Laptop:
#     def __init__(self, brand_name, model_name, price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#         # self.laptop = brand_name + " " + model_name + " " + price    # while price is int in line 91,92 not possible to concatnate here first need to change that in str but than after dicount method will not work so u can do only one method at a time

#     def discounted_price(self,num):
#         off = (num/100)*self.price
#         return self.price - off
        

# l1 = Laptop("HP","Ryzen AMD-5", 48000)
# l2 = Laptop("Lenovo","Ryzen AMD-7",67700)

# # print(l1.model_name)
# # print(l2.model_name)
# # print(l1.laptop)
# # print(l2.laptop)

# print(l1.discounted_price(10))
# print(l2.discounted_price(10))

# class Laptop:
#     def __init__(self, name, model, price):
#         self.name = name
#         self.model = model
#         self.price = price
#         self.full_detail = name + " " + model +" "+ str(price)
#     def discounted_price(self,num):
#         off = (num/100)*self.price
#         return self.price-off

# l1 = Laptop("HP", "AMD Ryzen-5", 49000)
# l2 = Laptop("Lenovo", "AMD Ryzen-7", 68000)

# print(l1.full_detail)
# print(l2.full_detail)
# print(l1.discounted_price(10)) # 10% discount on l1
# print(l2.discounted_price(50)) # 50% discount on l1


# class Laptop:
#     discount_percentage = 10 # here we are creating a class variable which will applied for def discount_percentage
#     def __init__(self, name, model, price):
#         self.name = name
#         self.model = model
#         self.price = price
#         self.full_detail = name + " " + model +" "+ str(price)
#     def discounted_price(self):
#         off = (Laptop.discount_percentage/100)*self.price
#         return self.price - off

# l1 = Laptop("HP", "AMD Ryzen-5", 49000)
# l2 = Laptop("Lenovo", "AMD Ryzen-7", 68000)

# print(l1.discounted_price())
# print(l2.discounted_price())
# print(l1.__dict__)
# print(l2.__dict__)

# # Calculating the area of cicle using class
# class Circle:
#     def __init__(self, radius, pi):
#         self.radius = radius
#         self.pi = pi
#     def area(self):
#         return 2*self.pi*self.radius

# c = Circle(2,3.14)
# c1 = Circle(4,3.14)

# print(c.area())
# print(c1.area())

# # WE DON'T NEED TO PUT PI's VALUE ALL THE TIME WE CAN ASSIGN AS CLASS VARIABLE
# class Circle:
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 2*Circle.pi*self.radius

# c = Circle(2)
# c1 = Circle(4)

# print(c.area())
# print(c1.area())



# class Laptop:
#     discount_percentage = 10 # here we are creating a class variable which will applied for def discount_percentage
#     def __init__(self, name, model, price):
#         self.name = name
#         self.model = model
#         self.price = price
#         self.full_detail = name + " " + model +" "+ str(price)
#     def discounted_price(self):
#         off = (Laptop.discount_percentage/100)*self.price
#         return self.price - off

# Laptop.discount_percentage = 90
# l1 = Laptop("HP", "AMD Ryzen-5", 49000)
# l2 = Laptop("Lenovo", "AMD Ryzen-7", 68000)

# # print(l1.discounted_price())
# # print(l2.discounted_price())
# print(l1.__dict__)
# print(l2.__dict__)

# #*************************************************************************************************
# # PROBLEM-3 count_instance from class variable
# class Person:
#     count_instance = 0 #This is called class variable or class attribute
#     def __init__(self, name, lastname, age):
#         Person.count_instance += 1
#         self.name = name
#         self.lastname = lastname
#         self.age = age

# p1 = Person("Harsh","Singh", 24)
# p2 = Person("Gagan","Singh", 23)
# p3 = Person("Priya","Desai", 24)

# print(Person.count_instance) # It will give 3 as result beacause we have created 3 instance (p1,p2,p3)

# # CREATION OF A CLASSMETHOD AND COUNTING INSTANCES
# class Person:
#     count_instance = 0 # CLASS VARIABLE / CLASS ATTRIBUTE
#     def __init__(self, name, last_name, age):
#         Person.count_instance += 1
#         self.name = name
#         self.last_name = last_name
#         self.age = age

#     @classmethod
#     def count_instances(cls):
#         return f"You have created {cls.count_instance} instances of Person Class"
    
# p1 = Person("Harsh","Singh", 24)
# p2 = Person("Gagan","Singh", 23)

# print(Person.count_instances())

# class Person:
#     @classmethod # here we are using class-method decorators
#     def from_string(cls,string):
#         first,last,age = string.split(",")
#         return cls(first,last,age)

# p = Person.from_string('Harsh,Singh,24')
# print(p.full_name())


# # STACTIC-METHOD
# class Person:
#     @staticmethod # here we are using static-method decorators
#     def hello():
#         print("Hello Harsh!!,\nThanks for calling static method.")

# Person.hello()



class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def make_a_call(self, phone_number):
        print(f"calling {phone_number}.....")

    def full_name(self):
        return f"{self.brand} {self.model}"

phone1 = Phone("Nokia", 1100, 1500)
# print(phone1.price)
# print(phone1.brand)
# print(phone1.model)
# print(phone1.__dict__)

# phone1.price = 1000
# print(phone1.price) # HERE PRICE WILL BE 1000 BUT IN LINE NUMBER 257 PRICE = 1500
# # SO LIKE THIS(LINE 263) WE CAN CHANGE THE VALUES 















