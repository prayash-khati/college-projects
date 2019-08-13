#Importing various models i creared
import Invoice
import StockUpdate
import products

#Importing inbuilt functions
import random
import datetime

#Creating lists
alist=[]
blist=[]
clist=[]
dlist=[]
elist=[]
flist=[]
glist=[]


file=open("Stock.txt","r") #opening file for reading data
for line in file:
    d =line.split("\n")
    a=d[0]
    alist.append(a)
file.close()

blist.append(alist[0])
clist.append(alist[1])
dlist.append(alist[2])


for i in blist: #appending various data to different lists
    d=i.split(",")
    a=d[0]
    b=d[1]
    c=d[2]
    elist.append(a)
    elist.append(int(b))
    elist.append(int(c))

for i in clist: #appending various data to different lists
    d=i.split(",")
    a=d[0]
    b=d[1]
    c=d[2]
    flist.append(a)
    flist.append(int(b))
    flist.append(int(c))

for i in dlist: #appending various data to different lists
    d=i.split(",")
    a=d[0]
    b=d[1]
    c=d[2]
    glist.append(a)
    glist.append(int(b))
    glist.append(int(c))

def menu(): #Creating a function to show menu
    print("Press 1 to buy a product.")
    print("Press 2 to view the available products.")
    print("Press 3 to exit")
    return input("Enter your choice:")

def file(): #Creating a function to write a file
    a=str(random.randint(12000,100000))
    d=str(datetime.datetime.now())
    Invoice.file_write(a,name,choice,d,t_price,discount_p,quantity_p)
        
