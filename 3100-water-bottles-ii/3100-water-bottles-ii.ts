function maxBottlesDrunk(numBottles: number, numExchange: number): number {
    let emptyBottles = numBottles;

    while (emptyBottles >= numExchange) {
        emptyBottles = emptyBottles - numExchange + 1;
        numBottles += 1;
        numExchange += 1;
    }
    return numBottles;
}