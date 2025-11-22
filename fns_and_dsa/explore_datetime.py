from datetime import datetime
def display_current_datetime():
    """Displays the current date and time."""
    now = datetime.now()
    # formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {now}")
# current_datetime = datetime.now()
display_current_datetime()
days_ahead = int(input("Enter the number of days to add to the current date:"))
def future_date(days_ahead):
    """Returns the date that is 'days_ahead' days from today."""
    future = current_datetime + datetime.timedelta(days=days_ahead)
    return future

print(f'future date: {future_date(days_ahead)}')
