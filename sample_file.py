from persain_jalali_date import PersianJalaliDate# Example:
# date = PersianJalaliDate()
# print(date.get_jalali_date())
# print(date.get_jalali_date_time())
# print(date.get_jalali_date_time_with_custom_output(custom_output="%s:%m:%H %d/%M/%y"))
# print(date.convert_to_jalali_date(datetime.datetime.now()))
# print(date.convert_to_jalali_date_time(datetime.datetime.now()))
# print(date.convert_to_jalali_date_time_with_custom_output(datetime.datetime.now(), custom_output="%s:%m:%H %d/%M/%y"))
# print(date.convert_to_jalali(datetime.datetime.now()))
# print(date.convert_to_time(datetime.datetime.now()))
# print(date.gregorian_to_jalali(2021, 10, 1))
# print(date.g_days_in_month)
# print(date.j_days_in_month)
# print(date.gregorian_to_jalali(2021, 10, 1))
def main():
    date = PersianJalaliDate()
    print(date.get_jalali_date())
    print(date.get_jalali_date_time())
    print(date.get_jalali_date_time_with_custom_output(custom_output="%s:%m:%H %d/%M/%y"))
    print(date.convert_to_jalali_date(datetime.datetime.now()))
    print(date.convert_to_jalali_date_time(datetime.datetime.now()))
    print(
        date.convert_to_jalali_date_time_with_custom_output(datetime.datetime.now(), custom_output="%s:%m:%H %d/%M/%y"))
    print(date.convert_to_jalali(datetime.datetime.now()))
    print(date.convert_to_time(datetime.datetime.now()))
    print(date.gregorian_to_jalali(2021, 10, 1))
    print(date.g_days_in_month)
    print(date.j_days_in_month)
    print(date.gregorian_to_jalali(2021, 10, 1))
    # with day and month name
    print(date.convert_to_jalali_with_day_month_name(datetime.datetime.now()))


if __name__ == "__main__":
    main()
