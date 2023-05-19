
f1 = 1240000000
f2 = 1255000000
f3 = 1305000000
f4 = 1388000000
f5 = 1505000000
f6 = 1815000000
f7 = 1840000000
f8 = 1855000000

step12 = 150000000

f = f1
step = step12
ArrayIndex = 0

def sweeper(prob_lvl):

	global f1,f2,f3,f4,f5,f6,f7,f8,f,ArrayIndex,step12,step

	if prob_lvl:
		f += step
		ArrayIndex =ArrayIndex + 1
		
	if ArrayIndex == 1: 
		f = f2
		
	if ArrayIndex == 2: 
		f = f3
		
	if ArrayIndex == 3: 
		f = f4
			
	if ArrayIndex == 4: 
		f = f5
		
	if ArrayIndex == 5: 
		f = f6
		
	if ArrayIndex == 6: 
		f = f7
		
	if ArrayIndex == 7: 
		f = f8
		
	if f > f8 :
		f = f8
#		f = f1
#		step = step12
#		ArrayIndex =0
		
	return f


