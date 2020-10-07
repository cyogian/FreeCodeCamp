import re
regStart = re.compile(r'(\d+):(\d+) (PM|AM)')
regDuration = re.compile(r'(\d+):(\d+)')
dayToNumber = {
  "sunday": 0,
  "monday": 1,
  "tuesday": 2,
  "wednesday": 3,
  "thursday": 4,
  "friday": 5,
  "saturday": 6
}
numberToDay = [
  "Sunday",
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday"
]
def add_time(start, duration, startingDay=None):
  temp = re.fullmatch(regStart, start)
  startHour = int(temp.group(1))
  startMinute = int(temp.group(2))
  if temp.group(3) == "PM":
    startHour += 12
  temp = re.fullmatch(regDuration, duration)
  durationHours = int(temp.group(1))
  durationMinutes = int(temp.group(2))
  startMinute += durationMinutes
  if startMinute >= 60:
    startHour += 1
    startMinute -= 60
  startHour += durationHours
  days = int(startHour / 24)
  startHour %= 24
  hr12 = "AM"
  if startHour >= 12:
    startHour -= 12
    hr12 = "PM"
  day = ""
  nod = ""
  zero_min = ""
  if startingDay:
    d = dayToNumber[startingDay.lower()]
    d += days
    day = f', {numberToDay[d % 7]}'
  if days == 1:
    nod = " (next day)"
  elif days > 1:
    nod = f' ({days} days later)'
  if startHour == 0:
    startHour = 12
  if startMinute < 10:
    zero_min = "0"  
  newTime = f'{startHour}:{zero_min}{startMinute} {hr12}{day}{nod}' 
  return newTime