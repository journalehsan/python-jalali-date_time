"""
This class give Georgian date and time and return Persian date and time in string format.
Dates can be out like this: 1400/01/01 or 1400/01/01 12:00:00 or شنبه اول فروردین 1400
Or Dates with day name: شنبه اول فروردین 1400   12:00:00
Or Dates with month name: 1400/01/01 12:00:00
Or Dates with day and month name: شنبه اول فروردین 1400
Or Dates with day name and month number: شنبه 01 فروردین 1400
Or Dates with month name and day number: 1400/01/01
Or Dates with month name and day name: 01 فروردین 1400
Or Dates with day name and month name: شنبه 1 فروردین 1400
"""
import datetime
from typing import Union


class PersianJalaliDate:
    def __init__(self):
        self.georgian_date = None
        self.jalali_date = None
        self.jalali_date_time = None
        self.jalali_date_time_with_custom_output = None  # output like %s or %d or %m or %y or %H or %M or %S

    def get_jalali_date(self, georgian_date: Union[datetime.datetime, datetime.date] = None) -> str:
        if georgian_date is None:
            self.georgian_date = datetime.datetime.now()
        else:
            self.georgian_date = georgian_date
        self.jalali_date = self.convert_to_jalali_date(self.georgian_date)
        return self.jalali_date

    def get_jalali_date_time(self, georgian_date: Union[datetime.datetime, datetime.date] = None) -> str:
        if georgian_date is None:
            self.georgian_date = datetime.datetime.now()
        else:
            self.georgian_date = georgian_date
        self.jalali_date_time = self.convert_to_jalali_date_time(self.georgian_date)
        return self.jalali_date_time

    def get_jalali_date_time_with_custom_output(self, georgian_date: Union[datetime.datetime, datetime.date] = None,
                                                custom_output: str = None) -> str:
        if georgian_date is None:
            self.georgian_date = datetime.datetime.now()
        else:
            self.georgian_date = georgian_date
        self.jalali_date_time_with_custom_output = self.convert_to_jalali_date_time_with_custom_output(
            self.georgian_date, custom_output)
        return self.jalali_date_time_with_custom_output

    def convert_to_jalali_date(self, georgian_date: Union[datetime.datetime, datetime.date]) -> str:
        year, month, day = self.convert_to_jalali(georgian_date)
        return f"{year}/{month}/{day}"

    def convert_to_jalali_date_time(self, georgian_date: Union[datetime.datetime, datetime.date]) -> str:
        year, month, day = self.convert_to_jalali(georgian_date)
        hour, minute, second = self.convert_to_time(georgian_date)
        return f"{year}/{month}/{day} {hour}:{minute}:{second}"

    def convert_to_jalali_date_time_with_custom_output(self, georgian_date: Union[datetime.datetime, datetime.date],
                                                       custom_output: str) -> str:
        year, month, day = self.convert_to_jalali(georgian_date)
        hour, minute, second = self.convert_to_time(georgian_date)
        custom_output = custom_output.replace("%s", str(second))
        custom_output = custom_output.replace("%m", str(minute))
        custom_output = custom_output.replace("%H", str(hour))
        custom_output = custom_output.replace("%d", str(day))
        custom_output = custom_output.replace("%M", str(month))
        custom_output = custom_output.replace("%y", str(year))
        return custom_output

    def convert_to_jalali(self, georgian_date: Union[datetime.datetime, datetime.date]) -> tuple:
        g_y = georgian_date.year
        g_m = georgian_date.month
        g_d = georgian_date.day
        jalali_date = self.gregorian_to_jalali(g_y, g_m, g_d)
        return jalali_date

    # with day name
    def convert_to_jalali_with_day_name(self, georgian_date: Union[datetime.datetime, datetime.date]) -> str:
        year, month, day = self.convert_to_jalali(georgian_date)
        day_name = self.get_day_name(georgian_date)
        return f"{day_name} {day}/{month}/{year}"

    def convert_to_jalali_with_month_name(self, georgian_date: Union[datetime.datetime, datetime.date]) -> str:
        year, month, day = self.convert_to_jalali(georgian_date)
        month_name = self.get_month_name(month)
        return f"{day} {month_name} {year}"

    def convert_to_jalali_with_day_month_number(self, georgian_date: Union[datetime.datetime, datetime.date]) -> str:
        year, month, day = self.convert_to_jalali(georgian_date)
        month_name = self.get_month_name(month)
        return f"{day}/{month} {year}"

    # with day and month name
    def convert_to_jalali_with_day_month_name(self, georgian_date: Union[datetime.datetime, datetime.date]) -> str:
        year, month, day = self.convert_to_jalali(georgian_date)
        month_name = self.get_month_name(month)
        day_name = self.get_day_name(georgian_date)
        return f"{day_name} {day} {month_name} {year}"

    def get_month_name(self, month: int) -> str:
        month_names = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
                       "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
        return month_names[month - 1]

    def get_day_name(self, georgian_date: Union[datetime.datetime, datetime.date]) -> str:
        day_names = ["شنبه", "جمعه", "پنجشنبه", "چهار شنبه", "سه شنبه", "دو شنبه", "یک شنبه"]
        return day_names[georgian_date.weekday()]

    def convert_to_time(self, georgian_date: Union[datetime.datetime, datetime.date]) -> tuple:
        g_h = georgian_date.hour
        g_m = georgian_date.minute
        g_s = georgian_date.second
        return g_h, g_m, g_s

    def gregorian_to_jalali(self, gregorian_year, gregorian_month, gregorian_day):
        """
        Convert a Gregorian date to a Jalali date.

        Args:
            gregorian_year (int): The year of the Gregorian date.
            gregorian_month (int): The month of the Gregorian date.
            gregorian_day (int): The day of the Gregorian date.

        Returns:
            tuple: A tuple containing the Jalali year, month, and day.
        """
        adjusted_year = gregorian_year - 1600
        adjusted_month = gregorian_month - 1
        adjusted_day = gregorian_day - 1

        # Calculate the number of days since the start of the Gregorian calendar
        gregorian_day_number = 365 * adjusted_year + (adjusted_year + 3) // 4 - (adjusted_year + 99) // 100 + (
                adjusted_year + 399) // 400

        # Add the number of days in each month up to the current month
        for i in range(0, adjusted_month):
            gregorian_day_number += self.g_days_in_month[i]

        # If it's a leap year and after February, add an extra day
        if adjusted_month > 1 and ((adjusted_year % 4 == 0 and adjusted_year % 100 != 0) or (adjusted_year % 400 == 0)):
            gregorian_day_number += 1

        gregorian_day_number += adjusted_day

        # Convert the Gregorian day number to a Jalali day number
        jalali_day_number = gregorian_day_number - 79

        # Calculate the number of 33-year cycles
        number_of_cycles = jalali_day_number // 12053

        # Calculate the remaining days within the current cycle
        jalali_day_number %= 12053

        # Calculate the Jalali year
        jalali_year = 979 + 33 * number_of_cycles + 4 * (jalali_day_number // 1461)

        # Calculate the remaining days within the current year
        jalali_day_number %= 1461

        # If it's a leap year, adjust the year and remaining days
        if jalali_day_number >= 366:
            jalali_year += (jalali_day_number - 1) // 365
            jalali_day_number = (jalali_day_number - 1) % 365

        # Calculate the Jalali month and day
        for i in range(0, 11):
            if jalali_day_number < self.j_days_in_month[i]:
                break
            jalali_day_number -= self.j_days_in_month[i]
        jalali_month = i + 1
        jalali_day = jalali_day_number + 1

        return jalali_year, jalali_month, jalali_day

    # Number of days in each month in the Gregorian calendar
    g_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Number of days in each month in the Jalālī calendar
    j_days_in_month = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]


# Example:
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
