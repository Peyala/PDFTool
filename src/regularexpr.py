import re

def parsePDFsInput(line):
    # Compile the regular expression
    regular_expression = re.compile(r"-?\d+(?:-\d+)?")

    # Search in the text string using the regular expression
    result = regular_expression.findall(line)

    # Create a list where we will store the pages numbers
    pages = []

    # Iterate over each result
    for r in result:
        # If the result contains a dash, it means it is a range of numbers
        if "-" in r:
            # Compile a regular expression to separate the range into two parts
            range_regular_expression = re.compile(r"(\d+)-(\d+)")
            
            # Search in the result using the regular expression
            ex_range = range_regular_expression.findall(r)
            
            # Get the start and end of the range
            start = ex_range[0][0]
            end = ex_range[0][1]
            
            # Convert the values to integers
            start = int(start)
            end = int(end)
            
            # Check if the range is valid (start <= end)
            if start <= end:
                # Add each number in the range to the list
                pages += range(start, end+1)
            else:
                # If the range is not valid, print an error message
                print("Error: invalid range '{}'".format(r))
                return None
        else:
            # If it doesn't contain a dash, just add the number to the list
            pages.append(int(r))

    # Print the list of numbers
    return pages
