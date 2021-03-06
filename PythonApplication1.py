import os
#This is the menu function, this tells the user how to format the questions document and starts the test
def Menu():
    print("1)Start\n2)How to format the text file\n")
    try:
        choice=int(input())
    except (ValueError):
        print("Please enter a valid option\n")
        Menu()
    else:
        if choice==1:
            Main()
        elif choice==2:
            print("Place these symbols at the beginning of each line you want something to happen to\n ")
            print("!-End of the question\n*- Answer to the current question\nK- for the answers to the long answer questions\n")
            Menu()
        else:
            print("Please enter a valid answer\n")
            Menu()

#This function checks to see what the question type is and checks to see if it is the right answer
def CheckAnswer(AnswerNum,questionType,keyWordArray):
    userAnswer=""
    counter=0
    userAnswer=(input("Please enter Your answer: "))
    #If the question is a short answer
    if questionType!=1:
        if int(userAnswer)==AnswerNum:
            return(1)
        else:
             return(0)
    #If the answer is a long answer question
    else:
        userAnswer.lower()
        longAnswer=userAnswer.split()
        for i in range(len(longAnswer)):
            if longAnswer[i] in keyWordArray:
                counter+=1
            longAnswer[i]=None
    return(counter)

#This is the main function itlooks for the question type and question answers as well as printing the questions and finally the answers
def Main():
    questionType=0
    keyWordArray=list()
    numOfOptions=0
    answer=0
    answerStatus=list()

    #Gets file name and finds the path for it
    try:
        questionsFile=open(os.path.realpath(input("What is the file name of the quiz: "))+".txt",'r+')
    except FileNotFoundError:
                print("File name invalid. Please try again. NOTE: It has to be strongly typed(Uppercase matter) without any file extention(.txt)")
                Main()
    else:
        linesOfFile=questionsFile.readlines()
        for i in range(len(linesOfFile)):
            currentLine=linesOfFile[i]

            #Checks to see if it line is the end of the question
            if currentLine[0]=='!':
               answerStatus.append(CheckAnswer(answer,questionType,keyWordArray))
               numOfOptions=0
               answer=0

            #Checks if the current line is an answer
            elif currentLine[0]=='*':
                answer=numOfOptions
                questionType=0
                print(currentLine[1::])

            #Checks if the current line is a long question answer
            elif currentLine[0]=='K':
                questionType=1
                keyWordArray=currentLine[1::].split()

            #If none of the above happens then it reads the next line
            else:
                numOfOptions+=1
                print(currentLine)

        #Closes text file
        questionsFile.close()
        print("Here are your scores: ")
        for j in range(0,len(answerStatus)):
            print("Question",j, answerStatus[j])
            
Menu()
