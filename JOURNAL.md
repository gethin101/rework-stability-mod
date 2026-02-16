
# 15/2/26 - First design & BOM
**Total time spent: 2h**

Today, I thought about how I can make my camera system and started to plan out the design in the readme. I did some research on components and put together a rough BOM with links and prices (as you can see below).
I first decided to use a generic camera remote like [this](https://www.amazon.co.uk/Wireless-Bluetooth-Shutter-Control-Compatible/dp/B0C3MDRGGQ/ref=sr_1_5?crid=1AUUAI6KZOU9P&dib=eyJ2IjoiMSJ9.QVLF0H7hQrvwdcD5cQPL7kmGSj1CB8wCJjuq92bOQZTdGuGGy8UuHkAomWuRWlMsNT12CPv4abk_rd7BKORY1ZI1Bq3hkXjuYGyrUjMXWgxQNq2ZkX04FeLPp8Tv0dhOy5ANBi-qcXodvXw1pUbV9qVUa6Xa152H0fe0YUT6wCSFRn7Tm3ruk35WeQFy8U-kx0qaj--o2apszfDS6qf9W77vzDKOmrJk2CwK9EbaQ30.U_yHoSGx9FSXXItNZ2bkZa7ZnEE9pOYg_1XBc-cTTfY&dib_tag=se&keywords=camera+clicker&qid=1771172995&sprefix=camera+clicker%2Caps%2C97&sr=8-5) but then switched to using a [KW11-3Z microswitch](https://www.amazon.co.uk/sourcing-map-KW11-3Z-B-Waterproof-Components/dp/B0DWMF8MR8/ref=sr_1_1?dib=eyJ2IjoiMSJ9.tpnlK1m80hUXBJH2E_WHKxRkCwrBlTrwzOuiSs5lKMpYclgZFreWDynS6G68xPrteMSH4lKrZzf1a96Jmdb0VIofummMqnfiHZgkJ87gzHpXwS0ZKiSoQsk3aje7yWF2ty3W7tV04EF2pkzfxkq2xbdmRXyU5YlKXkw0L_WHVt2JM6TSYk1Df7G61qV7FxNiZsD1I-rFTzcKpvC6d-_gBA3FCacXqkeyGBVScuRFj4c7TUP8e4xqNZxHpevmTDV2Xe3nBFzq0LKcQbocrUG5c_q9mu3MVlOg3UKI-kXOTYY.p1ZnE8hvDETavcqhbG3aCii5acrIZ0l1-uv4gXue6Vc&dib_tag=se&keywords=KW11-3Z+microswitch&qid=1771256687&sr=8-1) to lower costs and as it should be more interesting to use.

You can see below a simple wiring diagram I put together showing how the components will be connected and how my system will work, as well as how the BOM looks at the moment

<img width="700" alt="journal_1" src="https://github.com/user-attachments/assets/bc9c09c5-91e0-4785-bef4-2561009c7e43" />






---

# 16/2/26 -  Pico Keystrokes
**Total time spent: 2h**

Today, I did some messing around with the camera app on my computer and realised that all I need the pi pico to do is send an **enter** keystroke to the computer while the camera app is open using the webcam and it will take and save all of the photos into a folder that I can view them all later and stitch together to make the timelapse.

I wrote the simple script for the pico in CircuitPython that detects the switch being pressed through one of the GPIO pins (I have put it to 15 for now but I can change whenever), it waits 0.15 seconds to make sure the switch isn't triggered twice and sends **enter** to my computer.

You can see below the first iteration of my CircuitPython program and how I plan to wire the microswitch to the pico (COM -> GND and NO -> GPIO)


<img width="500" height="800" alt="journal_2" src="https://github.com/user-attachments/assets/e317b664-7587-4a4b-8131-6c55a3cc4914" />

I temporarily removed the firmware from a pico I own and wrote a test code to mimic how my camera system will work. 
As you can see, the button will be the microswitch that the printer toolhead will tap into and the pico will pick up on that and use adafruit-HID to send an **enter** keystroke to my laptop to take a photo with the camera.

![video](Assets/picoEnter_test.gif)

---

# 17/2/26 -  Custom G-Code
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
