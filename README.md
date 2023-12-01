# Baseball Statistics Calculator

This Python program allows users to calculate various baseball statistics based on user input. The statistics currently supported are:

1. Batting Average: Calculates the batting average using the total number of hits and at-bats.
2. Slugging Percentage: Computes the slugging percentage using hits, singles, doubles, triples, home runs, and at-bats.
3. OPS (On-base Plus Slugging): Combines batting average, on-base percentage, and slugging percentage.

## How to Use

1. Run the program by executing the `main` function in the `baseball_calculator.py` file.

2. Choose the statistic you want to calculate by entering the corresponding number (1, 2, or 3) when prompted.

3. Enter the required information such as the total number of hits, singles, doubles, triples, home runs, at-bats, walks, and times hit by pitch.

4. The program will display the calculated statistic based on your input.

Example Usage

```bash
Baseball Statistics Calculator
----------------------------------
Choose the statistic you want to calculate:
1. Batting Average
2. Slugging Percentage
3. OPS
Enter your choice (1/2/3): 1
Enter the total number of hits (singles, doubles, triples, home runs): 200
Enter the number of singles: 100
Enter the number of doubles: 50
Enter the number of triples: 50
Enter the number of home runs: 0
Enter the number of at-bats: 1000
Enter the number of walks: 2
Enter the number of times hit by pitch: 2
Batting Average: 0.200
