function countPalindromicSubsequence(s: string): number {
    let result = new Set();
    let records: Record<string, [number, number]> = {};

    for (let i = 0; i < s.length; i++) {
        if (s[i] in records) {
            let [start, end] = records[s[i]];
            records[s[i]] = [start, Math.max(end, i)];
        }
        else records[s[i]] = [i, 0];
    }

    for (const key in records) {
        for (let i = records[key][0] + 1; i < records[key][1]; i++) {
            result.add(key + s[i] + key)
        }
    }

    return result.size;
};