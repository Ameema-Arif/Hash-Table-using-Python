from tabulate import tabulate

Directory = [""]*100

#We've to enter atleast 30 records in the table that's why

n = 30

#We are taking total 100 records from 0-99 becuase it is the max no. of 2 digit Hash addresses.
#In order to minimize the no. of collisions we will take any prime no. lesser than 99

m = 97

#*************************************************List of the 30 records which must be added into hash table*************************************************************

Records = [["","","63000","Hasan","021642880","03317866654"],["","","45556","Maham","0216646532","03243004007"],["","","40008","Danish","0213265098","03425678300"],
           
           ["","","56000","Mahmood","0219812340","03126700983"],["","","78123","Minal","0213007685","03278900564"],["","","15489","Zubair","0219807651","03346700432"],
           
           ["","","88201","Bilal","0215432346","03174567009"],["","","66448","Nida","0216543789","03006800985"],["","","23675","Taimoor","0213456547","03007832155"],
           
           ["","","23456","Ameema Arif","0216785432","03311337201"],["","","55432","Rameen","0217098654","03267890456"],["","","23529","Memoona Arif","0216667349","03306783214"],
           
           ["","","98723","Syed Arif Masood","0213567889","03002576701"],["","","88576","Nadeem","0215699411","03267555000"],["","","48871","Ahmed","0219888003","03148906850"],
           
           ["","","15438","Azhan","0216002486","03112111435"],["","","21570","Abiha","0215677789","03324567239"],["","","50406","Suleiman","0212009873","03404569806"],
           
           ["","","32158","Mahira","0216655432","03308745674"],["","","15879","Ishaq","0216778754","03222333550"],["","","96321","Mehrab","0215688324","03309099785"],
           
           ["","","78954","Sadaf","0214328579","03127699501"],["","","76768","Riffat","0217890055","03211786400"],["","","33333","Nafees","0215689906","03098555744"],
           
           ["","","32100","Rashid","0218856743","03014445098"],["","","78021","Sajida","02136667800","03213456098"],["","","78609","Usman","0215686743","03209876543"],

           
           ["","","67295","Nigar Arif","0215667889","03012894533"],["","","56349","Hira","0217655412","03139006237"],["","","43211","Zainab","0213689765","03008709654"],
           
           ["","","65478","Javed","0212348890","03338899567"],["","","20804","Seema","0214212567","03036784325"]]

#*********************************************Adding the Records to the Hash Table****************************************************************************************

for i in Records:
    Enum = int(i[2])
    Hashvalue = int(Enum % m)
    Hashadd = int(Enum % m)

    if Directory[Hashvalue] == "" :
        Records[Records.index(i)][0] = str(Hashvalue)
        Records[Records.index(i)][1] = str(Hashadd)
        Directory[Hashvalue] = i

    elif Directory[Hashvalue] != "" :
        
        while Directory[Hashvalue] != "" :
            if Hashvalue < 99:
                Hashvalue = Hashvalue+1

            elif Hashvalue == 99:
                Hashvalue = 0
                
        Records[Records.index(i)][0] = str(Hashvalue)
        Records[Records.index(i)][1] = str(Hashadd)
        Directory[Hashvalue] = i

#************All Records saved to the hash table according to the division method of hashing****************************************************************
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#****************Now moving towards the Insert, Search and View Functions***********************************************************************************
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#**************Using Division Method for Hashing And Doing Linear Probing where required********************************************************************
        
choice =  int(input("Press 1 to add a new record\nPress 2 to search a record\nPress 3 to view the Hash Table\n:"))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#***************************************************for adding a new record*********************************************************************************
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

if choice == 1:

#taking while loop ,so we can perform the same operation several times if needed
    while m>n:
        Enum = int(input("Enter a 5-digit Employee no. containing integers only:"))
        if Enum>9999 and Enum<100000:
            Ename = str(input("Enter Employee name(Don't leave this empty):"))
            Landline = str(input("Enter Landline no.(e.g:021*******)(Don't leave this empty):"))
            Mobile = str(input("Enter Mobile no.(e.g:03*********)(Don't leave this empty):"))

            Hashvalue = int(Enum % m)
            Hashadd = int(Enum % m)

