import datetime
current_datetime = datetime.datetime.now()
print(f'current date and time: {current_datetime}')
days_ahead = int(input("Enter the number of days to add to the current date:"))
def future_date(days_ahead):
    """Returns the date that is 'days_ahead' days from today."""
    future = current_datetime + datetime.timedelta(days=days_ahead)
    return future

print(f'future date: {future_date(days_ahead)}')
