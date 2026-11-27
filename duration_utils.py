def parse_duration(duration_str: str) -> int:
    # Split the duration string into components
    parts = duration_str.split('')

    # Initialize total seconds to zero
    total_seconds = 0

    # Iterate over each part of the duration string
    for i, part in enumerate(parts):
        if part == 'd':
            # Calculate the number of seconds in a day and add it to total_seconds
            total_seconds += 86400
        elif part.isdigit():
            # Convert the digit to an integer and multiply by the appropriate unit
            value = int(part)
            if i == 0:
                total_seconds += value * 3600  # hours
            elif i == 1:
                total_seconds += value * 60   # minutes
            else:
                total_seconds += value       # seconds

    return total_seconds