# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "2:02"))
# print(add_time("8:16 PM", "466:02"))
# print(add_time("3:30 PM", "2:12", "Monday"))
# print(add_time("2:59 AM", "24:00", "saturDay"))


# Run unit tests automatically
main(module='test_module', exit=False)