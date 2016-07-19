#organizate imports:
from datetime import datetime

#organizate variables
now = datetime.now()
#for date
current_year = now.year
current_month = now.month
current_day = now.day
#for time
current_hour = now.hour
current_minute = now.minute

timeVar = "Время"
timeVarUp = timeVar.upper()
timeVarDown = timeVarUp.lower()

dateVar = "Дата"
dateVarUp = dateVar.upper()
dateVarDown = dateVarUp.lower()

nameVar = "Имя"
nameVarUp = nameVar.upper()
nameVarDown = nameVarUp.lower()

moodVar = "Настроение"
moodVarUp = moodVar.upper()
moodVarDown = moodVarUp.lower()

my_name = "Моё имя"
my_nameUp = my_name.upper()
my_nameDown = my_nameUp.lower()

how_is_it_going = "Как дела?"
how_is_it_goingUp = how_is_it_going.upper()
how_is_it_goingDown = how_is_it_goingUp.lower()

how_old_are_you = "Сколько тебе лет?"
how_old_are_youUp = how_old_are_you.upper()
how_old_are_youDown = how_old_are_youUp.lower()

where_are_you_from = "Где ты живёшь?"
where_are_you_fromUp = where_are_you_from.upper()
where_are_you_fromDown = where_are_you_fromUp.lower()

########### ВРЕМЯ, ДАТА, ИМЯ, МОЁ ИМЯ, НАСТРОЕНИЕ,КАК ДЕЛА?, СКОЛЬКО ТЕБЕ ЛЕТ?
########### ГДЕ ТЫ ЖИВЁШЬ?

def time_time():
    """
    This function print`s current time.
    :return:
    """
    print('Часов:%s Минут:%s' % (current_hour, current_minute))

def date_date():
    """
    This function print`s current date.
    :return:
    """
    print('%s-%s-%s' % (current_day, current_month, current_year))
print("---------------------------------------------")
name = input("Давай познакомимся, как тебя зовут? ")
print()
print("У тебя прекрасное имя!", name)
print()
print("А теперь я покажу тебе свои способности!")
print()
print("Напиши следующие команды, а я выведу их на экран!")
while True:
    current_command = input("Время, Дата, Имя, Моё имя, Настроение, Как дела?,"
                            "Сколько тебе лет?, Где ты живёшь? ")
    print()
    if current_command == timeVar or current_command == timeVarUp or current_command == timeVarDown:
        time_time()
        print()
    elif current_command == dateVar or current_command == dateVarUp or current_command == dateVarDown:
        date_date()
        print()
    elif current_command == nameVar or current_command == nameVarUp or current_command == nameVarDown:
        print("Меня зовут Ио! :)")
        print()
    elif current_command == my_name or current_command == my_nameUp or current_command == my_nameDown:
        print("Я помню, тебя зовут ", name)
        print()
    elif current_command == moodVar or current_command == moodVarUp or current_command == moodVarDown:
        print("У меня отличное настроение! :) Надеюсь у тебя тоже!")
        print()
    elif current_command == how_is_it_going or current_command == how_is_it_goingUp or current_command == how_is_it_goingDown:
        print("Хорошо, люблю с тобой пообщаться :3")
        print()
    elif current_command == how_old_are_you or current_command == how_old_are_youUp or current_command == how_old_are_youDown:
        print("Мне 6 лет, но я робот :)")
        print()
    elif current_command == where_are_you_from or current_command == where_are_you_fromUp or current_command == where_are_you_fromDown:
        print("Я живу на планете Марс :)")
        print()
    else:
        print("Я не совсем понял твой вопрос.")
        print()
    next = int(input("Желаешь продолжить дальше(1-да,2-нет) "))
    if next == 1:
        pass
    elif next == 2:
        break
    else:
        print("Что?")
        print()