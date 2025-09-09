const sumVals = (arr) => {
    let ret = 0
    for (let i = 0; i < arr.length; i += 1) {
        ret += arr[i] % (10 ** 9 + 7)
    }
    return ret
}

function peopleAwareOfSecret(n: number, delay: number, forget: number): number {
    let prevLine = Array(forget).fill(0)
    prevLine[0] = 1

    for (let day = 1; day < n; day += 1) {
        const previousDayArr = prevLine
        const newDayArr = []
        for (let knownForDays = 0; knownForDays < forget; knownForDays += 1) {
            // The number of people that know the secret for exactly 1 day is the sum of all people that know the secret for more than delay days
            if (knownForDays === 0) {
                let knownForOneDay = 0
                let iter = delay - 1; // Note: Need to substract 1 because we shift first then determin how many new people are told the secret
                while (iter < forget - 1) {
                    knownForOneDay += previousDayArr[iter] % (10 ** 9 + 7)
                    iter += 1
                }
                newDayArr.push(knownForOneDay)
            } else {
                newDayArr.push(previousDayArr[knownForDays - 1])
            }
        }
        prevLine = newDayArr
    }
    return sumVals(prevLine) % (10 ** 9 + 7)
};