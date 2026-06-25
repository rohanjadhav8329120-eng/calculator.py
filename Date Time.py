from datetime import datetime
hour = datetime.now().hour
if hour < 12:
    print("Good Morning, Sir")
elif hour < 17:
    print("Good Afternoon, Sir")
else:
    print("Good Evenning, Sir")

# --------------------------------------------------------------------------------------------------

from datetime import datetime
hour = datetime.now().hour
if hour < 12:
    print("Good Morning, Sir")
elif hour < 17:
    print("Good Afternoon, Sir")
elif hour < 22:
    print("Good night, Sir")
else :
    print("Invalid Timing")