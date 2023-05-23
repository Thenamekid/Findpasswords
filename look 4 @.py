import re
import time

log_file = "log.txt"
last_at_timestamp = None
characters_typed = 0

while True:
    with open(log_file, "r") as f:
        # Read the entire file into a string
        contents = f.read()

        # Find all matches of the pattern @
        matches = re.findall(r"@", contents)

        # Check if the number of characters typed exceeds 50
        if characters_typed > 50:
            # Loop through each match
            for i, match in enumerate(matches):
                if i == 50:
                    break

                # Get the previous 30 words and the next 50 characters after the match
                start_index = max(0, contents.index(match) - 30)
                end_index = start_index + 80
                match_text = contents[start_index:end_index]

                # Print the match
                print(match_text)

                # Reset the characters typed counter
                characters_typed = 0

                # Update the last '@' symbol timestamp
                last_at_timestamp = time.time()

                # Add a delay of 1 second before printing the next match
                time.sleep(1)

        # Check if 2 minutes have passed since the last '@' symbol was pressed
        elif last_at_timestamp and time.time() - last_at_timestamp >= 120:
            # Print a message indicating that no matches were found within the time limit
            print(match_text)

            # Reset the characters typed counter
            characters_typed = 0

    # Wait for 1 second before checking the conditions again
    time.sleep(1)
