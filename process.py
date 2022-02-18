# The file "um-server-01.txt" is accessed through the open() and is saved as a series of lists to the log_file variable
log_file = open("um-server-01.txt")

# Function decleration which is requiring a perameter
def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()  # Strips unwanted syntax from the string lines in log_file
        # Aqquires the first 3 values in the line string and assigns it to a varaible called day
        day = line[0:3]
        if day == "Mon":  # Check to see if the day variable matches the string 'Tue'
            # If there is a match, print the entire line from which day was aqquired.
            print(line)
    log_file.seek(0,0)

log_file.seek(0,0)

def give_me_melons(log_file):
    for line in log_file:
         line = line.rstrip()
         melon = int(line[16:18])
         if melon > 10:
             print(line)
    log_file.seek(0,0)

# Envokes the sales_reports fucntion and passing log_file as its argument
# sales_reports(log_file)

give_me_melons(log_file)