function avoidFlood(rains: number[]): number[] {
    let dryDays = [];
    let n = rains.length;
    let result = Array(n).fill(-1);
    let lakeMap = new Map();

    function binarySearch(target) {
        let left = 0;
        let right = dryDays.length;

        while (left < right) {
            let mid = Math.floor((left + right) / 2);
            if (dryDays[mid] > target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    for (let i = 0; i < rains.length; i++) {
        let lake = rains[i];
        if (lake === 0) {
            dryDays.push(i);
        } else {
            if (lakeMap.has(lake)) {
                // filled
                let when = lakeMap.get(lake);
                let idx = binarySearch(when);
                if (idx === dryDays.length) {
                    return [];
                }
                // return smallest index of day is greater than when
                result[dryDays[idx]] = lake;
                dryDays.splice(idx, 1);
                lakeMap.set(lake, i)
            } else {
                lakeMap.set(lake, i);
            }
        }
    }
    for (const day of dryDays) {
        result[day] = 1;
    }
    return result;
};