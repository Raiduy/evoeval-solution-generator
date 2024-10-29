import re
import csv

# Define a function to parse the log file
def parse_log(file_path):
    log_data = []
    with open(file_path, 'r') as file:
        log_content = file.read()

        # Define regular expressions for each component
        entry_pattern = re.compile(
            r"\*{36}\n>>> (\w+) <<<\n\*{36}\n\n"  # Run name
            r"Label\s*:\s*(\w+)\n"                 # Label
            r"Begin\s*:\s*(.+)\n"                  # Begin
            r"Duration\s*:\s*([\d.]+)\s*us\n"      # Duration
            r"[-]+\n"                              # Separator line
            r"PKG\s*:\n\s*socket 0\s*:\s*([\d.]+)\s*uJ\n"  # PKG
            r"[-]+\n"                              # Separator line
            r"DRAM\s*:\n\s*socket 0\s*:\s*([\d.]+)\s*uJ\n", # DRAM
            re.MULTILINE
        )

        # Extract each log entry using the entry pattern
        for match in entry_pattern.finditer(log_content):
            run_name = match.group(1)
            label = match.group(2)
            begin = match.group(3)
            duration = match.group(4)
            pkg = match.group(5)
            dram = match.group(6)

            log_data.append({
                "Run Name": run_name,
                "Label": label,
                "Begin": begin,
                "Duration (us)": duration,
                "PKG (uJ)": pkg,
                "DRAM (uJ)": dram
            })

    return log_data

# Define a function to write the parsed data to a CSV file
def write_to_csv(log_data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ["Run Name", "Label", "Begin", "Duration (us)", "PKG (uJ)", "DRAM (uJ)"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for data in log_data:
            writer.writerow(data)

log_file_path = '../logs/90.log'
output_csv_path = '90_data.csv'

log_data = parse_log(log_file_path)
write_to_csv(log_data, output_csv_path)

print("Log data parsed and written to CSV file successfully.")
