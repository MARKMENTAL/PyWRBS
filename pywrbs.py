import random

print("Welcome to PyWRBS the free wrestling event booking simulator")
matches = int(input("Enter the amount of matches in the event:"))
fed = input("Enter the name or abbv. of the wrestling federation hosting the event:")
eventna = input("Now enter the event's name:")

i = 1
results = []
ratings = []
finalrating = 0
titlebonus = 0

while i <= matches:
	print ("Match " +str(i) +" of " +fed +" " +eventna);
	print("Choose a match type\n1:1v1\n2:2v2")
	matchty = int(input())
	
	if matchty == 1:
		print("1v1 Singles Match")
		wrestler1 = input("Enter the name of the first wrestler:")
		wrestler2 = input("Enter the name of the second wrestler:")
		w1ov = int(input("Enter a number representing wrestler 1's overness on a scale of 100:"))
		w2ov = int(input("Enter a number representing wrestler 2's overness on a scale of 100:"))
		titleop = input("If this is a title match enter the title's name, if not type a lowercase n: ")
		winner = int(input("Choose a winner for the match:\n1:" +wrestler1+ "\n2:" +wrestler2+"\n"))
		if winner == 1:
			matchre = wrestler1 + " defeated " + wrestler2 + " by pinfall."
			if titleop !="n":
				matchre+= "For the " + titleop +"."
				titlebonus = 10
		elif winner == 2:
			matchre = wrestler2 + " defeated " + wrestler1 + " by pinfall."
			if titleop !="n":
				matchre+= "For the " + titleop +"."
				titlebonus = 10	
		matchra = w1ov + w2ov - random.randint(85, 110)
		matchra += random.randint(8,17) 
		matchra += titlebonus
		matchre += "\nMatch Rating: " + str(matchra)
		results.append(matchre)
		ratings.append(matchra)		
		print(matchre)		
	elif matchty == 2:
		print("2v2 Tag Team Match")
		team1 = input("Enter the name of the first team:")
		team2 = input("Enter the name of the second team:")
		t1ov = int(input("Enter a number representing team 1's overness on a scale of 100:"))
		t2ov = int(input("Enter a number representing team 1's overness on a scale of 100:"))
		titleop = input("If this is a title match enter the title's name, if not type a lowercase n: ")
		winner = int(input("Choose a winner for the match:\n1:" +team1 + "\n2:" +team2+"\n"))
		if winner == 1:
			matchre = team1 + " defeated " + team2 + " by pinfall."
			if titleop !="n":
				matchre+= "For the " + titleop +"."
				titlebonus = 10
		elif winner == 2:
			matchre = team2 + " defeated " + team1 + " by pinfall."
			if titleop !="n":
				matchre+= "For the " + titleop +"."
				titlebonus = 10	
		matchra = t1ov + t2ov - random.randint(85, 110)
		matchra += random.randint(8 ,17) 
		matchra += titlebonus
		matchre += "\nMatch Rating: " + str(matchra)
		results.append(matchre)
		ratings.append(matchra)			
		print(matchre)		
		
	i+=1
	
i = 1
print("************************************\n"+fed+" " +eventna+" RESULTS\n************************************\n")	
for result in results:
	print("Match " +str(i) + " Result:\n" +result +"\n")
	i+=1

for rating in ratings:
	finalrating+=rating

finalrating = int(finalrating / matches)
print("The final rating for " +fed +" " +eventna + " is: " +str(finalrating))	

