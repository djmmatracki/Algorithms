


# [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
# ["10:00", "18:30"]

# 30



from datetime import datetime
from datetime import timedelta



def find_free_time(periods: list, day: list): # Return periods of free time for each person
    result = []
    day[0] = datetime.strptime(day[0], '%H:%M')
    day[1] = datetime.strptime(day[1], '%H:%M')

    for per in periods:
        per[0] = datetime.strptime(per[0], '%H:%M')
        per[1] = datetime.strptime(per[1], '%H:%M')

    if periods[0][0] - day[0] > timedelta(minutes=0):
        result.append([day[0], periods[0][0]])

    for i in range(len(periods)-1):
        if periods[i+1][0] - periods[i][1] > timedelta(minutes=0):
            result.append([periods[i][1], periods[i+1][0]])

    if day[1] - periods[-1][1] > timedelta(minutes=0):
        result.append([periods[-1][1], day[1]])

    return result

# for time_stamps_1 in free_time_1:
# for time_stamps_2 in free_time_2:

# if end_1 - start_2 > 30 min
# append ([end_1, start_2])

# if end_2 - start_1 > 30 min
# append ([end_2, start_1])


def find_meeting_options_time(periods_1: list, day_1: list, periods_2: list, day_2: list, meeting: int):

    result = []
    meeting_duration = timedelta(minutes=meeting)

    free_time_1 = find_free_time(periods_1, day_1)
    free_time_2 = find_free_time(periods_2, day_2)


    for per_1 in free_time_1:
        for per_2 in free_time_2:

            if per_2[1] - per_1[0] >= meeting_duration and per_2[0] <= per_1[0] <= per_2[1]:
                result.append([per_1[0], per_2[1]])

            if per_1[1] - per_2[0] >= meeting_duration and per_1[0] <= per_2[0] <= per_1[1]:
                result.append([per_2[0], per_1[1]])

    for element in result:
        element[0] = element[0].strftime("%H:%M")
        element[1] = element[1].strftime("%H:%M")

    return result
# [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
# ["9:00", "20:00"]

def main():

    periods_1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
    day_1 = ["9:00", "20:00"]

    periods_2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
    day_2 = ["10:00", "18:30"]



    print(find_meeting_options_time(periods_1, day_1, periods_2, day_2, 30))

if __name__ == '__main__':
    main()

# output-> [[11:30, 12:00], [15:00, 16:00], [18:00, 18:30]]
