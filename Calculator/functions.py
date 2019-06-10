expression = "" 


def press(num): 
	global expression 
	
	expression = expression + str(num) 

	equation.set(expression) 


def equalpress(): 
	try: 

		global expression
		total = str(eval(expression)) 

		equation.set(total) 
		
		expression = "" 

	except: 

		equation.set(" error ") 
		expression = "" 


def clear(): 
	global expression 
	expression = "" 
	equation.set("") 