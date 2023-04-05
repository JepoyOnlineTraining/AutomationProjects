# Exception Handling
# - event that cause program termination
# - occurs when use got error


# # Example 1
#
# print("this is stating point of program....")
# print("this is stating point of program....")
# print("this is stating point of program....")
#
# try:
#     print(x)
# except:
#     print(f"Exception occured")
# print("this is end of program....")
# print("this is end of program....")
# print("this is end of program....")




# Example 3

try:
    num1, num2 = 10, 1
    result = num1/num2
    print(f"result is {result}")
except ZeroDivisionError:
    print("Thrown ZeroDivisionError")
except SyntaxError:
    print("This is syntax error")
except:
    print("This will print for other exception")
else:
    print("No exception")
finally:
    print("Always execute")

