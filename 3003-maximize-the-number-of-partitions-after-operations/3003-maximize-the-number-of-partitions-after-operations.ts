function maxPartitionsAfterOperations(s: string, k: number): number {
    if (k === 26) {
        return 1;
    }

    const n = s.length;
    s = '@' + s + '@';
    const pref = new Array(n + 2).fill(0);
    const pval = new Array(n + 2).fill(0);

    let prefix = 0;
    let pbit = 0;

    // Calculate prefix partitions
    for (let i = 1; i <= n; i++) {
        const bit = 1 << (s.charCodeAt(i) - 'a'.charCodeAt(0));
        pbit |= bit;
        if (countBits(pbit) > k) {
            prefix++;
            pbit = bit;
        }
        pref[i] = prefix;
        pval[i] = pbit;
    }

    const suff = new Array(n + 2).fill(0);
    const sval = new Array(n + 2).fill(0);

    let suffix = 0;
    let sbit = 0;

    // Calculate suffix partitions
    for (let i = n; i >= 1; i--) {
        const bit = 1 << (s.charCodeAt(i) - 'a'.charCodeAt(0));
        sbit |= bit;
        if (countBits(sbit) > k) {
            suffix++;
            sbit = bit;
        }
        suff[i] = suffix;
        sval[i] = sbit;
    }

    let ans = 0;

    // Calculate the maximum number of partitions
    for (let i = 1; i <= n; i++) {
        let val = pref[i - 1] + suff[i + 1];
        const p = pval[i - 1];
        const s = sval[i + 1];
        const x = p | s;

        if (countBits(x) + 1 <= k) {
            val += 1;
        } else if (countBits(p) === k && countBits(s) === k && countBits(x) < 26) {
            val += 3;
        } else {
            val += 2;
        }

        ans = Math.max(val, ans);
    }

    return ans;
};

function countBits(n) {
    let count = 0;
    while (n) {
        count += n & 1;
        n >>= 1;
    }
    return count;
};
