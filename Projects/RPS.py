import random
import sys
while True:
    choice = input("აირჩიე ქაღალდი, ჭა ან მაკრატელი:")
    choices = ["ქაღალდი","ჭა","მაკრატელი"]
    f = random.choice(choices)

    if choice not in choices:
        print("კომპიუტერი: ჯერ წერა ისწავლე")
        sys.exit()
    else:
        print(f"შენ: {choice}")
        print(f"კოპიუტერი: {f}")
        if choice == "ქაღალდი" and f == "ჭა":
            print("შემ მოიგე")
        elif choice == "ჭა" and f == "მაკრატელი":
            print("შენ მოიგე")
        elif choice == "მაკრატელი" and f == "ქაღალდი":
            print("შენ მოიგე")
        elif choice == "ჭა" and f == "ჭა":
            print("ფრე")
        elif choice == "მაკრატელი" and f == "მაკრატელი":
            print("ფრე")
        elif choice == "ქაღალდი" and f == "ქაღალდი":
            print("ფრე")
        else:
            print("შენ წააგე")
    q = (input("გსურს თამაშინ გაგრძელება? კი/არა: "))
    if q != "კი":
        break
print("კარგად")