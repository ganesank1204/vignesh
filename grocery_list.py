grocery_list=[]
def add_item():
    itemA=input("enter item in a list:")
    grocery_list.append(itemA)
    print(itemA," is added to grocery_list")
def remove_item():
    try:
         itemA=input("enter item removed from list:")
         grocery_list.remove(itemA)
         print(itemA,"is removed from grocery_list")
    except ValueError:
        print("itemA is not found")
def view_list():
    if len(grocery_list)==0:
        print("grocery_list is empty")
    else:
        print("your grocery_list")
        for itemA in grocery_list:
            print(itemA)
def show_menu():
    print("\nMenu")
    print("1.add itemA")
    print("2.remove itemA")
    print("3. view itemA")
    print("4.exit")
def main():
    while True:
        show_menu()
        choice=int(input("enter choice by values"))
        if choice==1:
            add_item()
        elif choice==2:
            remove_item()
        elif choice==3:
            view_list()
        elif choice==4:
             print ("good bye!!")
             break
        else:
            print("enter a valid option")
main()