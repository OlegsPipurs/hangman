import time

print ("Start time")
start_time = time.time()
print(start_time)
stoppet = input ("Press enter to stop")
end_time = time.time()
print ("You have finished")
print(end_time)
print("----------------")
speles_laiks = int(end_time - start_time)
print("xxx" , speles_laiks)
