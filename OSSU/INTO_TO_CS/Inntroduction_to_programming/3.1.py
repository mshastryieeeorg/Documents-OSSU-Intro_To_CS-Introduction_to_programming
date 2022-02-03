hrs = input("Enter Hours:")
h = float(hrs)
rate = 10.5
pay = rate*h
overtime_rate = rate*1.5

if h > 40.0 :
    overtime_hours = h - 40.0
    Overtime_pay = 40*rate + overtime_hours*overtime_rate
    print(Overtime_pay)

elif h <= 40.0 :
    print(pay)
