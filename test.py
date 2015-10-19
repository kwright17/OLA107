# OLA107 BY kres wright,  CSCI 1170-009, Due: 10/16/15
# PROGRAM ID:  OLA107 / The Classroom Capacity Problem
# AUTHOR:  kres wright
# INSTALLATION:  MTSU
# REMARKS:  This proram reads and processes data until a sentinel
# value is reached. The first number in a set is the room number, 
# the second is the rooms' capacity, and the thrid is the size of 
# the class scheduled to meet in that room. This program outputs
# the room number, capacity, number of seats filled, seats available
# and a message 'FULL' or 'OPEN'


import sys     # needed to make input statement work
def main():
    count = 0
    overall_cap = 0
    tot_enroll = 0
    rem_rooms = 0

    # Priming read: room,capacity,size integer triplets from standard input
    room,capacity,size = map(int,sys.stdin.readline().split())
    
    #get determine if rooms empty or not
    def vacancy(data1, data2):
        if data1 -data2 > 0:
           return True
        else:
            return False
    #determine if seats remain
    def empty_seats():
        if vacancy(capacity,size) == True:
            return (capacity - size)
        else:
            return 0
    #determine class status
    def status():
        if vacancy(capacity,size) == True:
           
            return 'OPEN'
           
        else:
            return 'FULL'
        
    # Process triplets until EOF-sentinel encountered
    print ('Room', "Capacity", 'Size', 'Empty Seats', 'Status', sep = '  ')
    while room>=0:
        print(format(room,'>4d'),format(capacity,'>6d'), format(size,'>4d'), format(empty_seats(),'>4d'),'    '+status(),sep='\t')
        #...or, instead of just printing these values, do something with them.
        
        if status() == 'OPEN':
            rem_rooms += 1
        count += 1
        #SUMMARY
        overall_cap += capacity
        tot_enroll += size


        # Recurring read: room,capacity,size
        room,capacity,size = map(int,sys.stdin.readline().split())
    print('*'*41)   
    print('Rooms:', count)
    print ('Overall Capacity:', overall_cap)
    print('Total Enrollment:', tot_enroll)
    print('Number of Open Rooms Remaining:', rem_rooms)
    print('*'*41)
# Main
main()