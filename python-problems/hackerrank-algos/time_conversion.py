# Given a time in 12 - hour AM / PM format, convert it to military(24 - hour) time.
#
# Note: Midnight is 12:00: 00 AM on a 12 - hour clock, and 00: 00:00 on a 24 - hour clock.Noon is 12: 00:00 PM on a
# 12 - hour clock, and 12: 00:00 on a 24 - hour clock.
#
# Function
# Description
#
# Complete the timeConversion function in the editor below.It should return a new string representing the input time
# in 24 hour format.
#
# timeConversion has the following parameter(s):
#
# s: a string representing time in 12 hour format
# Input Format
#
# A single string s containing a time in 12 - hour clock format(i.e.: hh:mm: ssAM or hh:mm: ssPM), where 01 <= hh <=
# 12 and 00 <= mm, ss <= 59.
#
# Constraints
#
# All input times are valid
# Output Format
#
# Convert and print the given time in 24 - hour format, where 00 <= hh <= 23.
#
# Sample Input 0
# 07: 05:45PM
#
# Sample Output 0
# 19: 05:45
#


def time_conversion(s):
    hour, minute, second_ampm = s.split(':')
    if second_ampm[2:] == 'PM' and hour != '12':
        hour = str(int(hour) + 12)
    if second_ampm[2:] == 'AM' and hour == '12':
        hour = '00'
    if second_ampm[2:] == "PM" and hour == '12':
        hour = '12'
        return
    converted_time = hour + ':' + minute + ':' + second_ampm[0:2]
    print(converted_time)


time_conversion('12:05:45AM')
