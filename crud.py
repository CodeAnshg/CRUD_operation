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
import json
main={}
print("____________welcome to CRUD by dic_____________")
while True:
    print("Create--1 \nRead--2 \nUpdate--3 \nDelete--4")
    choose=int(input("choose your operation--"))
    if choose==1:
        name=input("Name--")
        email=input("email--")
        if is_valid_email(email) == True:
            print("congrats email is correct")
            phone=int(input("phone--"))
            if str(phone).isnumeric()==True and len(str(phone))==10:
                password=input("password--")   
                dic={"name":name,"email":email,"phone":phone,"password":password}
                
                main.update({phone:dic})
                x = json.dumps(main,indent=5)
                with open("data.json",'w') as file:
                    file.write(x)
            else:
                print("oops incorrect way to enter phone no :(")  
        else:
            print("oops wrong way to enter email :(")
    elif choose==2:
        phone1=int(input("phone number--"))
        if phone1 in main :
            print(main[phone1])
        else:
            print("its not there :(")
    elif choose==3:
        print("please choose your updation \nname--1 \nemail--2 \nphone--3 \npassword--4")
        updation=int(input('--'))
        if updation==1:
            user_id=int(input("input user phone no--"))
            if user_id in main.keys():
                main[user_id]["name"]=input("user new name--")
                print("Updated phone number successfully :)")
            else:
                print("Unknown phone no :(")
            
        elif updation==2:
            user_id=int(input("input user phone no--"))
            if  user_id in main.keys():
                main[user_id]["email"]=input("user new email--")
                print("updated your email successfully :)")
            else:
                print("unknown phoneno:(")
            
        elif updation==4:
            user_id=int(input("input user phone no--"))
            if user_id in main.keys():
                main[user_id]["password"]=input("user new email--")
                print("updated password successfully :) ")
            else:
                print("unknown phoneno :(")
            
        elif updation==3:
            old_num=int(input('old phone--'))
            new_num=int(input("new phone num--"))
            if old_num in main.keys():
                main[old_num]["phone"]=new_num
                main[new_num]=main[old_num]
                del main[old_num]
                print("phone number update successfully ;)")
            else:
                print("wrong phone no :(")
        else:
            print('wrong choice :(')
    elif choose==4:
        print("please choose what you want deleted \nname--1 \nemail--2 \nphone--3 \npassword--4 \nDelete a user--5")
        choice=int(input('--'))
        user_id=int(input("phone no--"))
        if choice==1:
            del main[user_id]["name"]
        elif choice==2:
            del main[user_id]["email"]
        elif choice==3:
            del main[user_id]["phone"]
        elif choice==4:
            del main[user_id]["password"]
        elif choice==5:
            del main[user_id]
        else:
            print("enter correct choice :(")
    else:
        break