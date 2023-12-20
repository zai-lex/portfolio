def FormatAnswer(Answers,Dashes):
    newlyformatedanswer=''
    # Numbers between [0-99]
    if len(Answers) == 1 and len(Dashes) == 3:
        newlyformatedanswer = '  ' + Answers
    elif len(Answers) == 1 and len(Dashes) == 4:
        newlyformatedanswer = '   '+ Answers
    elif len(Answers) == 2 and len(Dashes) == 3:
        newlyformatedanswer = ' ' + Answers
    elif len(Answers) == 2 and len(Dashes) == 4:
        newlyformatedanswer = '  ' + Answers
    elif len(Answers) == 3 and len(Dashes) == 4:
        newlyformatedanswer = ' ' + Answers
    # Numbers between [100-999]
    elif len(Answers) == 1 and len(Dashes) == 5:
        newlyformatedanswer= '    ' + Answers
    elif len(Answers) == 2 and len(Dashes) == 5:
        newlyformatedanswer= '   ' + Answers
    elif len(Answers) == 3 and len(Dashes) == 5:
        newlyformatedanswer= '  ' + Answers
    elif len(Answers) == 4 and len(Dashes) == 5:
        newlyformatedanswer = ' ' + Answers
    # Numbers between [1000-9999]
    elif len(Answers) == 1 and len(Dashes) == 6:
        newlyformatedanswer = '     ' + Answers
    elif len(Answers) == 2 and len(Dashes) == 6:
        newlyformatedanswer = '    ' + Answers
    elif len(Answers) == 3 and len(Dashes) == 6:
        newlyformatedanswer = '   ' + Answers
    elif len(Answers) == 4 and len(Dashes) == 6:
        newlyformatedanswer = '  ' + Answers
    elif len(Answers) == 5 and len(Dashes) == 6:
        newlyformatedanswer = ' ' + Answers
    
    return(newlyformatedanswer)




