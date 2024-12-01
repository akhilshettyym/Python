def min_cost_to_form_string(n, substrings, main_string):
    m = len(main_string)
    dp = [float('inf')] * (m + 1)
    dp[0] = 0  # Base case: no cost to form an empty string

    for sub, cost in substrings:
        sub_len = len(sub)
        for i in range(m - sub_len + 1):  # Check all starting positions
            if main_string[i:i + sub_len] == sub:
                dp[i + sub_len] = min(dp[i + sub_len], dp[i] + cost)

    return dp[m] if dp[m] != float('inf') else "Impossible"


# Input parsing
def main():
    # Example input
    input_data = """10
evi 8
vta 9
co 1
dev 5
vit 6
odv 2
d 3
de 4
itaa 1
a 7
codevita"""
    lines = input_data.splitlines()
    n = int(lines[0])
    substrings = []
    for i in range(1, n + 1):
        sub, cost = lines[i].rsplit(maxsplit=1)
        substrings.append((sub, int(cost)))
    main_string = lines[n + 1]
    
    # Solve
    result = min_cost_to_form_string(n, substrings, main_string)
    print(result)

main()