from datetime import timedelta, date

# helpful to construct curl for elasticsearch index deletion, search etc.
if __name__ == '__main__':
    start_date = date(2015, 7, 27)
    end_date = date(2015, 9, 18)
    dates = [(start_date + timedelta(days=d)).strftime("%Y_%m_%d") for d in range(0, (end_date-start_date).days + 1)]

    print ",".join(dates)