#Using while in order to keep the programing running until users decides to quit
print(products.inStock(elist,flist,glist))
while True:
    run=menu()
    if run=="1":
        choice1=input("What product would you like to buy? ")
        choice=choice1.upper() #Calling a module to convert lowercase string to uppercase string
        if choice=="MOUSE":
            if elist[1]>0:
                #Using exception handling to take correct input from the user
                success=False
                while success==False:
                    try:
                        quantity_p=int(input("How many products would you like to buy? "))
                        if quantity_p<=elist[1] and quantity_p>0:
                            success=True
                        else:
                            print("---------------------------------------------------------------")
                            print("Enter quantity is greater than or less than the available stock")
                            print("---------------------------------------------------------------")
                    except:
                        print("--------------------------------")
                        print("Please enter numbers for quantity")
                        print("--------------------------------")
                        
                print("Price=",elist[2])
                product=elist[1]
                q=product-quantity_p 
                print("Quantity=",quantity_p)
                a=elist[2]
                s1=False
                while s1==False:
                    dis1=input("Has discount been given(yes/no)?")
                    dis=dis1.upper()       
                    if dis=="YES":
                        #Using exception handling to take correct input from the user
                        success=False
                        while success==False:
                            try:
                                discount_p=int(input("Enter discount amount="))
                                if discount_p<=elist[2] and discount_p>0:
                                    success=True
                                else:
                                    print("-----------------------------------------------------------------------")
                                    print("Discount amount cannot be greater than or less than the mentioned price")
                                    print("-----------------------------------------------------------------------")
                            except:
                                print("---------------------------------------")
                                print("Please enter discount amount in numbers")
                                print("---------------------------------------")
                        s1=True
                        
                    elif dis=="NO":
                        discount_p=0
                        s1=True

                    else:
                        print("error")
                        s1=False
                  
                price=a*quantity_p 
                t_price=price-discount_p 
                print("Discount amount=",discount_p)
                print("Total Price=",t_price)
                name1=input("Enter your name=")
                name=name1.upper() 

                #Using exception handling to take correct input from the user
                s2=False
                while s2==False:
                    try:
                        final=input("Do you really want to purchase this product(yes/no)=")
                        final_choice=final.upper()
                        if final_choice=="YES":
                            elist[1]=q
                            file()
                            print("Thank you for your purchase")
                            s2=True
                        elif final_choice=="NO":
                            print(products.inStock(elist,flist,glist))
                            s2=True
                    except:
                        print("Error")
            else:
                print("----------------------")
                print("Currently not in stock")
                print("----------------------")
                
        elif choice=="HEADPHONE":
            if flist[1]>0:
                #Using exception handling to take correct input from the user
                success=False
                while success==False:
                    try:
                        quantity_p=int(input("Enter quantity="))
                        if quantity_p<=flist[1] and quantity_p>0:
                            success=True
                        else:
                            print("---------------------------------------------------------------")
                            print("Enter quantity is greater than or less than the available stock")
                            print("---------------------------------------------------------------")
                    except:
                        print("--------------------------------")
                        print("Please enter quantity in numbers")
                        print("--------------------------------")

                print("Price=",flist[2])
                product=flist[1]
                q=product-quantity_p
                print("Quantity=",quantity_p)
                a=elist[2]
                
                #Using exception handling to take correct input from the user
                s1=False
                while s1==False:
                    dis1=input("Has discount been given(yes/no)?")
                    dis=dis1.upper()       
                    if dis=="YES":
                        #Using exception handling to take correct input from the user
                        success=False
                        while success==False:
                            try:
                                discount_p=int(input("Enter discount amount="))
                                if discount_p<=flist[2] and discount_p>0:
                                    success=True
                                else:
                                    print("----------------------------------------------------------")
                                    print("Discount amount cannot be greater than the mentioned price")
                                    print("----------------------------------------------------------")
                            except:
                                print("---------------------------------------")
                                print("Please enter discount amount in numbers")
                                print("---------------------------------------")
                        s1=True
                        
                    elif dis=="NO":
                        discount_p=0
                        s1=True

                    else:
                        print("error")
                        s1=False
                  
                price=a*quantity_p
                t_price=price-discount_p
                print("Discount amount=",discount_p)
                print("Total Price=",t_price)
                name1=input("Enter your name=")
                name=name1.upper()
                
                #Using exception handling to take correct input from the user
                s2=False
                while s2==False:
                    try:
                        final=input("Do you really want to purchase this product(yes/no)=")
                        final_choice=final.upper()
                        if final_choice=="YES":
                            flist[1]=q
                            file()
                            print("Thank you for your purchase")
                            s2=True
                        elif final_choice=="NO":
                            print(products.inStock(elist,flist,glist))
                            s2=True
                    except:
                        print("Error")
            else:
                print("----------------------")
                print("Currently not in stock")
                print("----------------------")
                
        elif choice=="KEYBOARD":
            if glist[1]>0:
                success=False
                while success==False:
                    try:
                        quantity_p=int(input("Enter quantity="))
                        if quantity_p<=glist[1] and quantity_p>0:
                            success=True
                        else:
                            print("---------------------------------------------------------------")
                            print("Enter quantity is greater than or less than the available stock")
                            print("---------------------------------------------------------------")
                    except:
                        print("--------------------------------")
                        print("Please enter quantity in numbers")
                        print("--------------------------------")
                        
                print("Price=",glist[2])
                product=flist[1]
                q=product-quantity_p
                print("Quantity=",quantity_p)
                a=glist[2]   
                s1=False
                while s1==False:
                    dis1=input("Has discount been given(yes/no)?")
                    dis=dis1.upper()     
                    if dis=="YES":
                        #Using exception handling to take correct input from the user
                        success=False
                        while success==False:
                            try:
                                discount_p=int(input("Enter discount amount="))
                                if discount_p<=glist[2] and discount_p>0:
                                    success=True
                                else:
                                    print("-----------------------------------------------------------------------")
                                    print("Discount amount cannot be greater than or less than the mentioned price")
                                    print("-----------------------------------------------------------------------")
                            except:
                                print("---------------------------------------")
                                print("Please enter discount amount in numbers")
                                print("---------------------------------------")
                        s1=True
                        
                    elif dis=="NO":
                        discount_p=0
                        s1=True

                    else:
                        print("error")
                        s1=False
                  
                price=a*quantity_p
                t_price=price-discount_p
                print("Discount amount=",discount_p)
                print("Total Price=",t_price)
                name1=input("Enter your name=")
                name=name1.upper()

                s2=False
                while s2==False:
                    try:
                        final=input("Do you really want to purchase this product(yes/no)=")
                        final_choice=final.upper()
                        if final_choice=="YES":
                            glist[1]=q
                            file()
                            print("Thank you for your purchase")
                            s2=True
                        elif final_choice=="NO":
                            print(products.inStock(elist,flist,glist))
                            s2=True
                    except:
                        print("Error")
            else:
                print("----------------------")
                print("Currently not in stock")
                print("----------------------")
                        
        else:
            print("-----------------------------------------------")
            print("NOT IN STOCK OR USER ENTERED WRONG PRODUCT NAME")
            print("-----------------------------------------------")
            
    elif run=="2":
        print(products.inStock(elist,flist,glist))
            
    elif run=="3":
        a=",".join([str(i) for i in list5]) #Joins elemnts of list with" , "
        b=",".join([str(i) for i in list6]) #Joins elemnts of list with" , "
        c=",".join([str(i) for i in list7]) #Joins elemnts of list with" , "
        
        StockUpdate.read_file(a,b,c) #Calling a module to overwrite the main stock file
        break

    else:
        print("------------------------------")
        print("Please read the MENU carefully")
        print("------------------------------")





















    
