using System;

class CSWRBS {
    static int OvernessEval(int over) {
        Random rnd = new Random();
        if (over == 1) {
            over = rnd.Next(83, 95);
        } else if (over == 2) {
            over = rnd.Next(65, 80);
        } else if (over == 3) {
            over = rnd.Next(40, 60);
        } else {
            // if invalid assume jobber rng
            rnd.Next(40, 60);
        }
        return over;
    }

    static int DetermineRating(int w1ov, int w2ov) {
        Random rnd = new Random();
        int matchra = w1ov + w2ov - rnd.Next(85, 110);
        matchra += rnd.Next(8, 17);
        return matchra;
    }

    static string Promos(string w1, string w2) {
        Random rnd = new Random();
        int rng = rnd.Next(1, 4);
        string matchre = "";
        if (rng == 1) {
            matchre = w1 + " insulted " + w2 + " in a promo interview to hype up their next match.\n";
        } else if (rng == 2) {
            matchre = w1 + " attacked " + w2 + " backstage!\n";
        } else if (rng == 3) {
            matchre = w1 + " attacked " + w2 + " during their promo!\n";
        } else if (rng == 4) {
            matchre = "The locker room had to come to the ring to break up a brawl after " + w1 + " beat down " + w2 + "!";
        } else {
            // if invalid assume option 1
            matchre = w1 + " insulted " + w2 + " in a promo interview to hype up their next match.\n";
        }

        return matchre;

    }

    static string RatingToGrade(int matchra) {
        string grade = "";
        if (matchra < 60) {
            grade = "F";
        } else if (matchra >= 60 && matchra < 68) {
            grade = "D";
        } else if (matchra == 68 || matchra == 69) {
            grade = "D+";
        } else if (matchra >= 70 && matchra < 78) {
            grade = "C";
        } else if (matchra == 78 || matchra == 79) {
            grade = "C+";
        } else if (matchra >= 80 && matchra < 88) {
            grade = "B";
        } else if (matchra == 88 || matchra == 89) {
            grade = "B+";
        } else if (matchra >= 90 && matchra < 98) {
            grade = "A";
        } else if (matchra >= 98) {
            grade = "A+";
        }
        return grade;
    }

