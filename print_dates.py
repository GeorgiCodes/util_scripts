from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

# helpful to construct curl for elasticsearch index deletion
if __name__ == '__main__':
    start_date = date(2015, 7, 27)
    end_date = date(2015, 9, 18)
    dates = []
    for single_date in daterange(start_date, end_date):
        dates.append(single_date.strftime("%Y_%m_%d"))

    print ",".join(dates)
