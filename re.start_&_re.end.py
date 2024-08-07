def find_substring_indices(s, sub):
    start = 0
    while start <= len(s) - len(sub):
        pos = s.find(sub, start)
        if pos == -1:
            break
        print(f"({pos}, {pos + len(sub) - 1})")
        start = pos + 1
    
    if start == 0:
        print((-1, -1))

# Reading input from standard input (you may adjust this part based on how you're testing it)
if __name__ == "__main__":
    s = input().strip()
    sub = input().strip()
    find_substring_indices(s, sub)