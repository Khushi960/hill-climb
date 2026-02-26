import random

def main():
    tsp = [
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0]
    ]

    route, distance = hillClimbing(tsp)
    print("Best Route:", route)
    print("Minimum Distance:", distance)


def hillClimbing(tsp):
    current = randomSolution(tsp)
    currentDistance = routeLength(tsp, current)

    while True:
        neighbours = getNeighbours(current)
        bestNeighbour = current
        bestDistance = currentDistance

        for neighbour in neighbours:
            dist = routeLength(tsp, neighbour)
            if dist < bestDistance:
                bestNeighbour = neighbour
                bestDistance = dist

        if bestDistance >= currentDistance:
            break

        current = bestNeighbour
        currentDistance = bestDistance

    return current, currentDistance


def randomSolution(tsp):
    route = list(range(len(tsp)))
    random.shuffle(route)
    return route


def routeLength(tsp, route):
    total = 0
    for i in range(len(route)):
        total += tsp[route[i]][route[(i + 1) % len(route)]]
    return total


def getNeighbours(route):
    neighbours = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            newRoute = route[:]
            newRoute[i], newRoute[j] = newRoute[j], newRoute[i]
            neighbours.append(newRoute)
    return neighbours


if __name__ == "__main__":
    main()