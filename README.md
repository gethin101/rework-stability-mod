# Gethin's A1 Mini Camera Systen

This is my custom camera system design for the Bambu lab A1 Mini designed and made during [Hackclub's Rework program](https://rework.hackclub.com/). 

It uses custom G-code, a raspberry pi pico 2H, a Logitech C270 webcam and a KW11-3Z microswitch to record smooth timelapses of my prints.


# How it works:

- Nozzle moves to specific position between layers through my custom G-code and taps into the microswitch 
- Raspberry Pi Pico 2H wired to the microswitch detects the signal and sends keystrokes to computer
- Computer picks up the keystrokes and takes action (screenshot or take photo)
- Nozzle goes back to printing and repeats the process every layer
- I will edit the photos together to make the timelapse

**I will need to design in CAD custom mounds for the switch and for the camera**

# Wiring

This is my first plan for the wiring and connections of all my components and how they will interact with each other. You can see how the printer sets of the switch, how the pico picks up the signal and passes on keybinds to the laptop via USB and how the computer takes pictures using the camera.

<p>
  <img src="Assets/wiring_1.png" alt="wiring image 1" width="700">
</p>



# Component BOM:

| Name | Use | Link | Quantity | Price | US |
|------|-----|------|----------|-------|----|
| Logitech C270 | Take photos of my prints | [link](https://www.amazon.co.uk/Logitech-Education-Widescreen-Correction-Noise-Reducing/dp/B07W7MNYXB/ref=sr_1_2?adgrpid=1180876387007368&dib=eyJ2IjoiMSJ9.vLz9cVkRNAa0ej75miJ5roxaHhB80-X1vhg_IQItC5pp6SZBMN7C67i30iICWQ9UK5X0pMIs5L_q8CmRK5GGDEAVTEHmQIuuIJNs-I7HcXIK31o3KDUrsjRxs4aXIMLv5Di0Kg7CNLcZ28hsaiL_3N6-iADth6JHPAExYaXMUGRhh17VmBxktVRJslJ5BGHOfcGe5q8HsrGj2UhopTzJK6nwmaxHogjW34LPzcsoIOw.9AucXKEudp3Nv-fHK4gMsy092TVqA7dq7eV0YdkbvuE&dib_tag=se&hvadid=73805053645591&hvbmt=be&hvdev=c&hvlocphy=246414&hvnetw=o&hvqmt=e&hvtargid=kwd-73804911389513%3Aloc-188&hydadcr=5054_2465234&keywords=logitech%2Bc270&mcid=c2c0258fb8393f31a8efafd4156b50a6&msclkid=115b1b2aae1d1728bdcd72bb48c33dcd&qid=1771169507&sr=8-2&th=1) | x1 | £15.99 | $21.82 |
| KW11-3Z microswitch  | Registers tap from printer | [link](https://www.amazon.co.uk/sourcing-map-KW11-3Z-B-Waterproof-Components/dp/B0DWMF8MR8/ref=sr_1_1?dib=eyJ2IjoiMSJ9.tpnlK1m80hUXBJH2E_WHKxRkCwrBlTrwzOuiSs5lKMpYclgZFreWDynS6G68xPrteMSH4lKrZzf1a96Jmdb0VIofummMqnfiHZgkJ87gzHpXwS0ZKiSoQsk3aje7yWF2ty3W7tV04EF2pkzfxkq2xbdmRXyU5YlKXkw0L_WHVt2JM6TSYk1Df7G61qV7FxNiZsD1I-rFTzcKpvC6d-_gBA3FCacXqkeyGBVScuRFj4c7TUP8e4xqNZxHpevmTDV2Xe3nBFzq0LKcQbocrUG5c_q9mu3MVlOg3UKI-kXOTYY.p1ZnE8hvDETavcqhbG3aCii5acrIZ0l1-uv4gXue6Vc&dib_tag=se&keywords=KW11-3Z+microswitch&qid=1771256687&sr=8-1) | x1 | £5.99| $8.16 |
| Raspberry Pi Pico 2H | Act as a HID to send signal to computer | [link](https://thepihut.com/products/raspberry-pi-pico-2?variant=54063366701441) | x1 | £5.40 | $7.36 |
| 3D printed mounts | Secure clicker & camera | Printing legion | x2 | £? | $? |

Total = £27.38 or $37.34


# Firmware

I have written the code for the pico in CircuitPython as I am relatively familiar with it. 
It recieves the signal from the microswitch through a GPIO pin and uses the adafruit_HID library to send an **enter** keystroke to my computer via USB cable. [The code can be seen here](Firmware/code.py)

I have also learnt how to write custom G-code for my printer so I can make it move into the microswitch between every layer.
[The g-code can be seen here](Firmware/printer.gcode)









## Rework criteria: **(temporary)**

- Full image of your project/'s CAD
- Short description of your project and why you made it
- BOM in table format
- Wiring diagram for your full project





