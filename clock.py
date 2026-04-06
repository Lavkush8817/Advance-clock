import time
import os

def digital_clock():
    try:
        while True:
            # Get the current time in HH:MM:SS format
            current_time = time.strftime("%H:%M:%S")
            
            # Clear the terminal screen (works for Windows and Mac/Linux)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("========================")
            print(f"  CURRENT TIME: {current_time}  ")
            print("========================")
            print("Press Ctrl+C to stop the clock")
            
            # Wait for 1 second before updating
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped by user.")

if __name__ == "__main__":
    digital_clock()
