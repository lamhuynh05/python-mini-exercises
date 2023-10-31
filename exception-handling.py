try: 
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to dividy by: "))
    result = numerator/denominator

except ValueError as e:
    print(e)
    print("Enter only numbers please")
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by 0 dummy")
except Exception as e: # catch all diff exceptions, but should have multiple exceptions
    print(e)
    print("something went wrong")

else:
    print(result) #only print result if there is no exception

finally: # final clause = always execute
    print("This will always execute") 