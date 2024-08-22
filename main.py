from utils import pelivalikko, progress_bar
import time

if __name__ == "__main__":
    total = 100 
    
    for i in range(total + 1):
        progress_bar(i, total)

    print()
    
    pelivalikko() 
