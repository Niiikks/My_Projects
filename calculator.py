def calculator():
    while True:
        try:
            t = True
            a = float(input("შეიტანეთ a : "))
            x = input("შეიტანეთ მოქმედება (+, - , * , /) : ")
            b = float(input("შეიტანეთ b : "))
            print("--------------------------------------------------------------------------------------------")
            x = x.strip()
            if x == "+":
                ab = (a + b)
                print(ab)
            elif x == "-":
                ab = (a - b)
                print(ab)
            elif x == "*":
                ab = (a * b)
                print(ab)
            elif x == "/":
                ab = (a / b)
                print(ab)
            else:
                print("მოქმედება არასწორია")
            while t:
                x = input("შეიტანეთ მოქმედება (+, - , * , /) ან გაასაუფთავე ( c ) : ")
                if x == "c":
                    pass
                else:
                    b = float(input("შეიტანეთ b : "))
                    print("--------------------------------------------------------------------------------------------")
                x = x.strip()
                if x == "c":
                    print("გასუფთავდა")
                    print("--------------------------------------------------------------------------------------------")
                    t = False
                elif x == "+":
                    ab = (ab + b)
                    print(ab)
                elif x == "-":
                    ab = (ab - b)
                    print(ab)
                elif x == "*":
                    ab = (ab * b)
                    print(ab)
                elif x == "/":
                    ab = (ab / b)
                    print(ab)
                else:
                    print("მოქმედება არასწორია")
        except ZeroDivisionError:
            print("ნულზე გაყოფა შეუძლებელია")
        except ValueError:
            print("a და b აუცილებლად უნდა იყოს რიცხვი")

calculator()