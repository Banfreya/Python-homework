print("Как Вас зовут?")
username = input()
print("Здравствуйте, " + username + "!")
print("Как дела?")
answer = input()
match answer:
    case 'хорошо':
        print("Я за вас рада!")
    case 'плохо':
        print("Всё наладится!")
