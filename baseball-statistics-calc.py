def calculate_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0.0
    else:
        batting_average = float(hits / at_bats)
        return round(batting_average, 3)  # Round the batting average to 3 decimal places

def calculate_slugging_percentage(hits, singles, doubles, triples, home_runs, at_bats):
    if at_bats == 0:
        return 0.0
    else:
        total_bases = singles + (2 * doubles) + (3 * triples) + (4 * home_runs) 
        return total_bases / at_bats #calculate and return slugging percentage

def calculate_on_base_percentage(hits, walks, hit_by_pitch, at_bats):
    plate_appearances = at_bats + walks + hit_by_pitch
    if plate_appearances == 0:
        return 0.0 #calculate on base percentage to be used in OPS calculation
    else:
        return (hits + walks + hit_by_pitch) / plate_appearances

def calculate_ops(batting_average, on_base_percentage, slugging_percentage):
    return batting_average + on_base_percentage + slugging_percentage #combines battingAVG, on-base %, and slugging %, to calculate OPS

def get_user_input(): #ask user for all neccesary parameters
    hits = int(input("Enter the total number of hits (singles, doubles, triples, home runs): "))
    singles = int(input("Enter the number of singles: "))
    doubles = int(input("Enter the number of doubles: "))
    triples = int(input("Enter the number of triples: "))
    home_runs = int(input("Enter the number of home runs: "))
    at_bats = int(input("Enter the number of at-bats: "))
    walks = int(input("Enter the number of walks: "))
    hit_by_pitch = int(input("Enter the number of times hit by pitch: "))
    
    return hits, singles, doubles, triples, home_runs, at_bats, walks, hit_by_pitch


def calculate_all_stats(hits, singles, doubles, triples, home_runs, at_bats, walks, hit_by_pitch):
    batting_average = calculate_batting_average(hits, at_bats)
    slugging_percentage = calculate_slugging_percentage(hits, singles, doubles, triples, home_runs, at_bats)
    on_base_percentage = calculate_on_base_percentage(hits, walks, hit_by_pitch, at_bats)
    ops = calculate_ops(batting_average, on_base_percentage, slugging_percentage)
    
    return batting_average, slugging_percentage, ops


def main():
    print("Baseball Statistics Calculator")
    print("----------------------------------")

    print("Choose the statistic you want to calculate:") #outputs the menu, and gives user options for what they want to calculate
    print("1. Batting Average")
    print("2. Slugging Percentage")
    print("3. OPS")
    print("4. All Three Stats")

    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 1:  
        hits, at_bats = get_user_input()[:2]  # Get only hits and at-bats for batting average
        batting_average = calculate_batting_average(hits, at_bats)
        print(f"Batting Average: {batting_average:.3f}") #displays batting average to three decimal places


    elif choice == 2:
        hits, singles, doubles, triples, home_runs, at_bats = get_user_input()[:6]
        slugging_percentage = calculate_slugging_percentage(hits, singles, doubles, triples, home_runs, at_bats)
        print(f"Slugging Percentage: {slugging_percentage:.3f}") #display sliugging percentage to three decimal places
    
    elif choice == 3:
        hits, singles, doubles, triples, home_runs, at_bats, walks, hit_by_pitch = get_user_input()
        batting_average = calculate_batting_average(hits, at_bats)
        on_base_percentage = calculate_on_base_percentage(hits, walks, hit_by_pitch, at_bats)
        slugging_percentage = calculate_slugging_percentage(hits, singles, doubles, triples, home_runs, at_bats)
        ops = calculate_ops(batting_average, on_base_percentage, slugging_percentage)
        print(f"OPS: {ops:.3f}") #display OPS to three deciamal places
    
    elif choice == 4:
        hits, singles, doubles, triples, home_runs, at_bats, walks, hit_by_pitch = get_user_input()
        batting_average, slugging_percentage, ops = calculate_all_stats(hits, singles, doubles, triples, home_runs, at_bats, walks, hit_by_pitch)
        #display all 3 stats to three decimal places
        print(f"Batting Average: {batting_average}")
        print(f"Slugging Percentage: {slugging_percentage:.3f}")
        print(f"OPS: {ops:.3f}") 
    
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        #breaks loop

if __name__ == "__main__":
    main()
