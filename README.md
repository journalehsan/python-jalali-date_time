# Python Package for Persain Jalali Date convert
This class give Georgian date and time and return Persian date and time in string format. Dates can be out like this: 1400/01/01 or 1400/01/01 12:00:00 or شنبه اول فروردین 1400
# Example:
```
date = PersianJalaliDate()
print(date.get_jalali_date())
print(date.get_jalali_date_time())
print(date.get_jalali_date_time_with_custom_output(custom_output="%s:%m:%H %d/%M/%y"))
print(date.convert_to_jalali_date(datetime.datetime.now()))
print(date.convert_to_jalali_date_time(datetime.datetime.now()))
print(date.convert_to_jalali_date_time_with_custom_output(datetime.datetime.now(), custom_output="%s:%m:%H %d/%M/%y"))
print(date.convert_to_jalali(datetime.datetime.now()))
print(date.convert_to_time(datetime.datetime.now()))
print(date.gregorian_to_jalali(2021, 10, 1))
print(date.g_days_in_month)
print(date.j_days_in_month)
print(date.gregorian_to_jalali(2021, 10, 1))
```
