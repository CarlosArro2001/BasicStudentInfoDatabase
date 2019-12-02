import sys 
#data storage declaration
stdID = [0,1,2,3,4,5,6,7,8,9]
stdName = ["Jim","Pam","Michael","Derek","Meredith","Chris","Patrick","Jonathan","Clement","Devon"]
stdAge = [15,15,16,16,17,17,18,18,15,16]
stdGen = ["M","F","M","M","F","M","M","M","F","M"]
stdNat = ["American","Spanish","French","British","British","Filipino/British","Japanese","Korean","French","Canadian"]
stdGrade= [9,9,10,10,11,11,12,12,9,10]
stdMath = [80,99,89,84,90,91,92,88,86,87]
stdEng  = [90,90,99,96,95,89,100,91,92,100]
stdSci  = [80,90,86,79,78,94,79,81,86,89]
stdECA1 = ["MUN","Basketball","Swimming","Dance","Robotics","MUN","Music","Art","Comp.Math","Robotics"]
stdECA2 = ["Robotics","Comp.Math","Art","Music","MUN","Robotics","Dance","Swimming","Basketball","MUN"]
stdEvents = ["MUN Conference 1","Mathlympics","Swim Comp.1","Dance Comp. 1","Robotics Comp.1","Robotics Comp.1","Dance Comp.1","Swim Comp.2","MathLympics","MUN Conference 2"]
#stdInfo function------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def stdInfo():
    print("Welcome to the student information database enter the letters for the following actions:")
    print("\n a - Read student data \n b - Enter a new students information")
    choice1 = input()
    if choice1 == "a":
        print("Please enter ID ")
        idInput = int(input())
        for i in stdID:
            if idInput == i :
                print("Found")
                break
            else :
                print("Not found")
                continue
        print("\n Name : " + stdName[idInput] + "\n Age : " + str(stdAge[idInput]) + "\n Gender :  " + stdGen[idInput] + "\n Nationality : " + stdNat[idInput] + "\n Grade " + str(stdGrade[idInput]))  
    if choice1 == "b":
        #Creation of student ID 
        newID = len(stdID)
        stdID.append(newID)
        print("Enter name : ")
        newName = input()
        stdName.append(newName)
        print("Enter age : ")
        newAge = int(input())
        stdAge.append(newAge)
        print("Enter Gender : ")
        newGen = input()
        stdGen.append(newGen)
        print("Enter Nationality : ")
        newNat = input()
        stdNat.append(newNat)
        print("Enter Grade : ")
        newGrade = int(input())
        stdGrade.append(newGrade)
        print("\n New student Details : ")
        print("\n ID :" + str(newID) +"\n Name :" + newName + "\n Age :" + str(newAge) + "\n Gender :" + newGen + "\n Nationality :" + newNat + "\n Grade :" + int(newGrade)) 
    print("Do you want to go to the main menu?")
    choice2 = input()
    if choice2 == "yes" or choice2 == "Yes":
        mainFunction()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
          


#stdInfo function
    
def TrackRecord():
    print("Welcome to the student track record database please enter the letters for the foklwing actions :")
    print("\n a - Enter new grade \n b - Display grade ")
    choice = input()
    if choice == "a":
        print("Please enter ID ")
        idInput = int(input())
        for i in stdID:
            if idInput == i :
                print("Found")
                break
            else :
                print("Not found")
                continue
        print("\n Enter grade for student : " + str(idInput))
        gradeIn = input()
        print("\n Enter subject for student : " + str(idInput)) 
        subjectIn = input()

        if subjectIn == "Math" or subjectIn == "math":
            stdMath[idInput] = gradeIn
        if subjectIn == "English" or subjectIn == "english":
            stdEng[idInput] = gradeIn
        if subjectIn == "Science" or subjectIn == "science":
            stdSci[idInput] = gradeIn     
        print("\n Grades for student " + str(idInput) + " have been updated")
    if choice == "b":
        print("Please enter ID ")
        idInput = int(input())
        for i in stdID:
            if idInput == i :
                print("Found")
                break
            else :
                print("Not found")
                continue
        print("\n The grades for student : " + str(idInput))
        print("\n Math : " + str(stdMath[idInput]))
        print("\n English : " + str(stdEng[idInput]))
        print("\n Science : " + str(stdSci[idInput]))

    print("Do you want to go to the main menu?")
    choice2 = input()
    if choice2 == "yes" or choice2 == "Yes":
        mainFunction()
#stdInfo function
    
def eca():
    print("\n Welcome to the ECA Database (Extra Curricular Activities)")
    print("\n Enter the student ID to display the activities of the student")
    idInput = int(input())
    for i in stdID:
        if idInput == i :
            print("Found")
            break
        else :
            print("Not found")
            continue
    print("\n These are the ECA's and events attended by " + stdName[idInput])
    print("\nE.C.A 1 : " + stdECA1[idInput])
    print("\nE.C.A 2 : " + stdECA2[idInput])
    print("\n Events : " + stdEvents[idInput])
    
    print("Do you want to go to the main menu?")
    choice2 = input()
    if choice2 == "yes" or choice2 == "Yes":
        mainFunction()

#main function
def mainFunction():
    print("Hello Welcome to the Student Information Program (S.I.P) \n ")
    print("\n Choose the following numbers for each one of the actions")
    print("a - Access Basic Student information \nb - Access student Track Record \nc - Access students E.C.A (extra curricular activities) \nd - Exit program")
    print("\n Choice :")
    x = input()
    while x != "d":
        if x == "a":
            stdInfo()
        if x == "b":
            TrackRecord()
        if x == "c":
            eca()
        if x == "d":
            sys.exit(0)
    

#calling the mainFunction
mainFunction()
