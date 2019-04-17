#!/usr/bin/env python

import random

start_time_default = 540 # 9:00 (9 h since 0:00)
start_min_deviation = -5 # -15 min
start_max_deviation = 15 # +15 min
days = 22 # days per month
day_time_default = 480 # 8 h
day_min_deviation = -60 # -1 h
day_max_deviation = 60 # +1 h

def timeRandomizer(default_time, min_deviation, max_deviation, deviation_step=5):
  deviation_rand = random.randrange(min_deviation, max_deviation, deviation_step)
  time = default_time + deviation_rand
  return time

def dayTimesGenerator():
  times = []
  count = 1
  days_step = 2

  while(count<days): 
    day_time = timeRandomizer(day_time_default, day_min_deviation, day_max_deviation)
    times.append(day_time)
    next_day_time = day_time_default + (day_time_default - day_time)
    times.append(next_day_time)
    count += days_step
  else:
    if count == days:
      times.append(day_time_default*days-sum(times))
  
  return times

def startEndHoursGenerator(times):
  pairs = []

  for i in range(days):
    start_time = timeRandomizer(start_time_default, start_min_deviation, start_max_deviation)
    end_time = start_time + times[i]
    start_hour, start_min = divmod(start_time, 60)
    end_hour, end_min = divmod(end_time, 60)
    time_str = str(start_hour) + ':' + str(start_min).zfill(2) + '\t' + str(end_hour) + ':' + str(end_min).zfill(2)
    pairs.append(time_str)

  return pairs

########
# MAIN #
########

if __name__ == '__main__':

  day_times = dayTimesGenerator()
  print 'Total month time: {} min\n'.format(sum(day_times))

  # some additional shuffling for the generated day times
  random.shuffle(day_times)

  time_pairs = startEndHoursGenerator(day_times)
  print 'Work start/end pairs generated below are in tsv format and ready being pasted right in your excel/sheets timesheet\n'
  print '{}'.format('\n'.join(time_pairs))

  # Generating tsv file
  #with open('karta_czasu.tsv', 'w') as filehandle:  
  #  for time in time_pairs:
  #      filehandle.write('%s\n' % time)

