# why we don't write directly the code why i we need finally?
# finally used in functions, finally will run even if the function returns otherwise not
def main():
    try:
        a = int(input("Enter a Number: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("I am inside finally")
