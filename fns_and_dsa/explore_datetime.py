# explore_datetime in python
def display_current_datetime():
    """A function to display the current date and time"""
    from datetime import datetime as dt

    current_date = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)


def calculate_future_date():
    """A function to calculate a future date given a number of days"""
    from datetime import datetime as dt

    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")
    future_date = (current_date + dt.timedelta(days=number_of_days)).strftime(
        "%Y-%m-%d")
    print(f"Future date: {future_date}")
