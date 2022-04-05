import random

def writeresults(fed, eventna, finalgrade, results):
    filename = input("Enter a name for a text file to save these results into (omit the .txt extension)\n")
    resultfile = open(filename + ".txt","a")
    resultfile.write("\n************************************\n"+fed+" " +eventna+" RESULTS\n************************************\n") 
    i = 1

    for result in results:                                                                                                   
        resultfile.write("\nSegment " +str(i) + " Result:\n" +result +"\n")
        i+=1

    resultfile.write("\nThe final rating for " +fed +" " +eventna + " is: " +finalgrade + "\n")
    print("The file '" + filename + ".txt'" + " has been saved to successfully.")

def getwinmethod(wm):
    if wm == 1:
        winmethod = "pinfall"
    elif wm == 2:
        winmethod = "submission"
    elif wm == 3:
        winmethod = "knockout"
    return winmethod

def tvratings(eventna,fed):
    rawstring = "raw"
    smackstring = "smackdown"
    rampagestring = "rampage"
    dynamitestring = "dynamite"
    darkstring = "dark"
    nitrostring = "nitro"

    if rawstring in eventna.lower() and fed.lower() == "wwe":
        viewers = random.randint(1500000,3000000)
        # using f strings to format the viewer number with commas
        print("\nUSA Network TV Viewers: " +f'{viewers:,}')
    
    elif smackstring in eventna.lower() and fed.lower() == "wwe":
        viewers = random.randint(1000000,2800000)
        print("\nFOX TV Viewers: "+f'{viewers:,}')

    elif rampagestring in eventna.lower() and fed.lower() == "aew" or fed.lower() == "wcw" and nitrostring in eventna.lower():
        viewers = random.randint(430000,1100000)  
        print("\nTNT TV Viewers: "+f'{viewers:,}')

    elif dynamitestring in eventna.lower() and fed.lower() == "aew":
        viewers = random.randint(500000,1400000)
        print("\nTBS TV Viewers: "+f'{viewers:,}')

    elif darkstring in eventna.lower() and fed.lower() == "aew":
        viewers = random.randint(300000, 1800000)
        print("\nYouTube Viewers: "+f'{viewers:,}')

    else:
        viewers = random.randint(1000,20000)
        print("\nLive Event Attendance: " +f'{viewers:,}')

def overnesseval(over, wrestler,matchty):
    if over == 1:
        over = random.randint(80,87)
    elif over == 2:
        over = random.randint(65,78)
    elif over == 3:
        over = random.randint(60,70)
    if matchty == 1 or matchty == 2:
        skillbonus = int(input("Choose an option to represent " +wrestler +"'s technical wrestling skill:\n1:Technical Expert\n2:Solid Ring Worker\n3:Garbage\n"))
    elif matchty == 3:
        skillbonus = int(input("Choose an option to represent " +wrestler +"'s microphone/acting skill:\n1:Charismatic Expert\n2:Solid Actor\n3:Garbage on the mic\n"))
    if skillbonus == 1:
        over+=random.randint(5,10)
    elif skillbonus == 2:
        over+=random.randint(3, 8)
    elif skillbonus == 3:
        over+=random.randint(1,5)
    return over

def determinerating(w1ov,w2ov):
    matchra = w1ov + w2ov - random.randint(80, 100)
    return matchra

def promos(w1, w2):
    rnd = int(input("Choose a promo\n1:In-Ring Promo\n2:Backstage Attack\n3:Promo Attack\n4:Impromptu Brawl\n5:Custom Promo\n"))
    
    if rnd == 1:
        matchre = w1 + " insulted and intimidated " + w2 + " to hype up their next match.\n"
    elif rnd == 2:
        matchre = w1 + " attacked " + w2 + " backstage!\n"
    elif rnd == 3:
        matchre = w1 +" attacked " + w2 + " during their promo!\n"
    elif rnd == 4:
        matchre = "The locker room had to come to the ring to break up a brawl after " +w1 + " beat down " +w2 +"!\n"
    elif rnd == 5:
        matchre = input("Custom promo! Type up a custom promo for " +w1 + " and " +w2 +":\n")
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

