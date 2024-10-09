
# At 12:00am each morning you are given a list of timestamps for that day separated by a comma.
# Some timestamps may be different and some may be at the same time.
# Please write a Python script that sends an API call at each of the timestamps, accurate down to the second.
# If multiple timestamps are at the same time, the API calls must be sent at the same time.
# List of Times for a Given Day (24hr Hour:Minutes:Seconds): 09:15:25,11:58:23,13:45:09,13:45:09,13:45:09,17:22:00,17:22:00
# API Call to Send GET request to "ifconfig.co"

# Please send a Zip file that contains the python code and a readme on how to execute.
# You can import any native python packages (ex: datetime, urllib, etc...) you need but no 3rd party packages.

# Things we're looking for:
# proper readme
# doc strings
# logging
# ability to generate test times within a few seconds to test
# unit/integration tests
# breaking up the main function into smaller sub function
# moving the URL to a global config
# ability to accept timestamps via the CLI

# Things we're looking for:
# proper readme
# doc strings
# logging
# ability to generate test times within a few seconds to test
# unit/integration tests
# breaking up the main function into smaller sub function
# moving the URL to a global

import threading
import requests
import time
import logging

def timestamp_inSec(timestamps)
    # method to calculate the time
    timestamp_array = []
    for time in timestamps
        timestamp_individual = time.split(":")
        if timestamp_individual.length == 3
            result = 0
            for index, value in timestamp_individual
                if value >=0 & value < 60
                    if index == 0
                        result += (value *60 *60)
                    else if index == 1
                        result += (value *60)
                    else
                        result += value
                    end
                end
            end
            timestamp_array.append(result)
        else
            print("Provide valid input of timeStamp")
        end
    end
    return timestamp_array

def fetch_data(param)
    # method to fetch response
    response = requests.get('ifconfig.co', param)
    if response.status_code == 200:
        data = print(response.json())
        print(data)
    else
        print('Error:', response.status_code)
    end

threads = []
for param in timestamp_inSec:
    param_sec = timestamp_inSec(time)
    threads = threading.append(target=fetch_data(param_sec), args=('ifconfig.co', ))
    threads.append(thread)

    #  configure the log to report all messages
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    thread.start

for thread in threads:
    thread.join()

print "Elapsed Time: %s" % (time.time() - start)






    

       
      
       
       

    

