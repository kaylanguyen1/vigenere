import sys
from datetime import datetime

def logger(log_file, log_message):
     with open(log_file, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        file.write(f"{timestamp} {log_message}\n")
def main():
    log_file = sys.argv[1]
    
    while True:
        log_message = sys.stdin.readline().strip()
        if not log_message:
            continue
        if log_message == "[QUIT] Exiting program":
            break
        logger(log_file, log_message)
        

if __name__ == "__main__":
    main()