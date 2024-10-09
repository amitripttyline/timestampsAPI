# timestampsAPI
Need to import below libraries
1. threading
2. requests
3. time
4. logging

timestampsAPI\apiScript.py
=> Codebase file to write the logic
   Methods: 
   timestamp_inSec -> Conversion of timeStamp data in second
   fetch_data  -> To request for the api with proper parameter
=> Rest request are kept for synchronous threading

timestampsAPI\test_apiScript.py 
=> Unit test case file to validate the data

Execute => write below command in py console
pythonX apiScript.py (X- whatever version installed)