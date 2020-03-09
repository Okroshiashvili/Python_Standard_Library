


"""
The module provides access to several different types of clocks, each useful for different purposes.
"""



# Comparing Clocks

import textwrap
import time


available_clocks = [
    ("monotonic", time.monotonic),
    ("perf_counter", time.perf_counter),
    ("process_time", time.process_time),
    ("time", time.time),
]


for clock_name, func in available_clocks:
    print(textwrap.dedent('''\
    {name}:
        adjustable    : {info.adjustable}
        implementation: {info.implementation}
        monotonic     : {info.monotonic}
        resolution    : {info.resolution}
        current       : {current}
    ''').format(
        name=clock_name,
        info=time.get_clock_info(clock_name),
        current=func())
    )



# Wall Clock Time

"""
Prints number of seconds since the start of epoch.
For Unix systems, epoch starts 0:00, January 1, 1970.
"""

print()
print("+" * 40)

print('The time is :', time.time())



# Processor Clock Time


"""
The value returned by "process_time()" reflect the actual time
used by the program as it runs.
"""

print()
print("+" * 40)


for i in range(5):
    print("Process time is :", time.process_time())
    time.sleep(2)
    print("Process time after delay :", time.process_time())
