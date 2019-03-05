
import random
import datetime

hours = 7
minutes = 30
message_1 = 'Alarm clock +5 min. '
my_subject = [ "Functional Analise", "English Language", "Game Theory", "Databases" ]
number_of_tryes = 1

print("First of all, I need to woke up.")

while True:
    woke_up = random.choice([True, False])
    if woke_up == True:
        print ("From the",number_of_tryes,"try..." ," Woke up time", datetime.time(hours, minutes))
        print ("Now it`s time to hawe a wash and clean teeth.")
        break
    if woke_up == False:
        number_of_tryes += 1
        print(datetime.time(hours, minutes), "Woke up: Not yet!\n", message_1)
        minutes += 5
        if minutes >= 60:
            minutes -= 60
            hours += 1

teeth_are_dirty = True
dirty_level = random.random()
movement_with_a_toothbrush = 0.1

while teeth_are_dirty:
    if dirty_level < 0 :
        print("Teeth are already clean!")
        teeth_are_dirty = False
    else:
        dirty_level -= movement_with_a_toothbrush
today_subjects = []
print("Next I`l make my bag...")
print ("Subjects for today are:")

for i in range(4):
    if random.choice([True, False]) == True:
        today_subjects += my_subject[i]
        print ("\t", my_subject[i])

print("So, now l`m ready for a good day...")









