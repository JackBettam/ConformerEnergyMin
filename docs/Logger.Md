# Logger.py

This is a custom built logging package. The aim is to export a message to the log after a successful (or failed) step has occured. 


## Included functions
There is currently one function that can be imported. Documnetation is below:

### logger
Called by:
```
from includes.Logger import logger
logger('message')
```

This first checks if a log text file exists. Automatically, this is ```'log.txt'```, but a custom log file can be made by calling ```File = 'logfile.txt'```, with ```logfile.txt``` being whatever the logfile is called. This then appends the message string to the log file with the current time and date. This will not delete any previous message. Only strings can be accepted. 


## Pre-required packages
This requires the following packages from standard installs of Python:
* os
* datetime

If running in the same directory as Main.Py, the import section will not need 'includes'. 