function maxFreqSum(s: string): number {
    const isVowel = (c) => {
        return c === "a" || c === "e" || c === "i" || c === "o" || c === "u";
    };

    const mp: { [key: string]: number } = {};
    for (const ch of s) {
        mp[ch] = (mp[ch] || 0) + 1;
    }

    let vowel = 0, consonant = 0;
    for (let ch = "a".charCodeAt(0); ch <= "z".charCodeAt(0); ch++) {
        const char = String.fromCharCode(ch);
        const count = mp[char] || 0;
        if (isVowel(char)) {
            vowel = Math.max(vowel, count);
        } else {
            consonant = Math.max(consonant, count);
        }
    }
    return vowel + consonant;
};