# Gethin's A1 Mini Camera Systen

This is my custom camera system design for the Bambu lab A1 Mini made during [Hackclub's Rework program](https://rework.hackclub.com/). 

It uses custom G-code, a raspberry pi pico WH, a Logitech C270 webcam and a KW11-3Z microswitch to record smooth timelapses of my prints.


# How it works:

- Nozzle moves to specific position between layers through my custom G-code and taps into the microswitch 
- Raspberry Pi Pico WH wired to the microswitch detects the signal and sends keystrokes to computer
- Computer picks up the keystrokes and takes action (screenshot or take photo)
- Nozzle goes back to printing and repeats the process
- I will edit the photos together to make the timelapse

**I will need to design in CAD custom mounds for the switch and for the camera**

# Wiring

This is my first plan for the wiring and connections of all my components and how they will interact with each other. You can see how the printer sets of the switch, how the pico picks up the signal and passes on keybinds to the laptop via USB and how the computer takes pictures using the camera.

<p>
  <img src="Assets/wiring_1.png" alt="wiring image 1" width="700">
</p>



# Component BOM:

| Name | Use | Link | Price | US |
|------|-----|------|-------|----|
| Logitech C270 | Take photos of my prints | [link](https://www.amazon.co.uk/Logitech-Education-Widescreen-Correction-Noise-Reducing/dp/B07W7MNYXB/ref=sr_1_2?adgrpid=1180876387007368&dib=eyJ2IjoiMSJ9.vLz9cVkRNAa0ej75miJ5roxaHhB80-X1vhg_IQItC5pp6SZBMN7C67i30iICWQ9UK5X0pMIs5L_q8CmRK5GGDEAVTEHmQIuuIJNs-I7HcXIK31o3KDUrsjRxs4aXIMLv5Di0Kg7CNLcZ28hsaiL_3N6-iADth6JHPAExYaXMUGRhh17VmBxktVRJslJ5BGHOfcGe5q8HsrGj2UhopTzJK6nwmaxHogjW34LPzcsoIOw.9AucXKEudp3Nv-fHK4gMsy092TVqA7dq7eV0YdkbvuE&dib_tag=se&hvadid=73805053645591&hvbmt=be&hvdev=c&hvlocphy=246414&hvnetw=o&hvqmt=e&hvtargid=kwd-73804911389513%3Aloc-188&hydadcr=5054_2465234&keywords=logitech%2Bc270&mcid=c2c0258fb8393f31a8efafd4156b50a6&msclkid=115b1b2aae1d1728bdcd72bb48c33dcd&qid=1771169507&sr=8-2&th=1) | £15.99 | $21.82 |
| KW11-3Z microswitch  | Registers tap from printer | [link](https://www.aliexpress.com/item/1635599799.html?spm=a2g0o.productlist.main.10.7ecauiJbuiJbtT&algo_pvid=a4b0c7a8-eccd-498e-a2b7-f068ff1b265f&algo_exp_id=a4b0c7a8-eccd-498e-a2b7-f068ff1b265f-9&pdp_ext_f=%7B%22order%22%3A%22309%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21GBP%211.21%211.09%21%21%211.60%211.44%21%402103864c17711746884592468e7f50%2112000037070213569%21sea%21UK%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ac7b67d0a%3Bm03_new_user%3A-29895&curPageLogUid=ZispQDWkph9J&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1635599799%7C_p_origin_prod%3A) | £1.09 | $1.49 |
| Raspberry Pi Pico WH | Act as a HID to send signal to computer | [link](https://www.aliexpress.com/item/1005009646610678.html?spm=a2g0o.productlist.main.2.4fff499710NHCj&algo_pvid=8647a6a0-faaa-4c26-a72a-14cd1c1cc629&algo_exp_id=8647a6a0-faaa-4c26-a72a-14cd1c1cc629-1&pdp_ext_f=%7B%22order%22%3A%22125%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21GBP%213.99%213.99%21%21%215.27%215.27%21%40211b819117711727399704157e9c0f%2112000049755345588%21sea%21UK%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ac7b67d0a%3Bm03_new_user%3A-29895&curPageLogUid=vgdPdWfsgRRc&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009646610678%7C_p_origin_prod%3A) | £7.90 | $10.78 |
| 3D printed mounts | Secure clicker & camera | Printing legion | £? | $? |

Total = £24.98 or $34.09


# Firmware

I will need to program the Raspberry Pi Pico WH to recieve the signal from the microswitch and to act as a HID keyboard to send keystrokes to my computer via USB cable. 

I will likely program this in CircuitPython as I am relatively familiar with it.







## Rework criteria: **(temporary)**

- Full image of your project/'s CAD
- Short description of your project and why you made it
- BOM in table format
- Wiring diagram for your full project





