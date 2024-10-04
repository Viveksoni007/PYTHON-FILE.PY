def main():
    

    try:
        a=int(input("Hey,  Enter the number is :"))
        print(a)


    except Exception as e:
        print(e)

    finally:   # finally kise bhi chlana hota hai chiye kaise bhi use karo finally print hogaha hi 
        print(" I Am Inside Finally ")
    print("Thank you dear!")

main()