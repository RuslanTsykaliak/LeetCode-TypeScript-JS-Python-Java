function minTime(skill: number[], mana: number[]): number {
    const wizardCount: number = skill.length;
    const potionCount: number = mana.length;

    // Precompute cumulative sum of skills
    const cumulativeSkill: number[] = Array(wizardCount);
    cumulativeSkill[0] = skill[0];

    for (let i = 1; i < wizardCount; i++) {
        cumulativeSkill[i] = cumulativeSkill[i - 1] + skill[i];
    }

    // Track the start time of the current potion at the first wizard
    let currentPotionStartTime: number = 0;

    // Iterate through potions and update their start times
    for (let j = 1; j < potionCount; j++) {
        // The constraint from the first wizard
        let minTimeDelta: number = skill[0] * mana[j - 1];

        // Check constraints from all wizardtransitions
        for (let i = 0; i < wizardCount - 1; i++) {
            // Calculate time difference required to avoid waiting
            const timeDifference: number = cumulativeSkill[i + 1] * mana[j - 1] - cumulativeSkill[i] * mana[j];

            if (timeDifference > minTimeDelta) {
                minTimeDelta = timeDifference;
            }
        }

        // Update the start time for the current potion
        currentPotionStartTime += minTimeDelta;
    }

    // The finish time is the start time of the last potion plus its total time
    const lastPotionTotalTime: number = cumulativeSkill[wizardCount - 1] * mana[potionCount - 1];

    return currentPotionStartTime + lastPotionTotalTime;
};
