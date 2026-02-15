# Custom A1 Mini Camera Systen

This is my custom camera system design for the Bambu lab A1 Mini made during [Hackclub's Rework program](https://rework.hackclub.com/). It uses custom G-code, a raspberry pi pico WH, a Logitech C270 webcam and a camera clicker to record smooth timelapses of my prints.


# How it will work:

- Nozzle moves to specific positon between layers through my custom G-code and taps into the camera clicker
- Raspberry Pi Pico WH wired to the clicker detects the signal and sends command to computer
- Computer picks up the keybind and takes action (screenshot or take photo)
- Nozzle goes back to printing and repeats the process
- I will edit the photos together to make the timelapse

**I will need to design in CAD custom mounds for the switch and for the camera**


# Component BOM:

| Name | Use | Link | Price | US |
|------|-----|------|-------|----|
| Logitech C270 | Take photos of my prints | [link](https://www.amazon.co.uk/Logitech-Education-Widescreen-Correction-Noise-Reducing/dp/B07W7MNYXB/ref=sr_1_2?adgrpid=1180876387007368&dib=eyJ2IjoiMSJ9.vLz9cVkRNAa0ej75miJ5roxaHhB80-X1vhg_IQItC5pp6SZBMN7C67i30iICWQ9UK5X0pMIs5L_q8CmRK5GGDEAVTEHmQIuuIJNs-I7HcXIK31o3KDUrsjRxs4aXIMLv5Di0Kg7CNLcZ28hsaiL_3N6-iADth6JHPAExYaXMUGRhh17VmBxktVRJslJ5BGHOfcGe5q8HsrGj2UhopTzJK6nwmaxHogjW34LPzcsoIOw.9AucXKEudp3Nv-fHK4gMsy092TVqA7dq7eV0YdkbvuE&dib_tag=se&hvadid=73805053645591&hvbmt=be&hvdev=c&hvlocphy=246414&hvnetw=o&hvqmt=e&hvtargid=kwd-73804911389513%3Aloc-188&hydadcr=5054_2465234&keywords=logitech%2Bc270&mcid=c2c0258fb8393f31a8efafd4156b50a6&msclkid=115b1b2aae1d1728bdcd72bb48c33dcd&qid=1771169507&sr=8-2&th=1) | £15.99 | $21.82 |
| Camera clicker | Register clicks from printer | [link](https://www.amazon.co.uk/Wireless-Bluetooth-Shutter-Control-Compatible/dp/B0C3MDRGGQ/ref=sr_1_5?crid=1AUUAI6KZOU9P&dib=eyJ2IjoiMSJ9.QVLF0H7hQrvwdcD5cQPL7kmGSj1CB8wCJjuq92bOQZTdGuGGy8UuHkAomWuRWlMsNT12CPv4abk_rd7BKORY1ZI1Bq3hkXjuYGyrUjMXWgxQNq2ZkX04FeLPp8Tv0dhOy5ANBi-qcXodvXw1pUbV9qVUa6Xa152H0fe0YUT6wCSFRn7Tm3ruk35WeQFy8U-kx0qaj--o2apszfDS6qf9W77vzDKOmrJk2CwK9EbaQ30.U_yHoSGx9FSXXItNZ2bkZa7ZnEE9pOYg_1XBc-cTTfY&dib_tag=se&keywords=camera+clicker&qid=1771172995&sprefix=camera+clicker%2Caps%2C97&sr=8-5) | £4.99 | $6.81 |
| Raspberry Pi Pico WH | Act as a HID to send signal to computer | [link](https://www.aliexpress.com/item/1005009646610678.html?spm=a2g0o.productlist.main.2.4fff499710NHCj&algo_pvid=8647a6a0-faaa-4c26-a72a-14cd1c1cc629&algo_exp_id=8647a6a0-faaa-4c26-a72a-14cd1c1cc629-1&pdp_ext_f=%7B%22order%22%3A%22125%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21GBP%213.99%213.99%21%21%215.27%215.27%21%40211b819117711727399704157e9c0f%2112000049755345588%21sea%21UK%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ac7b67d0a%3Bm03_new_user%3A-29895&curPageLogUid=vgdPdWfsgRRc&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009646610678%7C_p_origin_prod%3A) | £7.90 | $10.78 |
| 3D printed mounts | Secure clicker & camera | Self-print | £0 | $0 |

Total = £28.88 or $39.42


# Firmware

I will need to program the Raspberry Pi Pico WH to recieve the signal from the clicker and to act as a HID keyboard to send keystrokes to my computer via USB cable. 

I will likely program this in CircuitPython as I am relatively familiar with it.







## Rework criteria: **(temporary)**

- Full image of your project/'s CAD
- Short description of your project and why you made it
- BOM in table format
- Wiring diagram for your full project



KW11‑3Z lever microswitch?

