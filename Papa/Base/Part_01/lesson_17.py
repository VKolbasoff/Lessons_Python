try:
    a = float("abc")
except ValueError:
    print("Cannot be reduce to a number!")

while True:
    a = input("Enter a positive number:  ")
    try:
        a = float(a)
        if a <= 0:
            raise Exception("The number is not positive!")
    except ValueError:
        print("Cannot be reduce to a number!")
    except Exception as exp:
        print(exp)
    else:
        print("Thanks for the correct input!")
    finally:
        print("The program is completed!")
        exit(0)


