import random

def overnesseval(over):
    if over == 1:
         over = random.randint(83,95)
    elif over == 2:
         over = random.randint(65,80)
    elif over == 3:
         over = random.randint(40,60)
    return over

def determinerating(w1ov,w2ov):
    matchra = w1ov + w2ov - random.randint(85, 110)
    matchra += random.randint(8,17) 
    return matchra

def promos(w1, w2):
    rnd = random.randint(1,4)
    
    if rnd == 1:
        matchre = w1 + " insulted and intimidated " + w2 + " to hype up their next match.\n"
    elif rnd == 2:
        matchre = w1 + " attacked " + w2 + " backstage!\n"
    elif rnd == 3:
        matchre = w1 +" attacked " + w2 + " during their promo!\n"
    elif rnd == 4:
        matchre = "The locker room had to come to the ring to break up a brawl after " +w1 + " beat down " +w2 +"!\n"

    return matchre

def ratingtograde(matchra):
    grade = ""
    if matchra < 60:
        grade = "F"
    elif matchra >= 60 and matchra < 68:
        grade = "D"
    elif matchra == 68 or matchra == 69:
        grade = "D+"
    elif matchra >= 70 and matchra < 78:
        grade = "C"
    elif matchra == 78 or matchra == 79:
        grade = "C+"
    elif matchra >= 80 and matchra < 88:
        grade = "B"
    elif matchra == 88 or matchra == 89:
        grade = "B+"
    elif matchra >= 90 and matchra < 98:
        grade = "A"
    elif matchra >= 98:
        grade = "A+"

    return grade

print("Welcome to PyWRBS the free wrestling event booking simulator")
matches = int(input("Enter the amount of matches/segments in the event: "))
fed = input("Enter the name or abbv. of the wrestling federation hosting the event: ")
eventna = input("Now enter the event's name: ")

i = 1
results = []
ratings = []
finalrating = 0

while i <= matches:
    print ("\nSegment " +str(i) +" of " +fed +" " +eventna);
    print("Choose a match/segment type\n1:1v1 Match\n2:2v2 Match\n3:Promo Segment")
    matchty = int(input())

    if matchty == 1:
        print("1v1 Singles Match")
        wrestler1 = input("Enter the name of the first wrestler: ")
        wrestler2 = input("Enter the name of the second wrestler: ")
        w1ov = int(input("Choose an option to represent " +wrestler1 +"'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber\n"))
        w2ov = int(input("Choose an option to represent " +wrestler2 +"'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber\n"))
        w1ov = overnesseval(w1ov)
        w2ov = overnesseval(w2ov)
        titleop = input("If this is a title match enter the title's name, if not type a lowercase n: ")
        winner = int(input("Choose a winner for the match:\n1:" +wrestler1+ "\n2:" +wrestler2+"\n"))
        if winner == 1:
            matchre = wrestler1 + " defeated " + wrestler2 + " in a match by pinfall.\n"
            if titleop !="n":
                matchre+= "The match was for the " + titleop +".\n"
        elif winner == 2:
            matchre = wrestler2 + " defeated " + wrestler1 + " in a match by pinfall.\n"
            if titleop !="n":
                matchre+= "The match was for the " + titleop +".\n"
        matchra = determinerating(w1ov,w2ov)
        segmentgrade = ratingtograde(matchra)
        matchre += "\nSegment Rating: " + segmentgrade
        results.append(matchre)
        ratings.append(matchra)        
        print(matchre)        
    elif matchty == 2:
        print("2v2 Tag Team Match")
        team1 = input("Enter the name of the first team: ")
        team2 = input("Enter the name of the second team: ")
        t1ov = int(input("Choose an option to represent " +team1 +"'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber\n"))
        t2ov = int(input("Choose an option to represent " +team2 +"'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber\n"))
        t1ov = overnesseval(t1ov)
        t2ov = overnesseval(t2ov)
        titleop = input("If this is a title match enter the title's name, if not type a lowercase n: ")
        winner = int(input("Choose a winner for the match:\n1:" +team1 + "\n2:" +team2+"\n"))
        if winner == 1:
            matchre = team1 + " defeated " + team2 + " in a match by pinfall.\n"
            if titleop !="n":
                matchre+= "The match was for the " + titleop +".\n"
        elif winner == 2:
            matchre = team2 + " defeated " + team1 + " in a match by pinfall.\n"
            if titleop !="n":
                matchre+= "The match was for the " + titleop +".\n"
        matchra = determinerating(t1ov,t2ov)
        segmentgrade = ratingtograde(matchra)
        matchre += "\nSegment Rating: " + segmentgrade
        results.append(matchre)
        ratings.append(matchra)
        print(matchre)

    elif matchty == 3:
        print("Promo/Interview Segment")
        wrestler1 = input("Enter the name of the first wrestler or team: ")
        wrestler2 = input("Enter the name of the second wrestler or team: ")
        w1ov = int(input("Choose an option to represent " +wrestler1 +"'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber\n"))
        w2ov = int(input("Choose an option to represent " +wrestler2 +"'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber\n"))
        w1ov = overnesseval(w1ov)
        w2ov = overnesseval(w2ov)
        winner = int(input("Choose a winner for the promo:\n1:" +wrestler1+ "\n2:" +wrestler2+"\n"))
        if winner == 1:
            matchre = promos(wrestler1,wrestler2)
        elif winner == 2:
            matchre = promos(wrestler2,wrestler1)
        matchra = determinerating(w1ov,w2ov)
        segmentgrade = ratingtograde(matchra)
        matchre += "\nSegment Rating: " + segmentgrade
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
finalgrade = ratingtograde(finalrating)
print("The final rating for " +fed +" " +eventna + " is: " +finalgrade)
