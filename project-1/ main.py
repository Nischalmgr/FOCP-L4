import sys
from tabulate import tabulate
def parse_drivers(file_path):
    """Parse the  file to extract driver details."""
    driver_details = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    _, code, name, team = parts
                    driver_details[code] = {"name": name, "team": team}
                else:
                    print(f"Skipping malformed line in drivers file: {line.strip()}")
    except FileNotFoundError:
        print(f"Drivers file not found: {file_path}")
        sys.exit(1)
    return driver_details

def parselap_times(file_path):
    """Parse the lap times file to take  location and lap time."""
    lap_data = {}
    location = None
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            location = file.readline().strip()
            if not location:
                print("Lap times file is empty or missing location information.")
                sys.exit(1)

            for line in file:
                line = line.strip()
                # Extract driver code and lap time
                for i, char in enumerate(line):
                    if char.isdigit():
                        driver_code = line[:i]
                        lap_time = line[i:]
                        break
                else:
                    print(f"Skipping malformed line in lap times file: {line}")
                    continue

                try:
                    lap_time = float(lap_time)
                    if driver_code not in lap_data:
                        lap_data[driver_code] = []
                    lap_data[driver_code].append(lap_time)
                except ValueError:
                    print(f"Skipping invalid lap time in file: {line}")
    except FileNotFoundError:
        print(f"Lap times file not found: {file_path}")
        sys.exit(1)
    return location, lap_data

def process_data(lap_data):
    """Process lap data to compute fastest lap, average times ."""
    if not lap_data:
        print("No lap data found. Please check the lap times file.")
        sys.exit(1)

    fastest_overall = None
    fastest_each_driver = {}
    average_each_driver = {}
    all_lap_times = []

    for driver, laps in lap_data.items():
        if not laps:  # Skip drivers with no laps
            continue
        fastest_time = min(laps)
        average_time = sum(laps) / len(laps)
        fastest_each_driver[driver] = fastest_time
        average_each_driver[driver] = average_time
        all_lap_times.extend(laps)

        if fastest_overall is None or fastest_time < fastest_overall[1]:
            fastest_overall = (driver, fastest_time)

    if not all_lap_times:  # Check if no lap times are available at all
        print("No valid lap times found. Please check the lap times file.")
        sys.exit(1)

    overall_average = sum(all_lap_times) / len(all_lap_times)
    return fastest_overall, fastest_each_driver, average_each_driver, overall_average

def display_results(location, fastest_overall, fastest_each_driver, average_each_driver, overall_average, driver_details):
    """Display the results in a readable format with driver details."""
    print(f"\nGrand Prix Location: {location}\n")
    
    fastest_driver_code = fastest_overall[0]
    fastest_driver = driver_details.get(fastest_driver_code, {})
    fastest_name = fastest_driver.get("name", fastest_driver_code)
    fastest_team = fastest_driver.get("team", "Unknown")

    print(f"Fastest Lap: {fastest_name} ({fastest_team}) with time {fastest_overall[1]:.3f} seconds")
    
    print("\nDriver Performance:")
    table = []
    for driver, fastest_time in sorted(fastest_each_driver.items(), key=lambda x: x[1]):
        avg_time = average_each_driver[driver]
        driver_info = driver_details.get(driver, {})
        name = driver_info.get("name", driver)
        team = driver_info.get("team", "Unknown")
        table.append([name, team, f"{fastest_time:.3f}", f"{avg_time:.3f}"])

    print(tabulate(table, headers=["Driver", "Team", "Fastest Time", "Average Time"], tablefmt="grid"))
    print(f"\nOverall Average Lap Time: {overall_average:.3f} seconds")
    print("\n")


if __name__ == "__main__":
    #Take arguments files
    if len(sys.argv) < 5:
        print("Usage: python main.py <driver_file> <lap_file1><lap_file2><lap_file3>")
        sys.exit(1)

    lap_times_files = sys.argv[2:]
    drivers_file = sys.argv[1]
    #Displays all all lpa1 lap2 and lap3 details
    for i, lap_time in enumerate(lap_times_files):
     print("Lap:",i+1)
    

     location, lap_data = parselap_times(lap_time)
     if not lap_data:
        print("No valid lap data found. Please check the input file.")
        sys.exit(1)

     driver_details = parse_drivers(drivers_file)
     fastest_overall, fastest_each_driver, average_each_driver, overall_average = process_data(lap_data)
     display_results(location, fastest_overall, fastest_each_driver, average_each_driver, overall_average, driver_details)

