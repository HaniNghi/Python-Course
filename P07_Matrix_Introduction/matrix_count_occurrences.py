def count_occurrences(matrix, item_to_count )->int:
    count = 0
    for row in matrix:
        for i in row:
            if i == item_to_count:
                count += 1
    return count

def main():
 m = [[1, 2, 3], [1, 2, 2], [1, 1, 1], [1, 2, 1]]
 print(count_occurrences(m, 1))
 print(count_occurrences(m, 2))
 print(count_occurrences(m, 5))

if __name__ == "__main__":
    main()