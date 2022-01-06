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
            Console.WriteLine("Match " + i + " of " + fed + " " + eventna);
            Console.WriteLine("Choose a match type\n1:1v1\n2:2v2");
            int matchty = Convert.ToInt32(Console.ReadLine());
            if (matchty == 1) {
                Console.WriteLine("1v1 Singles Match");
                Console.WriteLine("Enter the name of the first wrestler:");
                wrestler1 = Console.ReadLine();
                Console.WriteLine("Enter the name of the second wrestler:");
                wrestler2 = Console.ReadLine();
                Console.WriteLine("Enter a number representing wrestler 1's overness on a scale of 100:");
                w1ov = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("Enter a number representing wrestler 2's overness on a scale of 100:");
                w2ov = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("If this is a title match enter the title's name, if not type a lowercase n:");
                titleop = Console.ReadLine();
                Console.WriteLine("Choose a winner for the match:\n1:" + wrestler1 + "\n2:" + wrestler2);
                winner = Convert.ToInt32(Console.ReadLine());

                switch (winner) {
                case 1:
                    matchre = wrestler1 + " defeated " + wrestler2 + " by pinfall.";
                    if (titleop != "n") {
                        matchre += "\nIn a match for the " + titleop + ".";
                        titlebonus = 10;
                    }
                    break;
                case 2:
                    matchre = wrestler2 + " defeated " + wrestler1 + " by pinfall.";
                    if (titleop != "n") {
                        matchre += "\nIn a match for the " + titleop + ".";
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
                Console.WriteLine(matchre);
            } else if (matchty == 2) {
                Console.WriteLine("2v2 Tag Team Match");
                Console.WriteLine("Enter the name of the first team:");
                team1 = Console.ReadLine();
                Console.WriteLine("Enter the name of the second team:");
                team2 = Console.ReadLine();
                Console.WriteLine("Enter a number representing team 1's overness on a scale of 100:");
                t1ov = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("Enter a number representing team 2's overness on a scale of 100:");
                t2ov = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("If this is a title match enter the title's name, if not type a lowercase n:");
                titleop = Console.ReadLine();
                Console.WriteLine("Choose a winner for the match:\n1:" + team1 + "\n2:" + team2);
                winner = Convert.ToInt32(Console.ReadLine());

                switch (winner) {
                case 1:
                    matchre = team1 + " defeated " + team2 + " by pinfall.";
                    if (titleop != "n") {
                        matchre += "\nIn a match for the " + titleop + ".";
                        titlebonus = 10;
                    }
                    break;
                case 2:
                    matchre = team2 + " defeated " + team1 + " by pinfall.";
                    if (titleop != "n") {
                        matchre += "\nIn a match for the " + titleop + ".";
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
                Console.WriteLine(matchre);
            }
            // incrementing counters after the match has been simmed
            i += 1;
            j += 1;
        }

        i = 1;
        Console.WriteLine("************************************\n" + fed + " " + eventna + " RESULTS\n************************************\n");
        foreach(string result in results) {
            Console.WriteLine("Match " + i + " Result:\n" + result + "\n");
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
        Console.WriteLine("Enter the amount of matches in the event:");
        matches = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Enter the name or abbv. of the wrestling federation hosting the event:");
        fed = Console.ReadLine();
        Console.WriteLine("Now Enter the event's name:");
        eventna = Console.ReadLine();
        BookEvent(matches, fed, eventna);
    }
}
