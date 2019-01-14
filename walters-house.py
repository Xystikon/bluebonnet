import sys
from time import sleep
import random

def init():

        n=0
        ne=0
        e=0
        se=0
        s=0
        sw=0
        w=0
        nw=0
        
        bedroom=1
        hallway=1
        bathroom=1
        room=1
        stairtop=1
        couch=1
        
        stairbottom=1
        dineroom=1
        office=1
        kitchen=1
        liveroom=1
        hallway2=1
        door=1
        
        l=0
        
        currentloc = "bedroom"
        print("I wake up in a bed, cold and hard. I sit up and walk to the middle of the room.")

        start()

def start():
        print("")
	
	if currentloc == "bedroom":
		n="window"
		nw="wall"
		e="wall"
		se="wall"
		s="wall"
		sw="wall"
		w="hallway"
		nw="wall"
		
		print("Bedroom\n")
		if bedroom == 1 or l == 1:
			print("There are two beds in the room, one of which I woke up in. To the north of me is a window that is boarded up, and there is a single exit through a door to the west.")
			bedroom = 0
			l=0
	
	elif currentloc == "hallway":
		n="bathroom1"
		ne="wall"
		e="bedroom"
		se="stairtop"
		s="wall"
		sw="wall"
		w="room"
		nw="couch"
		
		print("Hallway\n")
		if hallway == 1 or l == 1:
			print("I am in a hallway leading from east and west. A picture of an unknown family is north of me, and is mostly covered in moss. A doorway to a bedroom is east of me, and to the north is a closed door.")
			hallway = 0
			l=0
	
	elif currentloc == "bathroom1":
		n="sink"
		ne="wall"
		e="toilet"
		se="wall"
		s="hallway"
		sw="wall"
		w="wall"
		nw="wall"
		
		print("Bathroom\n")
		if bathroom == 1 or l == 1:
			print("I am now in a bathroom, with a sink north of me and a toilet east of me. I can exit the bathroom south.")
			bathroom = 0
			l=0

	elif currentloc == "room":
		n="couch"
		ne="wall"
		e="hallway"
		se="wall"
		s="stairtop"
		sw="stairtop"
		w="wall"
		nw="wall"
	
		print("Room\n")
		if room == 1 or l == 1:
			print("The hallway to the west opens up into a small room, in which there is a couch north. Going west is prevented due to a barred door. To the south is the top of a staircase leading down into the darkness.")
			room = 0
			l=0
	
	elif currentloc == "couch":
		n="wall"
		ne="wall"
		e="wall"
		se="wall"
		s="room"
		sw="hallway"
		w="wall"
		nw="wall"
		
		print("Other Side of the Room\n")
		if couch == 1 or l == 1:
			print("I am now on the other side of the room, a couch east of me. A smashed out tv in to my west. The other side of the room is south of me.")
			couch = 0
			l=0
			
	elif currentloc == "stairtop":
		n="room"
		ne="wall"
		e="stairbottom"
		se="wall"
		s="window"
		sw="wall"
		w="wall"
		nw="hallway"
		
		print("The Top of a Staircase\n")
		if stairtop == 1 or l == 1:
			print("I am at the top of a staircase, leading into darkness. To the north goes back to the room opening, and to the east is the staircase.")
			stairtop = 0
			l=0
					
	elif currentloc == "stairbottom":
		n="door"
		ne="dineroom"
		e="kitchen"
		se="wall"
		s="liveroom"
		sw="liveroom"
		w="stairtop"
		nw="wall"
		
		print("The Bottom of a Staircase\n")
		if stairbottom == 1 or l == 1:
			print("I am at the bottom of a staircase, leading upwards to the west. A door is infront of me, and a dining room is northwest. A kitchen is towards the east and a living room is south of me.")
			stairbottom = 0
			l=0
			
	elif currentloc == "door":
		n="outside"
		ne="wall"
		e="wall"
		se="wall"
		s="stairbottom"
		sw="wall"
		w="wall"
		nw="wall"
		
		print("The Door\n")		
		if door == 1 or l == 1:
			print("I come to a stop at a door, slightly ajar. To the south goes backwards to the staircase.")
			door = 0
			l=0
			
	elif currentloc == "dineroom":
		n="window"
		ne="wall"
		e="office"
		se="bathroom2"
		s="wall"
		sw="stairbottom"
		w="wall"
		nw="wall"
		
		print("A Dining Room\n")
		
		if dineroom == 1 or l == 1:
			print("I am now in a dining room, with books, papaers, and foreign machinery scattered around the table. A clouded window is north of me, an office is east of me, and a bathroom is southeast of me. To the southwest is the bottom of the stairs.")
			dineroom = 0
			l=0
			
	elif currentloc == "kitchen":
		n="balcony"
		ne="wall"
		e="stairbottom"
		se="wall"
		s="wall"
		sw="wall"
		w="stairbottom"
		nw="wall"
		
		print("Kitchen\n")		
		if kitchen == 1 or l == 1:
			print("I am in a kithcen, a balcony north of me. I can go back to the bottom of the stairs by walking west.")
			kitchen = 0
			l=0


        action = input('\n')
        move(action)

def move(act):
        
        if action == "n":
		currentloc = n
        elif action == "ne":
                currentloc = ne
	elif action == "e":
		currentloc = e
        elif action == "se":
                currentloc = se
	elif action == "s":
		currentloc = s
        elif action == "sw":
                currentloc = sw
	elif action == "w":
		currentloc = w
        elif action == "nw":
                currentloc = nw

        elif action == "l":
                l = 1
		
	if e == "wall" and currentloc == e or s == "wall" and currentloc == s or w == "wall" and currentloc == w or n == "wall" and currentloc == n:
		wallr = random.randint(0, 2)
	
		if wallr == 0:
			print("A wall blocks my way.")
		elif wallr == 1:
			print("A wall confronts me.")
		elif wallr == 2:
			print("A wall, overgrown and peeling prevents me from going in that direction.")
			
	elif e == "window" and currentloc == e or s == "window" and currentloc == s or w == "window" and currentloc == w or n == "window" and currentloc == n:
		windowr = random.randint(0,2)
		
		if windowr == 0:
			print("A coulded window blocks my way.")
		if windowr == 1:
			print("I can't get past this window.")
		if windowr == 2:
			print("I can't get past this window. Or see out of it.")

        
