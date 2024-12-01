def parse_matrix(matrix_lines):
    matrices = []
    for col in range(0, len(matrix_lines[0]), 3):
        digit_matrix = [
            matrix_lines[0][col:col + 3],
            matrix_lines[1][col:col + 3],
            matrix_lines[2][col:col + 3]
        ]
        matrices.append(digit_matrix)
    return matrices

def is_valid_digit(matrix, digits):
    for digit_index, digit in enumerate(digits):
        diff_count = 0
        for row1, row2 in zip(matrix, digit):
            for cell1, cell2 in zip(row1, row2):
                if cell1 != cell2:
                    diff_count += 1
                if diff_count > 1:
                    break
            if diff_count > 1:
                break
        if diff_count <= 1:
            return True
    return False

def possible_digits(matrix, digits):
    possibilities = []
    for digit_index, digit in enumerate(digits):
        diff_count = 0
        for row1, row2 in zip(matrix, digit):
            for cell1, cell2 in zip(row1, row2):
                if cell1 != cell2:
                    diff_count += 1
                if diff_count > 1:
                    break
            if diff_count > 1:
                break
        if diff_count <= 1:
            possibilities.append(digit_index)
    return possibilities

def calculate_possible_numbers(input_number, digits):
    all_possibilities = []
    for matrix in input_number:
        if not is_valid_digit(matrix, digits):
            return "Invalid"
        all_possibilities.append(possible_digits(matrix, digits))

    total_sum = 0
    from itertools import product

    for combination in product(*all_possibilities):
        total_sum += int("".join(map(str, combination)))

    return total_sum

def main():
    import sys
    input_lines = sys.stdin.read().strip().split("\n")

    digits = parse_matrix(input_lines[:3])

    input_number = parse_matrix(input_lines[3:])

    result = calculate_possible_numbers(input_number, digits)
    print(result)

if __name__ == "__main__":
    main()