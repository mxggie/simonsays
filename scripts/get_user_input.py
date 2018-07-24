from getpass import getpass
#this script shows how to get user input

print "What is your name?"
name = raw_input()
#user can see what they're typing

color = getpass ('What is your favorite color? ')
#user input can't see what they're typing

print "Hi", name
print "Your favorite color is", color
