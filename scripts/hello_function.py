import time
#try:except structure
def hello():
    print "Hello World!"
    time.sleep(10)

if __name__ == '__main__':
    try:
        hello()
    except KeyboardInterrupt:
        print 'Good bye'
