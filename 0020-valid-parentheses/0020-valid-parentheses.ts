function isValid(s: string): boolean {
    let stack: string[] = []
    let map: { [key: string]: string } = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for (let char of s) {
        if (char in map) {
            if (stack.length === 0 || stack.pop() !== map[char]) {
                return false
            }
        } else {
            stack.push(char)
        }
    }
    return stack.length === 0
};