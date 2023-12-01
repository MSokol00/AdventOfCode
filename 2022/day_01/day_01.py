def main():
    calories_per_elf = []

    with open('input.txt', 'r') as file:
        cal = 0
        for line in file:
            l = line.strip('\n')
            if l:
                cal += int(l)
            else:
                calories_per_elf.append(cal)
                cal = 0

    print(f'Part 1: {max(calories_per_elf)}')


    top_3_calories = []
    for i in range(3):
        top_3_calories.append(calories_per_elf.pop(calories_per_elf.index(max(calories_per_elf))))

    print(f'Part 2: {sum(top_3_calories)}')

if __name__ == '__main__':
    main()