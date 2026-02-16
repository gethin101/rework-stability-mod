
# 15/2/26 - First design & BOM
**Total time spent: 2h**

Today, I thought about how I can make my camera system and started to plan out the design in the readme. I did some research on components and put together a rough BOM with links and prices (as you can see below).
I first decided to use a generic camera remote like [this](https://www.amazon.co.uk/Wireless-Bluetooth-Shutter-Control-Compatible/dp/B0C3MDRGGQ/ref=sr_1_5?crid=1AUUAI6KZOU9P&dib=eyJ2IjoiMSJ9.QVLF0H7hQrvwdcD5cQPL7kmGSj1CB8wCJjuq92bOQZTdGuGGy8UuHkAomWuRWlMsNT12CPv4abk_rd7BKORY1ZI1Bq3hkXjuYGyrUjMXWgxQNq2ZkX04FeLPp8Tv0dhOy5ANBi-qcXodvXw1pUbV9qVUa6Xa152H0fe0YUT6wCSFRn7Tm3ruk35WeQFy8U-kx0qaj--o2apszfDS6qf9W77vzDKOmrJk2CwK9EbaQ30.U_yHoSGx9FSXXItNZ2bkZa7ZnEE9pOYg_1XBc-cTTfY&dib_tag=se&keywords=camera+clicker&qid=1771172995&sprefix=camera+clicker%2Caps%2C97&sr=8-5) but then switched to using a [KW11-3Z microswitch](https://www.aliexpress.com/item/1635599799.html?spm=a2g0o.productlist.main.10.7ecauiJbuiJbtT&algo_pvid=a4b0c7a8-eccd-498e-a2b7-f068ff1b265f&algo_exp_id=a4b0c7a8-eccd-498e-a2b7-f068ff1b265f-9&pdp_ext_f=%7B%22order%22%3A%22309%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21GBP%211.21%211.09%21%21%211.60%211.44%21%402103864c17711746884592468e7f50%2112000037070213569%21sea%21UK%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ac7b67d0a%3Bm03_new_user%3A-29895&curPageLogUid=ZispQDWkph9J&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1635599799%7C_p_origin_prod%3A) to lower costs and as it should be more interesting to use.

You can see below a simple wiring diagram I put together showing how the components will be connected and how my system will work, as well as how the BOM looks at the moment

<img width="700" alt="journal_1" src="https://github.com/user-attachments/assets/bc9c09c5-91e0-4785-bef4-2561009c7e43" />






---

# 16/2/26 -  Pico Keystrokes
**Total time spent: 1h**

Today, I did some messing around with the camera app on my computer and realised that all I need the pi pico to do is send an **enter** keystroke to the computer while the camera app is open using the webcam and it will take and save all of the photos into a folder that I can view them all later and stitch together to make the timelapse.

I wrote the simple script for the pico in CircuitPython that detects the switch being pressed through one of the GPIO pins (I have put it to 15 for now but I can change whenever), it waits 0.15 seconds to make sure the switch isn't triggered twice and sends **enter** to my computer.

You can see below the first iteration of my CircuitPython program and how I plan to wire the microswitch to the pico (COM -> GND and NO -> GPIO)


<img width="500" height="800" alt="journal_2" src="https://github.com/user-attachments/assets/e317b664-7587-4a4b-8131-6c55a3cc4914" />

I temporarily removed the firmware from a pico I own and wrote a test code to mimic how my camera system will work. 
As you can see, the button will be the microswitch that the printer toolhead will tap into and the pico will pick up on that and use adafruit-HID to send an **enter** keystroke to my laptop to take a photo with the camera.

![video](Assets/picoEnter_test.gif)









# Date -  title

[what'd a do]

[pics]

**Total time spent: ?**
