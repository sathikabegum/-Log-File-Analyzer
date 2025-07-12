import re

# Path to the system log file
log_path = "/var/log/auth.log"  # Change if you're using a different log

# Regular expression to find failed SSH login attempts
pattern = re.compile(r"Failed password for (invalid user )?(\w+) from ([\d.]+)")

failed_attempts = {}

with open(log_path, "r") as file:
    for line in file:
        match = pattern.search(line)
        if match:
            user = match.group(2)
            ip = match.group(3)
            key = (user, ip)
            failed_attempts[key] = failed_attempts.get(key, 0) + 1

# Print the results
print("📌 Failed SSH login attempts detected:\n")
for (user, ip), count in failed_attempts.items():
    print(f"User: {user:10} | IP: {ip:15} | Attempts: {count}")
