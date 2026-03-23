#clothes branding program

# brand = input("enter the brand of clothes: ")
# if brand == "nike":
#     print("you are wearing nike clothes")
# elif brand == "adidas":
#     print("you are wearing adidas clothes")
# elif  brand == "puma":
#     print("you are wearing puma clothes") 
# else:
#     print("you are wearing other brand clothes")



#basic calculator program
# num1=float(input("enter first number: "))
# num2=float(input("enter second number: "))
# operator=input("enter operator (+, -, *, /): ")

# if operator == "+":
#     print("result:", num1 + num2)
# elif operator == "-":
#     print("result:", num1 - num2)
# elif operator == "*":
#     print("result:", num1 * num2)
# elif operator == "/":
#     if num2 != 0:
#         print("result:", num1 / num2)
#     else:
#         print("error: division by zero is not allowed")
# else:
#     print("invalid operator!")


 # weather suggestion program

# weather = input("enter the weather (sunny, rainy, cold): ").lower() #lower method is used to convert all the upper case characters into lower case.
# if weather == "sunny":
#     print("wear light clothes and sunglasses")
# elif weather == "rainy":
#     print("carry an umbrella and wear waterproof shoes")
# elif weather == "cold":
#     print("wear warm clothes and a jacket")
# else:
#     print("invalid weather type!")


#traffic light program
# light = input("enter the traffic light color (red, yellow, green): ").lower()
# if light == "red":
#     print("stop")
# elif light == "yellow":
#     print("get ready")
# elif light == "green":
#     print("go")
# else:
#     print("invalid traffic color!")




#PANDAS
#DataFrame : the structured dataframe
#create dataframe
# import pandas as pd
# kanishka=pd.DataFrame([10,20,30,40,50], columns=["numbers"])
# print(kanishka)
# print(type(kanishka)) #DataFrame


# import pandas as pd
# data=pd.DataFrame([5,10,15,20,25], columns=["multiple of 5"])
# print(data)


# import pandas as pd
# abcd={"name": ["tanu", "neha", "prachi", "priya", "anjali", "aditi"], "age": [18, 20, 22, 25, 23,21], "salary": [10000, 20000, 23000, 25000, 30000, 28000]}
# df=pd.DataFrame(abcd)
# print(df)
# print(df.head(2))
# print(df.tail(3))
# print(df.shape)
# print(df.columns)
# print(df.rename(columns={"salary" : "payment"}, inplace = True))
# print(df)
# print(df.info()) #gives all information about the table(types, memory)
# print(df.describe()) #for stastical summary
      
# #df.head() # by default first 5 rows if we write indexing in circle bracket then it will give output according to this.
# #df.tail() # by default last 5 rows    
# #df.shape - tells us about the no. of rows and columns

# #create a co. where you have employee id, age, salary, joining date, min=15 rows 
#import pandas as pd 
# abc={ "name" : ["angel", "priya", "kavita", "aditi", "anjali", "kanishka", "neha", "ritu", "palak", "prachi", "khushi", "akshara","shivani", "anshi", "vaishnavi"],
#      "emp id" : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
#     "age" : [23,34,21,13,14,17,24,42,27,29,21,32,54,12,32],
#      "salary" : [12000,13000,10000,21000,32000,43000,1200,2000,32000,7000,9000,8000,7020,5600,6400],
#      "joining date" : [1,1,2,3,4,5,23,12,15,16,17,27,31,12,21]}
# df=pd.DataFrame(abc)
# print(df)


# df.to_csv("new_data.csv", index=False) #to remove index number
# load_df = pd.read_csv(r"C:\users\kdev2\new_data.csv")
# load_df


#CREATE A DATA FRAME WITH YOUR EMPLOYEE WORKING IN A RESTAURANT. MINIMUM EMPLOYEES ARE 20-25.

import pandas as pd

data = {
    "Employee_ID": [101,102,103,104,105,106,107,108,109,110,
                    111,112,113,114,115,116,117,118,119,120,
                    121,122,123,124,125],

    "Name": ["Rahul","Priya","Amit","Neha","Rohan","Simran","Arjun","Pooja","Karan","Anjali",
             "Vikas","Sneha","Deepak","Meera","Raj","Tina","Sahil","Ritu","Aditya","Nisha",
             "Manoj","Kavita","Rakesh","Isha","Varun"],

    "Position": ["Chef","Waiter","Manager","Cashier","Cleaner",
                 "Waiter","Chef","Receptionist","Waiter","Chef",
                 "Cleaner","Waiter","Chef","Cashier","Manager",
                 "Waiter","Chef","Cleaner","Waiter","Receptionist",
                 "Chef","Waiter","Cleaner","Cashier","Manager"],

    "Salary": [35000,18000,50000,22000,15000,
               18000,36000,20000,17500,34000,
               15000,18500,35500,22000,48000,
               19000,36000,15000,18000,21000,
               37000,18500,15500,23000,49000]
}

df = pd.DataFrame(data)

print(df)


#CREATE A CHART WITH YOUR FILE WITH USING OF PANDAS NUMPY AND MATPLOT INCLUDING PIE CHART BAR CAHRT AND SCATTER PLOT.



name=input("Enter your name:")
age=int(input("Enter your age:"))
marks1, marks2, marks3=map(float, input("Enter marks in 3 subjects (separated by space):").split())
total=marks1+marks2+marks3
average=total/3
print("\n---Student Report---")
print(f"Name:{name}")
print(f"Age:{age}")
print("Marks:", marks1, marks2, marks3, sep=",")
print("Total Marks=", total)
print("Average marks=", round(average,2))
print("Thank You", end=" ")
print("For using this program!")