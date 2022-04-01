# Convert date from {MMDDYYYY} format to {MMMM DD, YYYY} format

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

date = input("Enter date in MMDDYYYY format: ")
month_index = int(date[:2]) - 1
month = months[month_index]
day = date[2:4]
year = date[4:]

date_str = month + ' ' + day + ', ' + year
print(date_str)
