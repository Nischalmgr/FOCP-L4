# Race Results Analysis

This Python program processes race lap time data and driver details to provide detailed insights into driver performance during a Grand Prix. It reads data from files, calculates statistics, and displays results in a formatted manner.

## Features
- Parse driver details from a CSV file.
- Parse lap time data from multiple files.
- Calculate:
  - Fastest lap time for each driver.
  - Average lap time for each driver.
  - Overall fastest lap time.
  - Overall average lap time.
- Display the results in a readable tabular format using the `tabulate` library.

---

## Prerequisites

1. **Python 3.x**
   Ensure Python 3.x is installed on your system.

2. **Dependencies**
   Install the `tabulate` library:
   ```bash
   pip install tabulate
   ```

---

## File Format Requirements

### Drivers File Format
The driver file should be a CSV file with the following structure:
```csv
Row_Number,Driver_Code,Driver_Name,Team_Name
```
**Example:**
```csv
1,DR1,John Doe,Team A
2,DR2,Jane Smith,Team B
```

### Lap Times File Format
Each lap time file should:
- Start with the Grand Prix location (one line).
- Contain driver codes followed by their lap times in seconds.

**Example:**
```txt
Silverstone
DR1,85.432
DR2,84.923
```

---

## Usage

Run the program with the following command:
```bash
python main.py <drivers_file> <lap_times_file1> <lap_times_file2> <lap_times_file3>
```

### Example:
```bash
python main.py drivers.csv lap1.txt lap2.txt lap3.txt
```

### Output:
- Displays the Grand Prix location.
- Outputs the fastest lap and driver details.
- Shows driver performance in a tabular format.
- Provides the overall average lap time.

---

## Functions

### `parse_drivers(file_path)`
Parses the drivers file to extract driver details.
- **Input:** Path to the driver file.
- **Output:** Dictionary with driver codes as keys and driver details as values.

### `parselap_times(file_path)`
Parses a lap times file to extract the location and lap times.
- **Input:** Path to a lap times file.
- **Output:** Location (string) and lap data (dictionary).

### `process_data(lap_data)`
Processes lap data to calculate statistics.
- **Input:** Lap data dictionary.
- **Output:** Fastest overall lap, fastest lap per driver, average lap per driver, and overall average lap time.

### `display_results(location, fastest_overall, fastest_each_driver, average_each_driver, overall_average, driver_details)`
Displays the results in a user-friendly format.
- **Inputs:** Location, calculated statistics, and driver details.

---

## Error Handling
- **Malformed Data:** Skips lines that don't match the expected format.
- **File Not Found:** Exits with an error message if any file is missing.
- **Empty Data:** Exits with an error message if the lap times file has no valid data.

---

## Sample Output
```
Grand Prix Location: dewsberry

Fastest Lap: Jane Smith (Team B) with time 84.923 seconds

Driver Performance:
+-------------+---------+---------------+--------------+
| Driver      | Team    | Fastest Time  | Average Time |
+-------------+---------+---------------+--------------+
| Jane Smith  | Team B  | 84.923        | 85.125       |
| John Doe    | Team A  | 85.432        | 85.789       |
+-------------+---------+---------------+--------------+

Overall Average Lap Time: 85.457 seconds
```

---

## Notes
- Ensure the input files follow the required format.
- You can add more lap times files to analyze additional races.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.
