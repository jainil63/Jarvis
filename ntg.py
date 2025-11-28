import datetime


def get_greeting():
    current_hour = datetime.datetime.now().hour

    if 4 <= current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 5:
        return "Good afternoon!"
    else:
        return "Good evening!"


wish = get_greeting()
print(wish)