try:
    print("Welcome to PyWRBS the free wrestling event booking simulator")
    matches = int(input("Enter the amount of matches/segments in the event: "))
    fed = input("Enter the abbreviation of the wrestling federation hosting the event: ")
    eventna = input("Now enter the event's name: ")

    i = 1
    results = []
    ratings = []
    finalrating = 0

    while i <= matches:
        print ("\nSegment " +str(i) +" of " +fed +" " +eventna);
        print("Choose a match/segment type\n1:Singles Match\n2:Tag Match\n3:Promo Segment")
        matchty = int(input())
        
        # normal match chosen
        if matchty == 1:
            print("Singles Match")
            wrestler1 = input("Enter the name of the first wrestler: ")
            wrestler2 = input("Enter the name of the second wrestler: ")
            w1ov = int(input("Choose an option to represent " +wrestler1 +"'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber\n"))
            w2ov = int(input("Choose an option to represent " +wrestler2 +"'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber\n"))
            w1ov = overnesseval(w1ov,wrestler1,matchty)
            w2ov = overnesseval(w2ov,wrestler2,matchty)
            titleop = input("If this is a title match enter the title's name, if not type a lowercase n: ")
            winner = int(input("Choose a winner for the match:\n1:" +wrestler1+ "\n2:" +wrestler2+"\n3:No Contest/DQ\n"))
            if winner == 1:
              winmethod = int(input("Choose a win method for the match:\n1:Pinfall\n2:Submission\n3:Knockout\n"))
              winmethod = getwinmethod(winmethod)
              matchre = wrestler1 + " defeated " + wrestler2 + " in a match by " +winmethod + ".\n"
              if titleop !="n":
                   matchre+= "Title: " + titleop +"\n"
            elif winner == 2:
              winmethod = int(input("Choose a win method for the match:\n1:Pinfall\n2:Submission\n3:Knockout\n"))
              winmethod = getwinmethod(winmethod)
              matchre = wrestler2 + " defeated " + wrestler1 + " in a match by " + winmethod + ".\n"
              if titleop !="n":
                   matchre+= "Title: " + titleop +"\n"
            elif winner == 3:
                matchre = "The match between " +wrestler1 + " and " +wrestler2 + " ended in a no contest/disqualification\n"

            matchre += "Match Time: " +matchtime()
            matchra = determinerating(w1ov,w2ov)
            segmentgrade = ratingtograde(matchra)
            matchre += "\nSegment Rating: " + segmentgrade
            results.append(matchre)
            ratings.append(matchra)        

        # tag match chosen
        elif matchty == 2:
            print("Tag Team Match")
            team1 = input("Enter the name of the first team: ")
            team2 = input("Enter the name of the second team: ")
            t1ov = int(input("Choose an option to represent " +team1 +"'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber\n"))
            t2ov = int(input("Choose an option to represent " +team2 +"'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber\n"))
            t1ov = overnesseval(t1ov,team1,matchty)
            t2ov = overnesseval(t2ov,team2,matchty)
            titleop = input("If this is a title match enter the title's name, if not type a lowercase n: ")
            winner = int(input("Choose a winner for the match:\n1:" +team1 + "\n2:" +team2+"\n3:No Contest/DQ\n"))
            if winner == 1:
                winmethod = int(input("Choose a win method for the match:\n1:Pinfall\n2:Submission\n3:Knockout\n"))
                winmethod = getwinmethod(winmethod)
                matchre = team1 + " defeated " + team2 + " in a match by " + winmethod + ".\n"
                if titleop !="n":
                    matchre+= "Title: " + titleop +"\n"
            elif winner == 2:
                winmethod = int(input("Choose a win method for the match:\n1: Pinfall\n2: Submission\n3: Knockout\n"))
                winmethod = getwinmethod(winmethod)
                matchre = team2 + " defeated " + team1 + " in a match by " + winmethod + ".\n"
                if titleop !="n":
                    matchre+= "Title: " + titleop +"\n"
            elif winner == 3:
                matchre = "The match between " +team1 + " and " +team2 + " ended in a no contest/disqualification\n"
            
            matchre += "Match Time: " +matchtime()
            matchra = determinerating(t1ov,t2ov)
            segmentgrade = ratingtograde(matchra)
            matchre += "\nSegment Rating: " + segmentgrade
            results.append(matchre)
            ratings.append(matchra)
        
        # promo/interview chosen
        elif matchty == 3:
            print("Promo/Interview Segment")
            wrestler1 = input("Enter the name of the first wrestler or team: ")
            wrestler2 = input("Enter the name of the second wrestler or team: ")
            w1ov = int(input("Choose an option to represent " +wrestler1 +"'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber\n"))
            w2ov = int(input("Choose an option to represent " +wrestler2 +"'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber\n"))
            w1ov = overnesseval(w1ov,wrestler1,matchty)
            w2ov = overnesseval(w2ov,wrestler2,matchty)
            matchre = promos(wrestler1,wrestler2)
            matchra = determinerating(w1ov,w2ov)
            segmentgrade = ratingtograde(matchra)
            matchre += "\nSegment Rating: " + segmentgrade
            results.append(matchre)
            ratings.append(matchra)

        # on invalid option, counter i is subtracted by 1, so after the reincrimentation of the counter, the user can try again with no negative consquence
        else:
            print("Invalid Selection, try again...")
            i-=1

        # increment i after match/segment
        i+=1
    
    # Show Results Start Here
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
    tvratings(eventna,fed)
    saveresults = input("Would you like to save the show results?(y/n)\n")

    if saveresults.lower() == "y":
        writeresults(fed, eventna, finalgrade, results)

except ValueError:
    print("An error occurred, invalid input...\nPyWRBS shutting down...")
except KeyboardInterrupt:
    print("\nPyWRBS shutting down...")
except ZeroDivisionError:
    print("\nYou scheduled 0 segments, so there was no show...\nPyWRBS shutting down...")
