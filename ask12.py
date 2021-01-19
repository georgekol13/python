f = open("asciifile.txt", "r")
Lines = f.readlines() 
  
count = 0
# Strips the newline character 
for index,line in enumerate(Lines): 
	line = line.strip()
	listLine = list(line)
	
	newLine = []
	for char in listLine:
		newAscii = 255-ord(char)
		newChar = chr(newAscii)
		newLine.append(newChar)
	
	rotated = [x for x in newLine[::-1]]
	print(f"Line {index+1}:")
	print(listLine,rotated) #Auti i grammi uparxei gia na deiksei oti gurnaei ton xaraktira se katoptriko kai antistrefetai i lista, alla den ektuponetai sosta sto cmd
	print(f'The text {line} was changed to {"".join(rotated)}\n')
