# - *-  coding: utf- 8 - *-
def get_S7_area(varname):
	"""
	 set S7 area from variable name (string)
	 returns area as int
	"""
	#######################################
	# get area
	#######################################
	# flags
	if(varname[0].lower()=='f') or (varname[0].lower()=='m'):
		# flags
		vararea=0x83
	# outputs
	elif(varname[0].lower()=='q') or (varname[0].lower()=='a'):
		# outputs
		vararea=0x82

	# inputs
	elif(varname[0].lower()=='i') or (varname[0].lower()=='e'):
		# inputs
		vararea=0x81

	# timer
	elif(varname[0].lower()=='t'):
		# timer
		vararea=0x1D

	# counter
	elif(varname[0].lower()=='z') or (varname[0].lower()=='c'):
		# counter
		vararea=0x1C
		
	# data block
	elif(varname[0].lower()=='d'):
		# data block
		vararea=0x84
		
	return vararea

def get_data_item(area, mem, name, delimiter):
	# if data block
	if area==0x84:

		# data block
		# format DBn.DXn.x if only a bit (x is 0..7)
		# or DBn.DYn
		# where n is a whole number (pay attention to address ranges of PLC)
		# where y is B for BYTE
		#            W for WORD (integer)
		#            D for DOUBLE WORD integer
		#  			 F for DOUBLE WORD float (real)
		
		# split data address into DB and operand
		parts = mem.split('.')
		# omit DB, get number
		dbnum = int(parts[0][2:])
		# get operand 
		memformat =  parts[1][1]
		
		#######################################
		# get format
		#######################################

		# get address for data bit
		if(memformat.lower()=='x'): #bit
			# only one byte
			length=1
			# format bool
			# byte address
			start = int(parts[1][2:])				
			format = '>B'
			# split name for bit name
			bitname = name.split(',')
			hdr =""
			for i in range(0,len(bitname)):
				if bitname[i] != "":
					hdr = hdr + bitname[i].upper() + delimiter
		
		# get address for data byte
		if(memformat.lower()=='b'): #byte
			length=1
			start = int(parts[1][2:])
			format = '>b'
			hdr = name + delimiter
			
		# get address for data word
		if(memformat.lower()=='w'): #word
			length=2
			start = int(parts[1][2:])
			format = '>h'
			hdr = name + delimiter
			
		# get address for data dword
		if(memformat.lower()=='d'):
			length=4
			start = int(parts[1][2:])
			format = '>i'
			hdr = name + delimiter

		# get address for data dword (real)
		if(memformat.lower()=='f'): #double word (real numbers)
			length=4
			start = int(parts[1][2:])
			format = '>f'
			hdr = name + delimiter
			
	else:
		# get address for other bits (I,O,F,T,C)
		memformat =  mem[1]
		# this time dbnum is 0
		dbnum = 0

		#######################################
		# get format
		#######################################
		
		if(memformat.lower()=='x'): #bit
			length=1
			start = int(mem.split('.')[0][2:])
			format = '>B'
			# split name for bit name
			bitname = name.split(',')
			hdr =""
			for i in range(0,len(bitname)):
				if bitname[i] != "":
					hdr = hdr + bitname[i].upper() + delimiter
			
		if(memformat.lower()=='b'): #byte
			length=1
			start = int(mem[2:])
			format = '>b'
			hdr = name + delimiter
			
		if(memformat.lower()=='w'): #word
			length=2
			start = int(mem[2:])	
			format = '>h'
			hdr = name + delimiter
			
		if(memformat.lower()=='d'):
			length=4
			start = int(mem.split('.')[0][2:])
			format = '>i'
			hdr = name + delimiter

		if(memformat.lower()=='f'): #double word (real numbers)
			length=4
			start = int(mem.split('.')[0][2:])
			format = '>f'
			hdr = name + delimiter

	return dbnum, length, start, format, hdr