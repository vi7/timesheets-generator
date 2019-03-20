#!/usr/bin/env python

import random

start_time_default = 540 # 9:00 (9 h since 0:00)
start_min_deviation = -5 # -15 min
start_max_deviation = 15 # +15 min
days = 20 # days per month
day_time_default = 480 # 8 h
day_min_deviation = -60 # -1 h
day_max_deviation = 60 # +1 h

def timeRandomizer(default_time, min_deviation, max_deviation, deviation_step=5):
  deviation_rand = random.randrange(min_deviation, max_deviation, deviation_step)
  time = default_time + deviation_rand
  return time

########
# MAIN #
########

if __name__ == '__main__':

  days_step = 2
  day_times = []
  times = []

  # work hours per day generator
  for i in range(0, days, days_step):
    day_time = timeRandomizer(day_time_default, day_min_deviation, day_max_deviation)
    day_times.append(day_time)
    next_day_time = day_time_default + (day_time_default - day_time)
    day_times.append(next_day_time)

  random.shuffle(day_times)

  # work start and end hours generator
  for i in range(days):
    start_time = timeRandomizer(start_time_default, start_min_deviation, start_max_deviation)
    end_time = start_time + day_times[i]
    start_hour, start_min = divmod(start_time, 60)
    end_hour, end_min = divmod(end_time, 60)
    time_str = str(start_hour) + ':' + str(start_min).zfill(2) + '\t' + str(end_hour) + ':' + str(end_min).zfill(2)
    times.append(time_str)

  print '{}'.format('\n'.join(times))

  # with open('karta_czasu.tsv', 'w') as filehandle:  
  #   for time in times:
  #       filehandle.write('%s\n' % time)
    
