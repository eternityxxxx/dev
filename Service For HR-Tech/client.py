import os, time, sys
pipe_name = os.getenv("HOME") + '/pipe_test'

def reader( ):
    pipein = open(pipe_name, 'r')
    while True:
        # remove line feed
        line = pipein.readline()[:-1]
        if len(line) > 0:
            print('Parent %d got "%s" at %s' % (os.getpid(), line, time.time( )))

if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)

reader()