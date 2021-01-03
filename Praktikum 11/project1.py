from datetime import datetime,timedelta

def diffDate(x):
    now = datetime.date(datetime.now())
    x = datetime.strptime(x, "%Y-%m-%d").date()
    return abs(x - now)

print("selisih harinya adalah {0} hari".format(diffDate("2020-12-30").days))