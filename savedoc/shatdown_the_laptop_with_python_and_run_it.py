import os

def simulate_shutdown():
    print("Simulating shutdown...")
    
    # Fake shutdown sequence
    for i in range(5):
        print(f"Shutting down ({i+1}/5)...")
        time.sleep(1)
        
    print("Shutdown complete!")

simulate_shutdown()
