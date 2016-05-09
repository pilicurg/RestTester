# RestTester
a REST tester written in Python, Runs REST API tests which are defined by several test cases written in JSON format.

## Features
- test cases are written in JSON format
- assertion logic are separated from scripts codes, therefore you can replenish test cases in the TC folder and no modification is needed to scripts.
- no additional dependencies required
- rich and extendable assertion logic, such as equal, has, sorted, etc.
- assertion syntax are designed to be more human-readable

## usage

RestTester.py *TC_folder_name*


where *TC_folder_name* is TC by default. You can regard each folder as a test suite, thus you can run a test suite by specifying a folder name which contains that suite.

## test cases
All test cases are listed in a file named *TC_list.json*, where the authentication method is also defined, if there's any.

## test case example
```json
{
    "url": "/some/api/",
    "method": "POST",
    "headers": {
        "Content-Type":"application/json",
        "charset":"utf-8"
    },
    "body": {"payload":"some value"},
    "test": {
        "code": {"equals":200},
        "result.level1": {"has": "level2"},
        "result.level1.level2[2].somelist":{"sorted": "asc", "max": 10}
    }
}
```
### a brief explanation
The url, method, headers and body are necessary parameters to make a request so they must be defined explicitly except for method is GET if omitted.
The test part is for assertion, and is human readable. The supported assertions are:
- equals
- has
- sorted
- max
- min

 these logic can be easily extended in src/Tester.py
