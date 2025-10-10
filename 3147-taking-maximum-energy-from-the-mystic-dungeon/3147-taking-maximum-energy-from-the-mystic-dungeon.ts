function maximumEnergy(energy: number[], k: number): number {
    for (let j = energy.length - k - 1; j >= 0; j--) {
        energy[j] += energy[j + k]
    }
    return Math.max(...energy)
};