    static void BookEvent(int matches, string fed, string eventna) {
        int i = 1;
        int j = 0;
        int finalrating, w1ov, w2ov, t1ov, t2ov, matchra, winner;
        finalrating = 0;
        w1ov = 0;
        w2ov = 0;
        t1ov = 0;
        t2ov = 0;
        matchra = 0;
        winner = 0;
        string[] results = new string[matches];
        int[] ratings = new int[matches];
        string matchre, titleop, team1, team2, wrestler1, wrestler2, segmentgrade, finalgrade;
        matchre = "";
        titleop = "";
        team1 = "";
        team2 = "";
        wrestler1 = "";
        wrestler2 = "";
        segmentgrade = "";
        finalgrade = "";
        while (i <= matches) {
            Console.WriteLine("Segment " + i + " of " + fed + " " + eventna);
            Console.WriteLine("Choose a match/segment type\n1:1v1 Match\n2:2v2 Match\n3:Promo Segment");
            int matchty = Convert.ToInt32(Console.ReadLine());
            if (matchty == 1) {
                Console.WriteLine("1v1 Singles Match");
                Console.WriteLine("Enter the name of the first wrestler:");
                wrestler1 = Console.ReadLine();
                Console.WriteLine("Enter the name of the second wrestler:");
                wrestler2 = Console.ReadLine();
                Console.WriteLine("Choose an option to represent " + wrestler1 + "'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber");
                w1ov = Convert.ToInt32(Console.ReadLine());
                w1ov = OvernessEval(w1ov);
                Console.WriteLine("Choose an option to represent " + wrestler2 + "'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber ");
                w2ov = Convert.ToInt32(Console.ReadLine());
                w2ov = OvernessEval(w2ov);
                Console.WriteLine("If this is a title match enter the title's name, if not type a lowercase n: ");
                titleop = Console.ReadLine();
                Console.WriteLine("Choose a winner for the match:\n1:" + wrestler1 + "\n2:" + wrestler2);
                winner = Convert.ToInt32(Console.ReadLine());

                switch (winner) {
                case 1:
                    matchre = wrestler1 + " defeated " + wrestler2 + " by pinfall.\n";
                    if (titleop != "n") {
                        matchre += "The match was for the " + titleop + ".\n";
                    }
                    break;
                case 2:
                    matchre = wrestler2 + " defeated " + wrestler1 + " by pinfall.\n";
                    if (titleop != "n") {
                        matchre += "The match was for the " + titleop + ".\n";
                    }
                    break;
                }

                matchra = DetermineRating(w1ov, w2ov);
                segmentgrade = RatingToGrade(matchra);
                matchre += "\nSegment Rating: " + segmentgrade;
                results[j] = matchre;
                ratings[j] = matchra;
                Console.WriteLine(matchre + "\n");
            } else if (matchty == 2) {
                Console.WriteLine("2v2 Tag Team Match");
                Console.WriteLine("Enter the name of the first team:");
                team1 = Console.ReadLine();
                Console.WriteLine("Enter the name of the second team:");
                team2 = Console.ReadLine();
                Console.WriteLine("Choose an option to represent " + team1 + "'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber ");
                t1ov = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("Choose an option to represent " + team2 + "'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber ");
                t2ov = Convert.ToInt32(Console.ReadLine());
                t1ov = OvernessEval(t1ov);
                t2ov = OvernessEval(t2ov);
                Console.WriteLine("If this is a title match enter the title's name, if not type a lowercase n: ");
                titleop = Console.ReadLine();
                Console.WriteLine("Choose a winner for the match:\n1:" + team1 + "\n2:" + team2);
                winner = Convert.ToInt32(Console.ReadLine());

                switch (winner) {
                case 1:
                    matchre = team1 + " defeated " + team2 + " by pinfall.\n";
                    if (titleop != "n") {
                        matchre += "The match was for the " + titleop + ".\n";
                    }
                    break;
                case 2:
                    matchre = team2 + " defeated " + team1 + " by pinfall.\n";
                    if (titleop != "n") {
                        matchre += "The match was for the " + titleop + ".\n";
                    }
                    break;
                }

                matchra = DetermineRating(t1ov, t2ov);
                segmentgrade = RatingToGrade(matchra);
                matchre += "\nSegment Rating: " + segmentgrade;
                results[j] = matchre;
                ratings[j] = matchra;
                Console.WriteLine(matchre + "\n");
            } else if (matchty == 3) {
                Console.WriteLine("Promo/Interview Segment");
                Console.WriteLine("Enter the name of the first wrestler or team: ");
                wrestler1 = Console.ReadLine();
                Console.WriteLine("Enter the name of the second wrestler or team: ");
                wrestler2 = Console.ReadLine();
                Console.WriteLine("Choose an option to represent " + wrestler1 + "'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber");
                w1ov = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("Choose an option to represent " + wrestler2 + "'s overness:\n1:Main Eventer\n2:Midcarder\n3:Jobber");
                w2ov = Convert.ToInt32(Console.ReadLine());
                w1ov = OvernessEval(w1ov);
                w2ov = OvernessEval(w2ov);
                Console.WriteLine("Choose a winner for the promo:\n1:" + wrestler1 + "\n2:" + wrestler2);
                winner = Convert.ToInt32(Console.ReadLine());

                switch (winner) {
                case 1:
                    matchre = Promos(wrestler1, wrestler2);
                    break;
                case 2:
                    matchre = Promos(wrestler2, wrestler1);
                    break;
                }

                matchra = DetermineRating(w1ov, w2ov);
                segmentgrade = RatingToGrade(matchra);
                matchre += "\nSegment Rating: " + segmentgrade;
                results[j] = matchre;
                ratings[j] = matchra;
                Console.WriteLine(matchre + "\n");
            }
            // incrementing counters after the match has been simmed
            i += 1;
            j += 1;
        }

        // resetting match counter for printing event results
        i = 1;
        Console.WriteLine("\n************************************\n" + fed + " " + eventna + " RESULTS\n************************************\n");
        foreach(string result in results) {
            Console.WriteLine("Segment " + i + " Result:\n" + result + "\n");
            i += 1;
        }

        foreach(int rating in ratings) {
            finalrating += rating;
        }

        finalrating = finalrating / Convert.ToInt32(matches);
        finalgrade = RatingToGrade(finalrating);
        Console.WriteLine("The final rating for " + fed + " " + eventna + " is: " + finalgrade);
    }

    public static void Main() {
        int matches;
        string fed, eventna;
        Console.WriteLine("Welcome to CSWRBS the free wrestling event booking simulator");
        Console.WriteLine("Enter the amount of matches/segments in the event:");
        matches = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Enter the name or abbv. of the wrestling federation hosting the event:");
        fed = Console.ReadLine();
        Console.WriteLine("Now Enter the event's name:");
        eventna = Console.ReadLine();
        BookEvent(matches, fed, eventna);
    }
}
