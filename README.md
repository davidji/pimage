
I blew up my laptop by rebooting it with an SD card in it, and then trying to write a raspberry pi
image to it - which instead overwrote the start of my boot disk...

I decided the solution was a slightly more rigourous python script that finds
removeable media for you and won't proceed unless it can unmount all the volumes first.

I'm sure many other convenient features can be added as well.
