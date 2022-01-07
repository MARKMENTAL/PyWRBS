import random

print("Welcome to PyWRBS the free wrestling event booking simulator")
matches = int(input("Enter the amount of matches/segments in the event: "))
fed = input("Enter the name or abbv. of the wrestling federation hosting the event: ")
eventna = input("Now enter the event's name: ")

i = 1
results = []
ratings = []
finalrating = 0
titlebonus = 0

while i <= matches:
    print ("\nSegment " +str(i) +" of " +fed +" " +eventna);
    print("Choose a match/segment type\n1:1v1 Match\n2:2v2 Match\n3:Promo Segment")
    matchty = int(input())

    if matchty == 1:
        print("1v1 Singles Match")
        wrestler1 = input("Enter the name of the first wrestler: ")
        wrestler2 = input("Enter the name of the second wrestler: ")
        w1ov = int(input("Enter a number representing " +wrestler1 +"'s overness on a scale of 100: "))
        w2ov = int(input("Enter a number representing " +wrestler2 +"'s overness on a scale of 100: "))
        titleop = input("If this is a title match enter the title's name, if not type a lowercase n: ")
        winner = int(input("Choose a winner for the match:\n1:" +wrestler1+ "\n2:" +wrestler2+"\n"))
        if winner == 1:
            matchre = wrestler1 + " defeated " + wrestler2 + " in a match by pinfall.\n"
            if titleop !="n":
                matchre+= "The match was for the " + titleop +".\n"
                titlebonus = 10
        elif winner == 2:
            matchre = wrestler2 + " defeated " + wrestler1 + " in a match by pinfall.\n"
            if titleop !="n":
                matchre+= "The match was for the " + titleop +".\n"
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
        team1 = input("Enter the name of the first team: ")
        team2 = input("Enter the name of the second team: ")
        t1ov = int(input("Enter a number representing " +team1 +"'s overness on a scale of 100: "))
        t2ov = int(input("Enter a number representing " +team2 +"'s overness on a scale of 100: "))
        titleop = input("If this is a title match enter the title's name, if not type a lowercase n: ")
        winner = int(input("Choose a winner for the match:\n1:" +team1 + "\n2:" +team2+"\n"))
        if winner == 1:
            matchre = team1 + " defeated " + team2 + " in a match by pinfall.\n"
            if titleop !="n":
                matchre+= "The match was for the " + titleop +".\n"
                titlebonus = 10
        elif winner == 2:
            matchre = team2 + " defeated " + team1 + " in a match by pinfall.\n"
            if titleop !="n":
                matchre+= "The match was for the " + titleop +".\n"
                titlebonus = 10
        matchra = t1ov + t2ov - random.randint(85, 110)
        matchra += random.randint(8 ,17) 
        matchra += titlebonus
        matchre += "\nMatch Rating: " + str(matchra)
        results.append(matchre)
        ratings.append(matchra)
        print(matchre)

    elif matchty == 3:
        print("Promo/Interview Segment")
        wrestler1 = input("Enter the name of the first wrestler or team, they will be on the attacking side of this promo: ")
        wrestler2 = input("Enter the name of the second wrestler or team, they will be on the defending side of this promo: ")
        w1ov = int(input("Enter a number representing " +wrestler1 +"'s microphone skills on a scale of 100: "))
        w2ov = int(input("Enter a number representing " +wrestler2 +"'s microphone skills on a scale of 100: "))
        winner = int(input("Choose a winner for the promo:\n1:" +wrestler1+ "\n2:" +wrestler2+"\n"))
        if winner == 1:
            matchre = wrestler1 + " insulted and intimidated " + wrestler2 + " to hype up their next match.\n"
        elif winner == 2:
            matchre = wrestler2 + " came out to ambush and attack " + wrestler1 + ", ruining their promo.\n"
        matchra = w1ov + w2ov - random.randint(85, 110)
        matchra += random.randint(8,17) 
        matchre += "\nSegment Rating: " + str(matchra)
        results.append(matchre)
        ratings.append(matchra)
        print(matchre)
    i+=1
    
i = 1
print("\n************************************\n"+fed+" " +eventna+" RESULTS\n************************************\n")    
for result in results:
    print("Segment " +str(i) + " Result:\n" +result +"\n")
    i+=1

for rating in ratings:
    finalrating+=rating

finalrating = int(finalrating / matches)
print("The final rating for " +fed +" " +eventna + " is: " +str(finalrating))    
