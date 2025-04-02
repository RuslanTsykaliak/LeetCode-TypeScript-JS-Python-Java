function maximumTripletValue(nums: number[]): number {
        let left = 0, middle = 0, res = 0

        for (const i of nums) {
            res = Math.max(res, middle * i)
            middle = Math.max(left - i, middle)
            left = Math.max(left, i)
        }
        return res
};