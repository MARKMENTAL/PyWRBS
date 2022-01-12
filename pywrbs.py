import random

def overnesseval(over, wrestler):
    if over == 1:
         over = random.randint(80,90)
    elif over == 2:
         over = random.randint(65,78)
    elif over == 3:
         over = random.randint(50,60)
    skillbonus = int(input("Choose an option to represent " +wrestler +"'s technical wrestling skill:\n1:Technical Expert\n2:Solid Ring Worker\n3:Garbage\n"))
    if skillbonus == 1:
         over+=random.randint(10,20)
    elif skillbonus == 2:
         over+=random.randint(5,20)
    elif skillbonus == 3:
        over+=random.randint(1,10)
    return over

def determinerating(w1ov,w2ov):
    matchra = w1ov + w2ov - random.randint(80, 100)
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

def matchtime():
    mins = random.randint(0, 30)
    secs = random.randint(0, 59)
    # zerostr is created so a zero can be added to pad second values
    # under 10 for clearer readability
    zerostr = str(secs)
    if secs < 10:
        zerostr = "0" +str(secs)
    
    if secs == 0 and mins == 0:
        secs = 30

    timestr = str(mins) + ":" + zerostr
    return timestr

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
        w1ov = overnesseval(w1ov,wrestler1)
        w2ov = overnesseval(w2ov,wrestler2)
        titleop = input("If this is a title match enter the title's name, if not type a lowercase n: ")
        winner = int(input("Choose a winner for the match:\n1:" +wrestler1+ "\n2:" +wrestler2+"\n"))
        if winner == 1:
            matchre = wrestler1 + " defeated " + wrestler2 + " in a match by pinfall.\n"
            if titleop !="n":
                matchre+= "Title: " + titleop +"\n"
        elif winner == 2:
            matchre = wrestler2 + " defeated " + wrestler1 + " in a match by pinfall.\n"
            if titleop !="n":
                matchre+= "Title: " + titleop +"\n"

        matchre += "Match Time: " +matchtime()
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
        t1ov = overnesseval(t1ov,team1)
        t2ov = overnesseval(t2ov,team2)
        titleop = input("If this is a title match enter the title's name, if not type a lowercase n: ")
        winner = int(input("Choose a winner for the match:\n1:" +team1 + "\n2:" +team2+"\n"))
        if winner == 1:
            matchre = team1 + " defeated " + team2 + " in a match by pinfall.\n"
            if titleop !="n":
                matchre+= "Title: " + titleop +"\n"
        elif winner == 2:
            matchre = team2 + " defeated " + team1 + " in a match by pinfall.\n"
            if titleop !="n":
                matchre+= "Title: " + titleop +"\n"

        matchre += "Match Time: " +matchtime()
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
        w1ov = overnesseval(w1ov,wrestler1)
        w2ov = overnesseval(w2ov,wrestler2)
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
