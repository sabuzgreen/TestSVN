
f1 = 1240000000
f2 = 1255000000
f3 = 1305000000
f4 = 1388000000

step12 = 150000000

f = f1
step = step12
ArrayIndex = 0

def sweeper(prob_lvl):

	global f1,f2,f3,f4,f,ArrayIndex,step12,step

	if prob_lvl:
		f += step
		ArrayIndex =ArrayIndex + 1
		
	if ArrayIndex == 1: 
		f = f2
		
	if ArrayIndex == 2: 
		f = f3
		
	if ArrayIndex == 3: 
		f = f4
		
	if f > f4 :
#		f = f4
		f = f1
		step = step12
		ArrayIndex =0
		
	return f


