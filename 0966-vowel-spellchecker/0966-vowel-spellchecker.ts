
const vowels = ['a', 'e', 'i', 'o', 'u'];

const checkVowelWithQuery = (word: string, query: string): boolean => {
    if (word.length !== query.length) {
        return false;
    }


    for (let i = 0; i < word.length; i++) {
        const wordLetter = word[i].toLowerCase();
        const queryLetter = query[i].toLowerCase();

        if (vowels.includes(wordLetter) && vowels.includes(queryLetter)) {
            continue;
        }
        if (wordLetter === queryLetter) {
            continue;
        }
        return false;
    }
    return true;
}

const findVowel = (wordlist: string[], query: string): string => {
    for (let i = 0; i < wordlist.length; i++) {
        const word = wordlist[i];
        if (checkVowelWithQuery(word, query)) {
            return word;
        }
    }
    return '';
}

function spellchecker(wordlist: string[], queries: string[]): string[] {
    const wordlistSet = new Set<string>(wordlist);
    const wordlistInsensitiveSet = new Set<string>(wordlist.map((word) => word.toLowerCase()));
    const result: string[] = [];
    for (let i = 0; i < queries.length; i++) {
        const currentQuery = queries[i];
        // check full match
        if (wordlistSet.has(currentQuery)) {
            result.push(currentQuery);
            continue;
        }

        // check case insensitive
        if (wordlistInsensitiveSet.has(currentQuery.toLowerCase())) {
            const insensitive = wordlist.find((word) => word.toLowerCase() === currentQuery.toLowerCase());
            insensitive && result.push(insensitive);
            continue;
        }

        // check vowels
        result.push(findVowel(wordlist, currentQuery));
    }
    return result;
};