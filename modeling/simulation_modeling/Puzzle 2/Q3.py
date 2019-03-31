import random

arrive = 0  #time from start of clock at t=0 when ship i arrives the harbor for unloading
start = 0  #time from start of clock at which shipp i commences its unloading
idle  = 0  #time for which dock facilities are idle immediately before commencement of unloading ship i
wait  = 0 #time ship i waits in the harbor after arrival before unloading commences
finish  = 0 #time from start of clock at which service for ship i is completed at the unloading facilities
harbor = 0#total time ship is spends in the harbor.

HARTIME = 0#average time per ship in the harbor
MAXHAR  = 0#maximum time of a ship in the harbor

WAITTIME = 0 #Average waiting time per ship before unloading
MAXWAIT = 0   #Maximum waiting time of a ship

IDLETIME = 0   #Percentage of total simulatime time unloading facilities are idle

n = 1000    #1000 ships for the simulation

unload_bound_a = 45
unload_bound_b = 90
between_bound_a = 10
between_bound_b = 120

unload  = random.uniform(unload_bound_a, unload_bound_b)#time required to unload ship i at the dock (Random integer)
between = random.uniform(between_bound_a, between_bound_b)

arrive = between

HARTIME = unload
MAXHAR = unload
IDLETIME = arrive

finish = arrive + unload

for i in range(n - 1):
    between = random.uniform(between_bound_a, between_bound_b)
    unload = random.uniform(unload_bound_a, unload_bound_b)

    arrive = arrive + between   #arrive_i = arrive_(i-1) + between_i
    timediff = arrive - finish  #timediff = arrive_i - finish_(i-1)
    
    if (timediff >= 0):
        idle = timediff
        wait = 0
    else:
        wait = -timediff
        idle = 0
    
    start = arrive + wait  #start_i = arrive_i + wait_i
    finish = start + unload #finish_i = start_i + unload_i
    harbor = wait + unload  #harbor_i = wait_i + unload_i

    HARTIME += harbor   #sum harbor_i into HARTIME for averaging

    if harbor > MAXHAR:
        MAXHAR = harbor
    
    WAITTIME += wait    #sum wait_i into WAITIME for averaging
    IDLETIME += idle

    if wait > MAXWAIT:
        MAXWAIT = wait

HARTIME = HARTIME / n
WAITTIME = WAITTIME / n
IDLETIME = IDLETIME / finish

print('HARTIME:', HARTIME, 'MAXHAR', MAXHAR,
     'WAITIME', WAITTIME, 'MAXWAIT', MAXWAIT, 
     'percentage of IDLETIME', IDLETIME)
