""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Calculate the amount of time between the first and last shutdowns.

    Args:
        logfile (str): The path to the log file.

    Returns:
        datetime.timedelta: The time difference between the first and last shutdowns.
    """
    shutdown_events = get_shutdown_events(logfile)

    if len(shutdown_events) < 2:
        # Not enough shutdown events to calculate time difference
        return None

    # Extract the date field from the first and last shutdown events
    first_shutdown_time_str = shutdown_events[0].split(' ', 2)[1]
    last_shutdown_time_str = shutdown_events[-1].split(' ', 2)[1]

    # Convert the date strings to datetime objects
    first_shutdown_time = logstamp_to_datetime(first_shutdown_time_str)
    last_shutdown_time = logstamp_to_datetime(last_shutdown_time_str)

    # Calculate the time difference
    time_difference = last_shutdown_time - first_shutdown_time

    return time_difference

# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
