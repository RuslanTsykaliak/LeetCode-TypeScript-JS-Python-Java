function numberOfSubstrings(s: string): number {
    const lastIndex = { a: -1, b: -1, c: -1 };
    let count = 0;
    for (let right = 0; right < s.length; right++) {
        lastIndex[s[right] as keyof typeof lastIndex] = right;
        const minIndex = Math.min(lastIndex.a, lastIndex.b, lastIndex.c);
        count += minIndex + 1;
    };
    return count;
}