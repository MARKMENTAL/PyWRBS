using System;

class CSWRBS {
    static void BookEvent(int matches, string fed, string eventna) {
        int i = 1;
        int j = 0;
        Random rnd = new Random();
        int finalrating, titlebonus, w1ov, w2ov, t1ov, t2ov, matchra, winner;
        finalrating = 0;
        titlebonus = 0;
        w1ov = 0;
        w2ov = 0;
        t1ov = 0;
        t2ov = 0;
        matchra = 0;
        winner = 0;
        string[] results = new string[matches];
        int[] ratings = new int[matches];
        string matchre, titleop, team1, team2, wrestler1, wrestler2;
        matchre = "";
        titleop = "";
        team1 = "";
        team2 = "";
        wrestler1 = "";
        wrestler2 = "";
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
                Console.WriteLine("Enter a number representing " +wrestler1 +"'s overness on a scale of 100: ");
                w1ov = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("Enter a number representing " +wrestler2 +"'s overness on a scale of 100: ");
                w2ov = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("If this is a title match enter the title's name, if not type a lowercase n: ");
                titleop = Console.ReadLine();
                Console.WriteLine("Choose a winner for the match:\n1:" + wrestler1 + "\n2:" + wrestler2);
                winner = Convert.ToInt32(Console.ReadLine());

                switch (winner) {
                case 1:
                    matchre = wrestler1 + " defeated " + wrestler2 + " by pinfall.\n";
                    if (titleop != "n") {
                        matchre += "The match was for the " + titleop + ".\n";
                        titlebonus = 10;
                    }
                    break;
                case 2:
                    matchre = wrestler2 + " defeated " + wrestler1 + " by pinfall.\n";
                    if (titleop != "n") {
                        matchre += "The match was for the " + titleop + ".\n";
                        titlebonus = 10;
                    }
                    break;
                }

                matchra = w1ov + w2ov - rnd.Next(85, 110);
                matchra += rnd.Next(8, 17);
                matchra += titlebonus;
                matchre += "\nMatch Rating: " + matchra;
                results[j] = matchre;
                ratings[j] = matchra;
                Console.WriteLine(matchre +"\n");
            } else if (matchty == 2) {
                Console.WriteLine("2v2 Tag Team Match");
                Console.WriteLine("Enter the name of the first team:");
                team1 = Console.ReadLine();
                Console.WriteLine("Enter the name of the second team:");
                team2 = Console.ReadLine();
                Console.WriteLine("Enter a number representing " +team1+"'s overness on a scale of 100: ");
                t1ov = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("Enter a number representing " +team2 +"'s overness on a scale of 100: ");
                t2ov = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("If this is a title match enter the title's name, if not type a lowercase n: ");
                titleop = Console.ReadLine();
                Console.WriteLine("Choose a winner for the match:\n1:" + team1 + "\n2:" + team2);
                winner = Convert.ToInt32(Console.ReadLine());

                switch (winner) {
                case 1:
                    matchre = team1 + " defeated " + team2 + " by pinfall.\n";
                    if (titleop != "n") {
                        matchre += "The match was for the " + titleop + ".\n";
                        titlebonus = 10;
                    }
                    break;
                case 2:
                    matchre = team2 + " defeated " + team1 + " by pinfall.\n";
                    if (titleop != "n") {
                        matchre += "The match was for the " + titleop + ".\n";
                        titlebonus = 10;
                    }
                    break;
                }

                matchra = t1ov + t2ov - rnd.Next(85, 110);
                matchra += rnd.Next(8, 17);
                matchra += titlebonus;
                matchre += "\nMatch Rating: " + matchra;
                results[j] = matchre;
                ratings[j] = matchra;
                Console.WriteLine(matchre +"\n");
            } else if (matchty == 3){
                Console.WriteLine("Promo/Interview Segment");
                Console.WriteLine("Enter the name of the first wrestler or team, they will be on the attacking side of this promo: ");
                wrestler1 = Console.ReadLine();
                Console.WriteLine("Enter the name of the second wrestler or team, they will be on the defending side of this promo: ");
                wrestler2 = Console.ReadLine();
                Console.WriteLine("Enter a number representing " +wrestler1 +"'s microphone skills on a scale of 100:");
                w1ov = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("Enter a number representing " +wrestler2 +"'s microphone skills on a scale of 100:");
                w2ov = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("Choose a winner for the promo:\n1:" + wrestler1 + "\n2:" + wrestler2);
                winner = Convert.ToInt32(Console.ReadLine());

                switch (winner) {
                case 1:
                    matchre = wrestler1 + " insulted and intimidated " + wrestler2 + " to hype up their next match.\n";
                    break;
                case 2:
                    matchre = wrestler2 + " came out to ambush and attack " + wrestler1 + ", ruining their promo.\n";
                    break;
                }
                
                matchra = w1ov + w2ov - rnd.Next(85, 110);
                matchra += rnd.Next(8, 17);
                matchre += "\nSegment Rating: " + matchra;
                results[j] = matchre;
                ratings[j] = matchra;
                Console.WriteLine(matchre +"\n");
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
        Console.WriteLine("The final rating for " + fed + " " + eventna + " is: " + finalrating);
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
