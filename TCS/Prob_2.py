from collections import defaultdict

def parse_input():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    N, M = map(int, data[0].split())
    friendships = [tuple(map(int, line.split())) for line in data[1:M + 1]]
    K = int(data[M + 1])

    return N, friendships, K

def calculate_rostering_days(N, friendships, K):
    # Initialize adjacency list for friendships
    graph = defaultdict(list)
    for a, b in friendships:
        graph[a].append(b)
        graph[b].append(a)

    # Initial attendance (Day 1: All WFO)
    current_attendance = [True] * N  # True for WFO, False for WFH

    rostering_value = N  # Day 1 total attendance
    total_days = 1       # Start with day 1

    while rostering_value < K:
        next_attendance = [False] * N

        for employee in range(N):
            friends_wfo = sum(current_attendance[friend] for friend in graph[employee])

            if current_attendance[employee]:  # WFO today
                if friends_wfo == 3:
                    next_attendance[employee] = True
            else:  # WFH today
                if friends_wfo < 3:
                    next_attendance[employee] = True

        # Update attendance for the next day
        current_attendance = next_attendance
        rostering_value += sum(current_attendance)
        total_days += 1

    return total_days

def main():
    N, friendships, K = parse_input()
    result = calculate_rostering_days(N, friendships, K)
    print(result)

if __name__ == "__main__":
    main()