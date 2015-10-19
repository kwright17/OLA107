
#overall capacaty = 
#total enrollment
#number of open rooms
# triplets BY author name,  CSCI 1170-sec, Due: mm/dd/yy
# PROGRAM ID:  triplets.py / Example of reading multiple numbers per line
# AUTHOR:  author name
# INSTALLATION:  MTSU
# REMARKS:  This program illustrates a way to read three integer numbers
# together that appear on the same (stdin) input line.  The program is
# terminated by a sentinel triplet where the first triplet value is negative.

import sys     # needed to make input statement work

def main():
    count = 0

    # Priming read: room,capacity,size integer triplets from standard input
    room,capacity,size = map(int,sys.stdin.readline().split())

    # Process triplets until EOF-sentinel encountered
    while room>=0:
        print("room=",room," capacity=",capacity, " size=",size)
        #...or, instead of just printing these values, do something with them.
        count += 1

        # Recurring read: room,capacity,size
        room,capacity,size = map(int,sys.stdin.readline().split())

    print(count, "input triplets read")


# Main
main()
