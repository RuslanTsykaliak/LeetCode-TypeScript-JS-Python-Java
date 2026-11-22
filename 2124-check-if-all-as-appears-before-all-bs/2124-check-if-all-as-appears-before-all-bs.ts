function checkString(s: string): boolean {
    for (let a = 1; a < s.length; a++) {
        if (s[a - 1] == "b" && s[a] == "a") {
            return false;
        }
    }
    return true;
};