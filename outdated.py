months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        user=input("Date: ").strip()

        if "/" in user:
            month,day,year=user.split("/")
            month=int(month)
            day=int(day)
            year=int(year)

        elif "," in user:
            month_name,rest=user.split(" ",1)
            day,year=rest.split(",")
            day=int(day)
            year=int(year)
            month_name=month_name.strip().title()
            month=months.index(month_name)+1

        else:
            raise ValueError
        
        if not(1<=month<=12 and 1<=day<=31):
            raise ValueError
        
        print(f"{year:04}-{month:02}-{day:02}")
        break

    except ValueError:
        continue
