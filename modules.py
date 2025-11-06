from datetime import datetime
import math

now = datetime.now()
print(now.strftime("%I:%M:%S %p"))
print(now.strftime("%d-%b-%Y %I:%M %p"))

value = 4.87
print(float(value))  # converts to float (no effect here)
print(math.floor(value))  # rounds down (4)
print(math.ceil(value))  # rounds up (5)
