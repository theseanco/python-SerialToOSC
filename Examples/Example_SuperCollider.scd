//run this to check the message is getting through - check the post window
OSCFunc.trace

//stop the trace
OSCFunc.trace(false)

//run to test the example script
(
p = ProxySpace.push(s);
~one = {arg f = 440, f2 = 440; SinOsc.ar([f*10,f2*10],0,0.1)};
~one.play;
OSCFunc({|msg| ~one.set(\f,msg[1])},'/val1')
OSCFunc({|msg| ~one.set(\f2,msg[1])},'/val2')
)