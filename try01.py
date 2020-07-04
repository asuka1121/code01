try :
    from question import quest

    question_prompt = [
        "what is the color of an apple? \n(a) red/green \n(b) purple \n(c) blue\n\n",
        "what is the color of a watermelon? \n(a) yellow \n(b) green \n(c) pink\n\n",
        "what is the color of a strawberry? \n(a) yellow \n(b) purple \n(c) red \n\n "
    ]
    question = [
        quest(question_prompt[0], "a"),
        quest(question_prompt[1], "b"),
        quest(question_prompt[2], "c"),
    ]


    def run_question(quiz):
        score = 0
        count = 0
        while count < 3 :
            for quest in quiz:
                answers = ''
                answers = input(quest.prompt)
                answers = answers.lower()
                length = int(len(answers))
                if answers == quest.answer:
                    score += 1
                    count += 1
                else:
                    count += 1
                if length != 1 :
                    print("you can only enter either 'a' 'b' or 'c'")
                    break
 
        print("you have scored" + str(score) + "/" + str(len(question_prompt)))


    run_question(question)
except:
    print("something went wrong with the code")