import concurrent.futures
import subprocess

def run_script(ip):
    """Function to run the shell script with the given IP address."""
    command = f"./nmapAutomator.sh --host {ip} --type All"
    subprocess.run(command, shell=True)

def main():
    with open("target.txt", "r") as file:
        ips = [line.strip() for line in file if line.strip()]

    # Using ThreadPoolExecutor to run the script concurrently for each IP
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(run_script, ips)

if __name__ == "__main__":
    main()