#if the location is empty
            
            if Directory[Hashvalue] == "" :
                Rec = [str(Hashvalue),str(Hashadd),str(Enum),Ename,Landline,Mobile]
                
                Directory[Hashvalue] = Rec
                print("Record added successfully!")

                select = int(input("Press 1 to add another record\nPress 2 to view Hash Table\nPress 3 to Quit\n:"))
                if select == 1:
                    continue
                elif select == 2:
                    Headers = ["Serial No.","Hash Value","Employee No.","Employee Name","Landline No.","Mobile No."]
                    print(tabulate(Directory,headers=Headers,tablefmt="grid"))
                    break
                elif select == 3:
                    break

#if the location is not empty
                
            elif Directory[Hashvalue] != "" :
                while Directory[Hashvalue] != "" :
                    if Hashvalue < 99:
                        Hashvalue = Hashvalue+1

                    elif Hashvalue == 99:
                                Hashvalue = 0

                Rec = [str(Hashvalue),str(Hashadd),str(Enum),Ename,str(Landline),str(Mobile)]
                Directory[Hashvalue]= Rec
                        
                print("Record added successfully!")

                select = int(input("Press 1 to add another record\nPress 2 to view Hash Table\nPress 3 to Quit\n:"))
                if select == 1:
                    continue
                elif select == 2:
                    Headers = ["Serial No.","Hash Value","Employee No.","Employee Name","Landline No.","Mobile No."]
                    print(tabulate(Directory,headers=Headers,tablefmt="grid"))
                    break
                elif select == 3:
                    break

                                       
        else:
            print("Invalid Employee no.!")
            continue


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#****************************************************************for Searching a record*********************************************************************
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

elif choice == 2 :

#taking while loop ,so we can perform the same operation several times if needed
    while m>n:
        Enum = int(input("Enter a 5-digit Employee no. containing integers only:"))

        if Enum>9999 and Enum<100000:
            Hashvalue = int(Enum % m)
            Hashadd = int(Enum % m)
            
            if Directory[Hashvalue] == "" :
                print("\n")
                print("Hash Value=",Hashvalue)
                print("Record not found !")
                print("\n")
                print("No. of probes for unsuccessful search = 1")
                print("\n")

                select = int(input("\nPress 1 to search another record\nPress 2 to Quit\n:"))
                if select == 1:
                    continue
                elif select == 2:
                    break


            elif Directory[Hashvalue] != "" :
                
                if Directory[Hashvalue][2] == str(Enum):
                    Data = [Directory[Hashvalue]]
                    Headers = ["Serial No.","Hash Value","Employee No.","Employee Name","Landline No.","Mobile No."]
                    
                    print("\n")
                    print("No. of Probes for Successful Search = 1")
                    print("\n")
                    print(tabulate(Data,headers=Headers))
                    print("\n")

                    select = int(input("\nPress 1 to search another record\nPress 2 to Quit\n:"))
                    if select == 1:
                        continue
                    elif select == 2:
                        break



                elif Directory[Hashvalue][2] != str(Enum) :
                    probes = 1
                    
                    try:
                        while (Directory[Hashvalue][2] != str(Enum) and Directory[Hashvalue] != "") :
                            if Hashvalue < 99:
                                Hashvalue=Hashvalue+1
                                probes = probes+1

                            elif Hashvalue == 99:
                                Hashvalue=1
                                probes = probes+1

                        if Directory[Hashvalue][2] == str(Enum):
                            Data = [Directory[Hashvalue]]
                            Headers = ["Serial No.","Hash Value","Employee No.","Employee Name","Landline No.","Mobile No."]

                            print("\n")
                            print("No. of Probes for Successful Search = ",probes)
                            print("\n")
                            print(tabulate(Data,headers=Headers))
                            print("\n")

                            select = int(input("\nPress 1 to search another record\nPress 2 to Quit\n:"))
                            if select == 1:
                                continue
                            elif select == 2:
                                break

                    except IndexError:
                        
                            print("\n")
                            print("Hash Value=",Hashadd)
                            print("Record not found !")
                            print("\n")
                            print("No. of probes for unsuccessful search = ",probes)
                            print("\n")

                            select = int(input("\nPress 1 to search another record\nPress 2 to Quit\n:"))
                            if select == 1:
                                continue
                            elif select == 2:
                                break

                   
                    

        else:
            print("Invalid Employee no.!")
            continue
        

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#*******************************************************for viewing Hash Table*****************************************************************************
#----------------------------------------------------------------------------------------------------------------------------------------------------------
               
elif choice==3:
    Headers = ["Serial No.","Hash Value","Employee No.","Employee Name","Landline No.","Mobile No."]
    print(tabulate(Directory,headers=Headers,tablefmt="grid"))

    


    























           






