import time

# Specify the drive letter to be read
drive_letter = "E:"
raw_partition = "\\\\.\\"+drive_letter

# Define the length of data to be read
data_length = 1024*4

cycle = 0

# Define the time interval for repeated execution (unit: seconds)
interval = 60

while True:
    # Open the raw partition file and read data
    mark = 0
    with open(raw_partition, "rb") as f:
        while mark < 1024:
            data = f.read(data_length)
            mark += 1
            # Output the read data
            print("{}:{}:First {} bytes of {} raw partition: {}".format(cycle, mark, data_length, drive_letter, data))
            # Wait for a period of time before executing again
            time.sleep(interval)
    cycle += 1
