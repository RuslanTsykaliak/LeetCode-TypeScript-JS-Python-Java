function findClosest(x: number, y: number, z: number): number {
    // We need to return 1, 2, or 0
    // 1 if Person 1 (at position x) reaches position z first
    // 2 if Person 2 (at position y) reaches position z first
    // 0 if both Person 1 and Person 2 reach position z at the same time

    // We need to find the distance each person must travel
    // The winner is the person with the smaller distance
    // For example: x = 2, y = 7, z = 4
    // Distance for Person 1 = |z - x| = |4 - 2| = 2
    // Distance for Person 2 = |z - y| = |4 - 7| = 3 (we use Math.abs to handle negative values)
    // Compare the distances to determine the winner

    let distanceX = Math.abs(z - x);
    let distanceY = Math.abs(z - y);

    if (distanceX < distanceY) {
        return 1;
    } else if (distanceX > distanceY) {
        return 2;
    } else {
        return 0;
    }
};