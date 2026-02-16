
# 15/2/26, 15:32pm - First design & BOM
**Total time spent: 2h**

Today, I thought about how I can make my camera system and started to plan out the design in the readme. I did some research on components and put together a rough BOM with links and prices (as you can see below).

I decided to use a KW11-3Z microswitch as I think it will be interesting to use and it being small and compact will allow me to easily mount it to my printer.

You can see below a simple wiring diagram I put together showing how the components will be connected and how my system will work

<img width="700" alt="journal_1" src="https://github.com/user-attachments/assets/634a1383-e683-4871-98ee-7a4aa2ac729c" />





---

# 16/2/26, 14:28pm -  Pico Keystrokes
**Total time spent: 2h**

Today, I did some messing around with the camera app on my computer and realised that all I need the pi pico to do is send an **enter** keystroke to the computer while the camera app is open using the webcam and it will take and save all of the photos into a folder that I can view them all later and stitch together to make the timelapse.

I wrote the simple script for the pico in CircuitPython that detects the switch being pressed through one of the GPIO pins (I have put it to 15 for now but I can change whenever), it waits 0.15 seconds to make sure the switch isn't triggered twice and sends **enter** to my computer.

You can see below the first iteration of my CircuitPython program and how I plan to wire the microswitch to the pico (COM -> GND and NO -> GPIO)


<img width="500" height="800" alt="journal_2" src="https://github.com/user-attachments/assets/e317b664-7587-4a4b-8131-6c55a3cc4914" />

I temporarily removed the firmware from a pico I own and wrote a test code to mimic how my camera system will work. 
As you can see, the button will be the microswitch that the printer toolhead will tap into and the pico will pick up on that and use adafruit-HID to send an **enter** keystroke to my laptop to take a photo with the camera.

![video](Assets/picoEnter_test.gif)

---

# 17/2/26, 11.27am -  Custom G-Code
**Total time spent: 0.5h**

Today, I learnt how to make the G-code for my a1 mini where the toolhead will tap into the switch which will be positioned on the far left of the X-axis between every layer.
You can see the code below:


<img width="382" height="120" alt="image" src="https://github.com/user-attachments/assets/4d7f92a6-0082-45a7-b344-2437d0ffbb6a" />

My G-code in Bambu studio:

<img width="400" height="150" alt="image" src="https://github.com/user-attachments/assets/7f71817c-ad32-49c5-ad3b-8ba79284fc00" />







# Date -  title

[what'd a do]

[pics]

**Total time spent: ?**
