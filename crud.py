def is_valid_email(email):
    if "@" not in email:
        return False
    else:
        username, domain = email.split("@")
        if username and domain:
            if email.count("@") == 1:
                if "." in domain:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
def tri(i):
    if i==0:
        print("2 attempt left")
    elif i==1:
        print("1 attempt left")
    else :
        print("attempt over")
       
import json
main={}
print("____________welcome to CRUD by dic_____________")
while True:
    print("Create--1 \nRead--2 \nUpdate--3 \nDelete--4 \npress any num to exit--? \n")
    choose=input("choose your operation--")
    if choose=="1":
        name=input("Name--")
        while True :
            email=input("email--")
            if is_valid_email(email) == True:
                print("congrats email is correct")
                break
            else:
                print("oops wrong way to enter email :(")
        while True:
            phone=input("phone--")
            if str(phone).isnumeric()==True and len(str(phone))==10:
                break
            else:
                print("oops incorrect way to enter phone no :(") 
        while True:
            password=input("password--") 
            if len(password)>=8:
                dic={"name":name,"email":email,"phone":phone,"password":password}
                main.update({phone:dic})
                with open("myfile.json","w") as file:
                    json.dump(main,file,indent=5)
                break
            else:
                print("password length must be 8 :(")
    elif choose=="2":
        for i in range(3):
            phone1=input("phone number--")
            password1=input("Enter the Password--")
            with open("myfile.json","r") as file:
                x=json.load(file)
                if phone1 in x and password1==x[phone1]["password"]:
                    # with open("myfile.json","r") as file:
                    #   x=json.load(file,indent=5)
                    print(x[phone1])
                    break
                else:
                    print("its not there :(")
                    tri(i)
    elif choose=="3":
        print("please choose your updation \nname--1 \nemail--2 \nphone--3 \npassword--4")
        updation=input('--')
        if updation=="1":
            while True:
                user_id=input("input user phone no--")
                if user_id in main.keys():
                    main[user_id]["name"]=input("user new name--")
                    print("Updated name successfully :)")
                    break
                else:
                    print("Unknown phone no :(")  
        elif updation=="2":
            while True:
                user_id=input("input user phone no--")
                if user_id in main.keys():
                    main[user_id]["email"]=input("user new email--")
                    print("updated your email successfully :)")
                    break
                else:
                    print("unknown phoneno:(")    
        elif updation=="4":
            while True:
                user_id=input("input user phone no--")
                if user_id in main.keys():
                    main[user_id]["password"]=input("user new email--")
                    print("updated password successfully :) ")
                    break
                else:
                    print("unknown phoneno :(")
        elif updation=="3":
            while True:
                old_num=input('old phone--')
                new_num=input("new phone num--")
                if old_num in main.keys():
                    main[old_num]["phone"]=new_num
                    main[new_num]=main[old_num]
                    del main[old_num]
                    print("phone number update successfully ;)")
                    break
                else:
                    print("wrong phone no :(")
        else:
            print('wrong choice :(')
        with open("myfile.json","w") as file:
            json.dump(main,file,indent=5)
    elif choose=="4":
        print("please choose what you want deleted \nname--1 \nemail--2 \nphone--3 \npassword--4 \nDelete a user--5")
        choice=input('--')
        user_id=input("phone no--")
        password2=input("password--")
        with open("myfile.json","r") as file:
                x=json.load(file)
        if user_id in x.keys() and password2==x[user_id]["password"]:
            if choice=="1":
                del x[user_id]["name"]
            elif choice=="2":
                del x[user_id]["email"]
            elif choice=="3":
                del x[user_id]["phone"]
            elif choice=="4":
                del x[user_id]["password"]
            elif choice=="5":
                del x[user_id]
            else:
                print("enter correct choice :(")
            with open("myfile.json",'w') as file:
                json.dump(x,indent=5)
        else:
            print("you entered wrong details :(")
    else:
        break
