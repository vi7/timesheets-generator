#!/usr/bin/env python

import random
import operator

ops = {'+': operator.add,
       '-': operator.sub}

default_start_time = 540 # 9:00
default_end_time = 1020 # 17:00
start_time_deviation = 40 # -10 - +30 min
end_time_deviation = 80 # -10 - +70 min
goal_month_time = 9600 # 160 hour / month

report = {}
report_start_time_key = 'start_time'
report_end_time_key = 'end_time'

# tech statistics
iterations_num = 0

def timeRandomizer(default_time, deviation):
  deviation_rand = random.randint(0,deviation)
  if deviation_rand <= 10:
    op = random.choice(list(ops.keys()))
    time = ops.get(op)(default_time,deviation_rand)
  else:
    time = default_time + deviation_rand

  return time

########
# MAIN #
########

if __name__ == '__main__':
  
  while True:

    total_month_time = 0
    text_report = ''

    # create report
    for x in range(1,21):
      start_time = timeRandomizer(default_start_time,start_time_deviation)
      # print 'Start time is: {}'.format(start_time)

      end_time = timeRandomizer(default_end_time,end_time_deviation)
      # print 'End time is: {}'.format(end_time)

      report[x] = {report_start_time_key:start_time, report_end_time_key:end_time}

    # parse report
    for day_num, times in report.items():
      text_report += '\nDay ' + str(day_num) + '\n'
      day_total_time = times[report_end_time_key] - times[report_start_time_key]
      text_report += report_start_time_key + ' ' + str(times[report_start_time_key]) + '\n'
      text_report += report_end_time_key + ' ' + str(times[report_end_time_key]) + '\n'
      text_report += 'Total day time: ' + str(day_total_time) + '\n'
      total_month_time += day_total_time

      if total_month_time > goal_month_time:
        break

    iterations_num += 1

    if total_month_time == goal_month_time:
      break
    else:
      continue

  # print 'Total month time is {}'.format(total_month_time)
  print '\n==================\n'
  print 'Report for a month {}'.format(text_report)
  print '\nGenerated after {} iterations'.format(iterations_num)

  # for day_num, times in report.items():
  #   print '\nDay {}'.format(day_num)

  #   for time in times:
  #     print '{} is {}'.format(time, times[time])
