# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    def get_time_and_number(row):
        '''
            get the number and time in ses
        '''
        timegap, number = row.split(',')
        number = int(''.join(number.split('-')))
        timegap = timegap.split(':')
        timesum = int(timegap[0]) * 24 * 60 + int(timegap[1]) * 60 + int(timegap[2])
        return timesum, number

    def cal_pay(timegap):
        '''
            calculate the cost of a preiod of time
        '''
        cost = 0
        if timegap < 300:
            cost = timegap * 3
        else:
            import math
            cost = math.ceil(timegap / 60) * 150
        return cost

    raw_data = S.split('\n')
    result_dict = {}
    for row in raw_data:
        timegap, number = get_time_and_number(row)
        cost = cal_pay(timegap)
        if number in result_dict:
            result_dict[number][0] = result_dict[number][0] + timegap
            result_dict[number][1] = result_dict[number][1] + cost
        else:
            result_dict[number] = [timegap, cost]

    longest_time, smallest_number, current_key = 0, 999999999, 0
    for key, value in result_dict.items():
        smallest_number = min(key, smallest_number)
        if longest_time <= value[0]:
            current_key = key
            longest_time = value[0]

    if result_dict[smallest_number][0] == longest_time:
        del result_dict[smallest_number]
    else:
        del result_dict[current_key]

    total_cost = 0
    for key in result_dict:
        total_cost = result_dict[key][1] + total_cost

    return total_cost


print(solution('''99:88:99,666-666-666\n00:04:55,666-666-666\n00:05:00,555-555-555'''))
