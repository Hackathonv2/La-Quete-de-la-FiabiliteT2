def main():
    try:
        m, c = input().split(" ")
        m = int(m)
        c = int(c)
    except ValueError:
        print("Error: m and c must be integers.")
        exit(84)
    if m < 2 or m > 100:
        print("Error: m must be between 2 and 100.")
        exit(84)
    if c < m - 1 or c > (m * m - 1):
        print("Error: c must be between m - 1 and m * m - 1.")
        exit(84)

    links: list[tuple[str, str]] = []
    for i in range(c):
        try:
            a, b = input().split(" ")
        except ValueError:
            print(f"Error: invalid link at line: {i + 2}.")
            exit(84)
        if len(a) != 5 or len(b) != 5:
            print(f"Error: machine name's must be 5 character at line: {i + 2}.")
            exit(84)
        if a == b:
            print(f"Error: invalid link at line: {i + 2}.")
            exit(84)
        links.append((a, b))

    schema: dict[str, list[str]] = {}
    for a, b in links:
        if a not in schema:
            schema[a] = []
        schema[a].append(b)
        if b not in schema:
            schema[b] = []

    for machine in schema:
        if len(schema[machine]) != 1:
            continue
        if len(schema[schema[machine][0]]) >= m - 2:
            print(machine)
            exit(0)
    print("Error: no solution found.")
    exit(84)


if __name__ == '__main__':
    main()
