def get_year_D(date):
    newdate = []
    year = ''
    if date == '':
        return None
    else:
        newdate = date.split('/')
        if len(newdate[0]) != 2:
            return 0
        else:
            year = '20' + newdate[0]
            return year
