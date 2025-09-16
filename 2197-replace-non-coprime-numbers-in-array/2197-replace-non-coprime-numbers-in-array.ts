function replaceNonCoprimes(nums: number[]): number[] {
    const stack = []
    function gcd(m, n) {
        if (m > n) return gcd(n, m)
        if (m === 0) return n
        return gcd(n % m, m)
    }


    for (const val of nums) {
        let pushMe = val
        while (stack.length) {
            const top = stack.at(-1)
            const g = gcd(top, pushMe)
            if (g === 1) {
                break
            } else {
                pushMe = top * pushMe / g
                stack.pop()
            }
        }

        stack.push(pushMe)
    }


    return stack
};