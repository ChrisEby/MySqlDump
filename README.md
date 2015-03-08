MySql Dump
====================

#### Overview

Performs a mysql dump, compresses it, and drops it into a folder of your choosing.  Everything is specified in the settings.ini file.

#### Compatibility

Python 3.4+

#### Getting Started

Just run it first and it will generate a stock settings file.  From there it will exit and you can set up the settings.ini file with your information.  Then just re-run it and it will do its thing.

```
[mysql]
user = some_user
password = default
destination = /mnt/data/backups/mysql/current/
```

#### Caveats

The script is designed to be run on the server hosting the mysql instance you wish to back up.

And make sure the user has permission to run a mysqldump on the instance.

Enjoy!