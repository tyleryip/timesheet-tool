import re
import logging
from datetime import datetime

TIME_FORMAT = '%H:%M'

timespan_regex = re.compile("^([1-9][\d]?\:[\d]+)\-([1-9][\d]?\:[\d]+)$")

def parse_timesheet(input_file):
    output = ""

    tasks = {}
    current_task = ""

    # Parse line by line to extract tasks and convert timespans into durations
    lines = input_file.readlines()
    for line in lines:
        timespan_match = timespan_regex.match(line)

        # Skip empty lines
        if line.strip() == "":
            continue 

        if timespan_match:
            start = timespan_match.group(1)
            end = timespan_match.group(2)

            start_time = datetime.strptime(start, TIME_FORMAT)
            end_time = datetime.strptime(end, TIME_FORMAT)

            # Edge case: if task starts during the noon hour, 
            if start_time.hour == 12:
                start_time = start_time.replace(hour=0)

            # Edge case: if task starts in morning and ends in afternoon, we need to add 12 hours to the end time
            if end_time < start_time:
                end_time = end_time.replace(hour=end_time.hour + 12)

            time_delta = end_time - start_time
            duration_in_seconds = time_delta.total_seconds()
            duration_in_hours = duration_in_seconds / 3600

            logging.debug(f"{end_time=} {start_time=} {duration_in_hours=}")

            tasks[current_task] += duration_in_hours

        else:
            current_task = line.strip()
            if current_task not in tasks:
                tasks[current_task] = 0

    # Create the output string from the tasks
    for key, value in tasks.items():
        # Handle edge case for singular hour
        if value != 1:
            output += f"\n{key}\n{value} hours\n"
        else:
            output += f"\n{key}\n1 hour\n"

    return output
