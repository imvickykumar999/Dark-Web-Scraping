# recently my lapi(in warrenty) ran into battery problem, so i had to go to service center...
# then i thought i should code an alarm which alert me when battery reach 97% then i could switch it off.
# while coding this programme i faced many errors and a time came when i thought i should leave this project,
# but i made hit and trials many experiments then finally i started working perfectly :)
    
# ALERT BOTH MAX AND MIN BATTERY =====================================Vs_ydv_02==========================================
    
import psutil, time
# import pyttsx3
# from IPython.display import clear_output
# import matplotlib.pyplot as plt
from pygame import mixer 

# if using a Jupyter notebook include
# %matplotlib inline

# colors = ['orange', 'red', 'purple', 'blue', 'green', 'brown', 'black']
i = 0
battery = psutil.sensors_battery()
# speaker = pyttsx3.init()

plugged = battery.power_plugged
percent = battery.percent

# maxbat = percent + 1
maxbat = 97
# percent +- instant for testing mode
minbat = 40
# minbat = percent - 1

alarm = 60  # sec

if plugged == False:
    plugged = "Not Plugged In"
else:
    plugged = "Plugged In"

status = str(percent) + '% | ' + plugged
print(status)

# speaker.say(status)
# speaker.runAndWait()

count, data = 0, []

while True:
# for i in range(10):

    battery = psutil.sensors_battery()
    pluggedbool = battery.power_plugged
    percent = battery.percent
    
    if pluggedbool == False:
        plugged = "Not Plugged In"
    else:
        plugged = "Plugged In"
        
    count += 1
    i += 1

    # data.append(percent)
    
#   from IPython.display import clear_output
#   clear_output(wait=True)
    
#   plt.plot(data, color = colors[i % len(colors)])
#   plt.xlabel('Time (seconds)')
#   plt.ylabel('Percent')
#   plt.title('Charging Status')
    
#   axes.set_ylim([0,100])
#   plt.ylim((0, 100))
#   plt.show()
    
    print(str(count), '). ', str(percent), '[', str(maxbat), str(minbat), ']', plugged, str(battery))
    time.sleep(120)

    if percent >= maxbat or percent <= minbat:
        
        winsound.Beep(1000)

        # mixer.init()

#        speaker.say('\nPRESS => ENTER to stop Alarm and CHANGE CHARGING PLUG STATUS : ')
#        speaker.runAndWait()
        
        # mixer.music.load("audio.mp3") 
        # mixer.music.set_volume(0.9) 
        # mixer.music.play() 

        # input('\nPRESS => ENTER to stop Alarm and CHANGE CHARGING PLUG STATUS : ')
#       time.sleep(alarm)
        # mixer.music.stop()

#       break
        time.sleep(alarm)
        continue

    else:
        continue
    