def calculate_batting_average(hits, at_bats):
        batting_average = float(hits / at_bats)
        return round(batting_average, 3)  # Round the batting average to 3 decimal places

def calculate_slugging_percentage(hits, singles, doubles, triples, home_runs, at_bats):
    if at_bats == 0:
        return 0.0
    else:
        total_bases = singles + (2 * doubles) + (3 * triples) + (4 * home_runs)
        return total_bases / at_bats

def calculate_on_base_percentage(hits, walks, hit_by_pitch, at_bats):
    plate_appearances = at_bats + walks + hit_by_pitch
    if plate_appearances == 0:
        return 0.0
    else:
        return (hits + walks + hit_by_pitch) / plate_appearances

def calculate_ops(batting_average, on_base_percentage, slugging_percentage):
    return batting_average + on_base_percentage + slugging_percentage

def get_user_input():
    hits = int(input("Enter the total number of hits (singles, doubles, triples, home runs): "))
    singles = int(input("Enter the number of singles: "))
    doubles = int(input("Enter the number of doubles: "))
    triples = int(input("Enter the number of triples: "))
    home_runs = int(input("Enter the number of home runs: "))
    at_bats = int(input("Enter the number of at-bats: "))
    walks = int(input("Enter the number of walks: "))
    hit_by_pitch = int(input("Enter the number of times hit by pitch: "))
    
    return hits, singles, doubles, triples, home_runs, at_bats, walks, hit_by_pitch




def main():
    print("Baseball Statistics Calculator")
    print("----------------------------------")

    print("Choose the statistic you want to calculate:")
    print("1. Batting Average")
    print("2. Slugging Percentage")
    print("3. OPS")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        hits, at_bats = get_user_input()[:2]  # Get only hits and at-bats for batting average
        batting_average = calculate_batting_average(at_bats, hits)
        print(f"Batting Average: {batting_average}")

    elif choice == 2:
        hits, singles, doubles, triples, home_runs, at_bats = get_user_input()[:6]
        slugging_percentage = calculate_slugging_percentage(hits, singles, doubles, triples, home_runs, at_bats)
        print(f"Slugging Percentage: {slugging_percentage:.3f}")
    elif choice == 3:
        hits, singles, doubles, triples, home_runs, at_bats, walks, hit_by_pitch = get_user_input()
        batting_average = calculate_batting_average(hits, at_bats)
        on_base_percentage = calculate_on_base_percentage(hits, walks, hit_by_pitch, at_bats)
        slugging_percentage = calculate_slugging_percentage(hits, singles, doubles, triples, home_runs, at_bats)
        ops = calculate_ops(batting_average, on_base_percentage, slugging_percentage)
        print(f"OPS: {ops:.3f}")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()    print("Choose the statistic you want to calculate:")
    print("1. Batting Average")
    print("2. Slugging Percentage")
    print("3. OPS")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        hits, at_bats = get_user_input()[:2]  # Get only hits and at-bats for batting average
        batting_average = calculate_batting_average(hits, at_bats)
        print(f"Batting Average: {batting_average:.3f}")
    elif choice == 2:
        hits, singles, doubles, triples, home_runs, at_bats = get_user_input()[:6]
        slugging_percentage = calculate_slugging_percentage(hits, singles, doubles, triples, home_runs, at_bats)
        print(f"Slugging Percentage: {slugging_percentage:.3f}")
    elif choice == 3:
        hits, singles, doubles, triples, home_runs, at_bats, walks, hit_by_pitch = get_user_input()
        batting_average = calculate_batting_average(hits, at_bats)
        on_base_percentage = calculate_on_base_percentage(hits, walks, hit_by_pitch, at_bats)
        slugging_percentage = calculate_slugging_percentage(hits, singles, doubles, triples, home_runs, at_bats)
        ops = calculate_ops(batting_average, on_base_percentage, slugging_percentage)
        print(f"OPS: {ops:.3f}")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

