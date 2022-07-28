def date_formatter(date):

    dict = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }

    date_list = date.split('-')
    for month in dict:
        if date_list[1] == month:
            mes = dict[month]
    if len(date_list[2]) > 1:
        date_list[2] = date_list[2][1]
    new_date = mes + ' ' + date_list[2] + ', ' + date_list[0]
    return new_date
