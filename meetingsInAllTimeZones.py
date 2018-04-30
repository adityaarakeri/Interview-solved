from datetime import datetime
import pytz

#all the timezones across the world
OTHER_TIMEZONES = [
    pytz.timezone('US/Eastern'),
    pytz.timezone('Pacific/Auckland'),
    pytz.timezone('Asia/Calcutta'),
    pytz.timezone('UTC'),
    pytz.timezone('Europe/Paris'),
    pytz.timezone('Africa/Khartoum'),
]

#format string this is very useful format
FMT = '%Y-%m-%d %H:%M:%S %Z%z'

while True:
    user_input = input('\nWhen is your meeting? user format MM/DD/YYYY HH:MM : ')
    try:
        local_date = datetime.strptime(user_input, '%m/%d/%Y %H:%M')
    except ValueError:
        print("{} does not seem to be a valid input, please use a valid format of MM/DD/YYYY HH:MM".format(user_input))
    else:
        local_date = pytz.timezone('US/Pacific').localize(local_date)
        utc_date = local_date.astimezone(pytz.utc) 

        output = []

        for timezone in OTHER_TIMEZONES:
            output.append(utc_date.astimezone(timezone))

        for appointment in output:
            print(appointment.strftime(FMT))
        break