def arithmetic_arranger(problems,want_answers=None):
    #Prep Variables
    amount_of_problems=len(problems)
    list_of_formated_problems=list()
    whitespace='    '
    final_arangement=want_answers

    # Logic to prevent Errors
    if amount_of_problems > 5: 
        return('Error: Too many problems.') 

    for numbers in problems:
        brokenup_numbers=numbers.split()
        try:
            int(brokenup_numbers[0])
            int(brokenup_numbers[2])
        except:
            return('Error: Numbers must only contain digits.')
        
        if len(brokenup_numbers[0]) > 4 or len(brokenup_numbers[2]) > 4: 
            return('Error: Numbers cannot be more than four digits.')
        
        if brokenup_numbers[1] != '+' and brokenup_numbers[1] != '-': 
            return("Error: Operator must be '+' or '-'.")

        # Math to get the sum of the numbers
        if brokenup_numbers[1] == '+':
            answer=int(brokenup_numbers[0])+int(brokenup_numbers[2])
        else:
            answer=int(brokenup_numbers[0])-int(brokenup_numbers[2])



        if answer < 0:
            stringAnswer=str(answer)
            fakeanswer = stringAnswer.replace('-','') 
        else:
            stringAnswer=str(answer)
            fakeanswer = stringAnswer     


        # Formating the Numbers
        if len(brokenup_numbers[0]) == 4 or len(brokenup_numbers[2]) == 4 or len(fakeanswer) == 6:
            dashbar='------'
        elif len(brokenup_numbers[0]) == 3 or len(brokenup_numbers[2]) == 3 or len(fakeanswer) == 5:
            dashbar='-----'
        elif len(brokenup_numbers[0]) == 2 or len(brokenup_numbers[2]) == 2 or len(fakeanswer) == 4:
            dashbar='----'
        else:
            dashbar='---'

        # One Digit on Top
        if len(brokenup_numbers[0]) == 1 and len(brokenup_numbers[2]) == 1:
            if len(dashbar) == 4:
                newlyformated1='   ' + brokenup_numbers[0]
                newlyformated2='  ' + brokenup_numbers[2]
            else:
                newlyformated1='  ' + brokenup_numbers[0]
                newlyformated2=' ' + brokenup_numbers[2]
            newlyformatedanswer = FormatAnswer(stringAnswer,dashbar)
            
        elif len(brokenup_numbers[0]) == 1 and len(brokenup_numbers[2]) == 2:
            newlyformated1='   ' + brokenup_numbers[0]
            newlyformated2=' ' + brokenup_numbers[2]
            newlyformatedanswer = FormatAnswer(stringAnswer,dashbar)

        elif len(brokenup_numbers[0]) == 1 and len(brokenup_numbers[2]) == 3:
            newlyformated1='    ' + brokenup_numbers[0]
            newlyformated2=' ' + brokenup_numbers[2]
            newlyformatedanswer = FormatAnswer(stringAnswer,dashbar)

        elif len(brokenup_numbers[0]) == 1 and len(brokenup_numbers[2]) == 4:
            newlyformated1='     ' + brokenup_numbers[0]
            newlyformated2=' ' + brokenup_numbers[2]
            newlyformatedanswer = FormatAnswer(stringAnswer,dashbar)

        # Two Digits on Top
        elif len(brokenup_numbers[0]) == 2 and len(brokenup_numbers[2]) == 1:
            newlyformated1='  ' + brokenup_numbers[0]
            newlyformated2='  ' + brokenup_numbers[2]
            newlyformatedanswer = FormatAnswer(stringAnswer,dashbar)

        elif len(brokenup_numbers[0]) == 2 and len(brokenup_numbers[2]) == 2:
            if len(dashbar) == 5:
                newlyformated1='   ' + brokenup_numbers[0]
                newlyformated2='  ' + brokenup_numbers[2]
            else:
                newlyformated1='  ' + brokenup_numbers[0]
                newlyformated2=' ' + brokenup_numbers[2]
            newlyformatedanswer = FormatAnswer(stringAnswer,dashbar)

        elif len(brokenup_numbers[0]) == 2 and len(brokenup_numbers[2]) == 3:
            newlyformated1='   ' + brokenup_numbers[0]
            newlyformated2=' ' + brokenup_numbers[2]
            newlyformatedanswer = FormatAnswer(stringAnswer,dashbar)

        elif len(brokenup_numbers[0]) == 2 and len(brokenup_numbers[2]) == 4:
            newlyformated1='    ' + brokenup_numbers[0]
            newlyformated2=' ' + brokenup_numbers[2]
            newlyformatedanswer = FormatAnswer(stringAnswer,dashbar)

        # Three Digits on Top
        elif len(brokenup_numbers[0]) == 3 and len(brokenup_numbers[2]) == 1:
            newlyformated1='  ' + brokenup_numbers[0]
            newlyformated2='   '+ brokenup_numbers[2]
            newlyformatedanswer = FormatAnswer(stringAnswer,dashbar)

        elif len(brokenup_numbers[0]) == 3 and len(brokenup_numbers[2]) == 2:
            if len(dashbar) == 6:
                newlyformated1='   ' + brokenup_numbers[0]
                newlyformated2='   ' + brokenup_numbers[2]
            elif len(dashbar) == 5:
                newlyformated1='  ' + brokenup_numbers[0]
                newlyformated2='  ' + brokenup_numbers[2]
            newlyformatedanswer = FormatAnswer(stringAnswer,dashbar)

        elif len(brokenup_numbers[0]) == 3 and len(brokenup_numbers[2]) == 3:
            if len(dashbar) == 6:
                newlyformated1='   ' + brokenup_numbers[0]
                newlyformated2='  ' + brokenup_numbers[2]
            else:
                newlyformated1='  ' + brokenup_numbers[0]
                newlyformated2=' ' + brokenup_numbers[2]
            newlyformatedanswer = FormatAnswer(stringAnswer,dashbar)

        elif len(brokenup_numbers[0]) == 3 and len(brokenup_numbers[2]) == 4:
            newlyformated1='   ' + brokenup_numbers[0]
            newlyformated2=' ' + brokenup_numbers[2]
            newlyformatedanswer = FormatAnswer(stringAnswer,dashbar)

        # Four Digits on Top
        elif len(brokenup_numbers[0]) == 4 and len(brokenup_numbers[2]) == 1:
            newlyformated1='  ' + brokenup_numbers[0]
            newlyformated2='    ' + brokenup_numbers[2]
            newlyformatedanswer = FormatAnswer(stringAnswer,dashbar)

        elif len(brokenup_numbers[0]) == 4 and len(brokenup_numbers[2]) == 2:
            newlyformated1='  ' + brokenup_numbers[0]
            newlyformated2='   ' + brokenup_numbers[2]
            newlyformatedanswer = FormatAnswer(stringAnswer,dashbar)
            
        elif len(brokenup_numbers[0]) == 4 and len(brokenup_numbers[2]) == 3:
            newlyformated1='  ' + brokenup_numbers[0]
            newlyformated2='  ' + brokenup_numbers[2]
            newlyformatedanswer = FormatAnswer(stringAnswer,dashbar)
        
        elif len(brokenup_numbers[0]) == 4 and len(brokenup_numbers[2]) == 4:
            newlyformated1='  ' + brokenup_numbers[0]
            newlyformated2=' ' + brokenup_numbers[2]
            newlyformatedanswer = FormatAnswer(stringAnswer,dashbar)

        # Add all the variables to a list
        list_of_formated_problems.append(newlyformated1)
        list_of_formated_problems.append(brokenup_numbers[1])
        list_of_formated_problems.append(newlyformated2)
        list_of_formated_problems.append(dashbar)
        list_of_formated_problems.append(newlyformatedanswer)
    
    # Format all the problems and don't display the answer
    if want_answers == None:
        if amount_of_problems == 5:   
            final_arangement=(list_of_formated_problems[0]+whitespace+list_of_formated_problems[5]+whitespace+list_of_formated_problems[10]+whitespace+list_of_formated_problems[15]+whitespace+list_of_formated_problems[20]+'\n'
            +list_of_formated_problems[1]+list_of_formated_problems[2]+whitespace+list_of_formated_problems[6]+list_of_formated_problems[7]+whitespace+list_of_formated_problems[11]+list_of_formated_problems[12]+whitespace+list_of_formated_problems[16]+list_of_formated_problems[17]+whitespace+list_of_formated_problems[21]+list_of_formated_problems[22]+'\n'
            +list_of_formated_problems[3]+whitespace+list_of_formated_problems[8]+whitespace+list_of_formated_problems[13]+whitespace+list_of_formated_problems[18]+whitespace+list_of_formated_problems[23])
        if amount_of_problems == 4:   
            final_arangement=(list_of_formated_problems[0]+whitespace+list_of_formated_problems[5]+whitespace+list_of_formated_problems[10]+whitespace+list_of_formated_problems[15]+'\n'
            +list_of_formated_problems[1]+list_of_formated_problems[2]+whitespace+list_of_formated_problems[6]+list_of_formated_problems[7]+whitespace+list_of_formated_problems[11]+list_of_formated_problems[12]+whitespace+list_of_formated_problems[16]+list_of_formated_problems[17]+'\n'
            +list_of_formated_problems[3]+whitespace+list_of_formated_problems[8]+whitespace+list_of_formated_problems[13]+whitespace+list_of_formated_problems[18])
        elif amount_of_problems == 3:
            final_arangement=(list_of_formated_problems[0]+whitespace+list_of_formated_problems[5]+whitespace+list_of_formated_problems[10]+'\n'
            +list_of_formated_problems[1]+list_of_formated_problems[2]+whitespace+list_of_formated_problems[6]+list_of_formated_problems[7]+whitespace+list_of_formated_problems[11]+list_of_formated_problems[12]+'\n'
            +list_of_formated_problems[3]+whitespace+list_of_formated_problems[8]+whitespace+list_of_formated_problems[13])
        elif amount_of_problems == 2:
            final_arangement=(list_of_formated_problems[0]+whitespace+list_of_formated_problems[5]+'\n'
            +list_of_formated_problems[1]+list_of_formated_problems[2]+whitespace+list_of_formated_problems[6]+list_of_formated_problems[7]+'\n'
            +list_of_formated_problems[3]+whitespace+list_of_formated_problems[8])
        elif amount_of_problems == 1:
            final_arangement=(list_of_formated_problems[0]+'\n'
            +list_of_formated_problems[1]+list_of_formated_problems[2]+'\n'
            +list_of_formated_problems[3])
    
    # Format all the problems and do display the answers 
    elif want_answers == True:
        if amount_of_problems == 5:   
            final_arangement=(list_of_formated_problems[0]+whitespace+list_of_formated_problems[5]+whitespace+list_of_formated_problems[10]+whitespace+list_of_formated_problems[15]+whitespace+list_of_formated_problems[20]+'\n'
            +list_of_formated_problems[1]+list_of_formated_problems[2]+whitespace+list_of_formated_problems[6]+list_of_formated_problems[7]+whitespace+list_of_formated_problems[11]+list_of_formated_problems[12]+whitespace+list_of_formated_problems[16]+list_of_formated_problems[17]+whitespace+list_of_formated_problems[21]+list_of_formated_problems[22]+'\n'
            +list_of_formated_problems[3]+whitespace+list_of_formated_problems[8]+whitespace+list_of_formated_problems[13]+whitespace+list_of_formated_problems[18]+whitespace+list_of_formated_problems[23]+'\n'
            +list_of_formated_problems[4]+whitespace+list_of_formated_problems[9]+whitespace+list_of_formated_problems[14]+whitespace+list_of_formated_problems[19]+whitespace+list_of_formated_problems[24])
        elif amount_of_problems == 4:   
            final_arangement=(list_of_formated_problems[0]+whitespace+list_of_formated_problems[5]+whitespace+list_of_formated_problems[10]+whitespace+list_of_formated_problems[15]+'\n'
            +list_of_formated_problems[1]+list_of_formated_problems[2]+whitespace+list_of_formated_problems[6]+list_of_formated_problems[7]+whitespace+list_of_formated_problems[11]+list_of_formated_problems[12]+whitespace+list_of_formated_problems[16]+list_of_formated_problems[17]+'\n'
            +list_of_formated_problems[3]+whitespace+list_of_formated_problems[8]+whitespace+list_of_formated_problems[13]+whitespace+list_of_formated_problems[18]+'\n'
            +list_of_formated_problems[4]+whitespace+list_of_formated_problems[9]+whitespace+list_of_formated_problems[14]+whitespace+list_of_formated_problems[19])
        elif amount_of_problems == 3:
            final_arangement=(list_of_formated_problems[0]+whitespace+list_of_formated_problems[5]+whitespace+list_of_formated_problems[10]+'\n'
            +list_of_formated_problems[1]+list_of_formated_problems[2]+whitespace+list_of_formated_problems[6]+list_of_formated_problems[7]+whitespace+list_of_formated_problems[11]+list_of_formated_problems[12]+'\n'
            +list_of_formated_problems[3]+whitespace+list_of_formated_problems[8]+whitespace+list_of_formated_problems[13]+'\n'
            +list_of_formated_problems[4]+whitespace+list_of_formated_problems[9]+whitespace+list_of_formated_problems[14])
        elif amount_of_problems == 2:
            final_arangement=(list_of_formated_problems[0]+whitespace+list_of_formated_problems[5]+'\n'
            +list_of_formated_problems[1]+list_of_formated_problems[2]+whitespace+list_of_formated_problems[6]+list_of_formated_problems[7]+'\n'
            +list_of_formated_problems[3]+whitespace+list_of_formated_problems[8]+'\n'
            +list_of_formated_problems[4]+whitespace+list_of_formated_problems[9])
        elif amount_of_problems == 1:
            final_arangement=(list_of_formated_problems[0]+'\n'
            +list_of_formated_problems[1]+list_of_formated_problems[2]+'\n'
            +list_of_formated_problems[3]+'\n'
            +list_of_formated_problems[4])



    return(final_arangement) 