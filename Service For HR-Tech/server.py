import os, time, sys
pipe_name = os.getenv("HOME") + '/pipe_test'

def writer( ):
    pipeout = os.open(pipe_name, os.O_WRONLY)
    counter = 0
    while counter < 10:
        time.sleep(1)
        os.write(pipeout, 'Number %03d\n' % counter)
        #counter = (counter+1) % 5
        counter = counter + 1
    os.close(pipeout)

writer()