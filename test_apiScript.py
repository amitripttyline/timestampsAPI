import pytest
from apiScript import timestamp_inSec

#unit testCases
def test_invalid_timestamp_inSec
   # check for innavlid input data
   result = apiScript(2:41,9)
   assert result == []

def test_negative_timestamp_inSec
   # check for negative clock time stamp seconds
   result = apiScript(-3:40:50)
   assert result == []

def proper_12hourclock_timestamp_inSec
    # check for 12hour clock time stamp seconds
    result = apiScript(3:40:50)
    assert result == 3*60*60 + 40 *60 + 50

def clock24hr_timestamp_inSec
    # check for 24 clock time stamp seconds
    result = apiScript(13:40:50)
    assert result == 13*60*60 + 40 *60 + 50


