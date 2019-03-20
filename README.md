Work time sheets generator
==========================

The generator script helps with routine of work timesheets population. It generates pairs of random work day start and end hours thus simulating those being populated by human.

Output of the script is pairs of day start and end hours delimited by tabs. It can be easily redirected into the file and then copypasted right into your excel/google doc.

Usage
-----

```sh
./karta_czasu.py
```

Example output:

    9:00    16:45
    8:45    17:00
    9:05    17:50
    9:00    16:50
    8:55    16:40
    8:55    16:20
    8:50    17:40
    9:05    17:15
    8:55    17:40
    8:45    17:00
    9:10    16:50
    9:10    16:25
    8:50    16:25
    9:10    17:45
    9:05    17:30
    8:55    17:40
    9:05    17:25
    8:45    16:00
    9:10    16:20
    9:00    16:15

Configuration
-------------

The following vars in the head of the script code can alter its behaviour:
- `start_time_default` - work day start time - minutes since 0:00
- `end_time_default` - work day end time - minutes since 0:00
- `start_min_deviation` - the earliest possible time you come to work - amount of minutes before `start_time_default`, negative number
- `start_max_deviation` - the latest possible time you come to work - amount of minutes since `start_time_default`
- `days` - amount of work days in the month
- `day_time_default` - amount of work hours per day - expressed in minutes
- `day_min_deviation` - how much shorter you work day can be comparing to the default - negative amount of minutes, absolute value should be equal to `day_max_deviation`
- `day_max_deviation` - how much longer you work day can be comparing to the default - positive amount of minutes, should be equal to the absolute value of `day_min_deviation`

TODO
----

- Make script parametrizable from CLI and env vars
- Implement the ability to provide not equal day time deviations
- Implement resulting start/end time report string (`time_str`)  as a separate class
- Create full featured python module
- Add tests

