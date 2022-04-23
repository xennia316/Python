word = """EEk!"""
print(word)

#notes from class

start = 'Na' * 4 + '\n'
middle = 'Hey' * 3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)
print(end[-1])
print(end.replace('G', 'F'))
newEnd = start.split('t')
print(newEnd)
print(len(end))


st = 'a duck goes  into a bar...'
print(st.capitalize())
print(st.title())
print(st.upper())

thing = 'woodchuck'
place = 'lake'
now = 'The {} is in the {}.'.format(thing, place)
print(now)
#assignment from class

#5.1
song = """When an eel grabs your arm,
... And it causes great harm,
... That's - a moray!"""

Moray = song.startswith('m')
print(Moray)
print(song.replace('moray', 'Moray'))

#5.2
questions = [
 "We don't serve strings around here. Are you a string?",
 "What is said on Father's Day in the forest?",
 "What makes the sound 'Sis! Boom! Bah!'?"
 ]

answers = [
 "An exploding sheep.",
 "No, I'm a frayed knot.",
 "'Pop!' goes the weasel."
 ]
Q = 'Q:'
A = 'A:'

line1 = Q + questions[0] + '\n' + A + answers[1] + '\n'
line2 = Q + questions[1] + '\n' + A + answers[2] + '\n'
line3 = Q + questions[1] + '\n' + A + answers[0] + '\n'

#line1 = questions[0] + answers[1]
#line2 = questions[1] + answers[2]
#line3 = questions[2] + answers[0]

print(line1, line2, line3)


#Numbers
seconds = 60
minutes = 60
seconds_per_hour = seconds * minutes
print('Numbers: \n')
print('Number of seconds per hour:', seconds_per_hour)

day = seconds_per_hour * 24
print('Number of seconds a day', day)

floatDay = day / seconds_per_hour
print('as per float', floatDay)

intDay = day // seconds_per_hour
print('as per intergers: ', intDay)