import aiml
import os
# Create the kernel and learn AIML files
kernel = aiml.Kernel()
dire=os.getcwd()
#kernel.learn("/Users/russelwise/Howie-master/standard/startup.xml")
os.chdir(dire + '/Ai/' + 'aiml/')
for i in os.listdir(dire + '/Ai/'+'aiml/'):
    kernel.learn(i)
# Press CTRL-C to break this loop
while True:
    tosay= kernel.respond(raw_input("Enter your message >> "))
    os.system('say '+tosay)
    print tosay

