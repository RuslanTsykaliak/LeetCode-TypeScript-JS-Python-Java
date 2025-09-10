function minimumTeachings(n: number, languages: number[][], friendships: number[][]): number {
    const counts = new Map<number, Set<number>>();

    for (let i = 0; i < friendships.length; ++i) {
        const _languages = new Array(n + 1).fill(0);
        let hasIntersection = false;

        for (let j = 0; j < languages[friendships[i][0] - 1].length; ++j) {
            ++_languages[languages[friendships[i][0] - 1][j]];
        }

        for (let j = 0; j < languages[friendships[i][1] - 1].length; ++j) {
            if (_languages[languages[friendships[i][1] - 1][j]]) {
                hasIntersection = true;
                break;
            }

            ++_languages[languages[friendships[i][1] - 1][j]];
        }

        if (!hasIntersection) {
            let language;

            for (let j = 0; j < languages[friendships[i][0] - 1].length; ++j) {
                language = counts.get(languages[friendships[i][0] - 1][j]);

                if (!language) {
                    language = new Set<number>();
                    counts.set(languages[friendships[i][0] - 1][j], language);
                }

                language.add(friendships[i][1]);
            }

            for (let j = 0; j < languages[friendships[i][1] - 1].length; ++j) {
                language = counts.get(languages[friendships[i][1] - 1][j]);

                if (!language) {
                    language = new Set<number>();
                    counts.set(languages[friendships[i][1] - 1][j], language);
                }

                language.add(friendships[i][0]);
            }

            for (let j = 1; j < _languages.length; ++j) {
                if (!_languages[j]) {
                    language = counts.get(j);

                    if (!language) {
                        language = new Set<number>();
                        counts.set(j, language);
                    }

                    language.add(friendships[i][0]);
                    language.add(friendships[i][1]);
                }
            }
        }
    }

    let minimum = Infinity;

    for (let value of counts.values()) {
        if (value.size < minimum) {
            minimum = value.size;
        }
    }

    return isFinite(minimum) ? minimum : 0;
};