# python-SerialToOSC
----------------------
**A python script which generates handy, fast and (relatively) dirty python scripts to convert Arduino Serial data into OSC messages**

## Dependencies

* Python 2.x
* [pyOSC](https://pypi.python.org/pypi/pyOSC)
* pyserial (installed using python-pip)

Tested on various versions of *ubuntu 14.04 upwards

## How-to

I wrote the script that this generator was based on to convert a high-rate stream of orientation data coming from an Arduino over Serial into OSC messages so that they could be used in Processing, and later in SuperCollider. I've ended up using this format for almost every project that needed Arduino serial parsing since, as it is easy, quick and will keep running in the background if other programs crash.

This generator assumes that you are sending messages in a certain format, that is:
* the message starts with the string ```msg= ``` - this is part of a crude catching mechanism to stop python trying to parse any noise, which was quite common when I was working on these projects
* all messages are sent at once on line (ending with Serial.println)
* individual messages within these lines are separated by spaces

An example message from Arduino in the Serial Monitor would look something like this:

```msg= 400 49.9999 329 10 3 1 foo```

When this is set up (an example is in Examples/ExampleArduinoSketch/), running the script generator using ```python scriptGenerator.py``` will create a script to parse your data. You will give it the following information:

1. Name of your script (make sure it ends in .py)
2. The IP address you want to send the OSC messages to
3. The port you will be sending to (for example ```57120``` for SuperCollider)
4. The serial port you will be reading from (for example ```/dev/ttyACM0```)
5. The Baud rate of the Arduino
6. The number of values in the stream (not including ```msg= ```)
7. The address you want to send each individual message to (a / is added automatically - so ```data/movement/x``` will send to ```/data/movement/x```)
8. The data type of each individual message (```str```, ```int```, ```float``` and suchlike. These are casted in python, so if you have some unusual data see Python's [conversion functions](https://docs.python.org/2/library/functions.html) 

Then insert your Arduino, and assuming all of the data you provided matches what is going on, the Serial data should be converted to OSC and sent to the specified IP address and port.

## Example

There is a short example in the Examples folder, containing an Arduino sketch which sends the values of A0 and A1, a Python script which parses the two values and sends them to SuperCollider's default ports (if you are using this script your port may need changing from /dev/ttyACM0), and SuperCollider code to dump the OSC to the post window, and then use it to control some sine waves.

------------------------

This is primitive and is designed to work for this very particular instance of Arduino usage, but seeing as i've used it an awful lot myself I figured a write-up would be useful to someone at the very least. It has only been tested on the *ubuntus, but I don't see why it wouldn't work on OSX. If you've tested it please let me know how you get on.

NB: The script may have some trouble dealing with exceptionally fast data streams (if the script keeps terminating with invalid literal) - one solution for this is to just keep trying to run the script over and over again until it takes, or to slow your data down. :).

Sean
