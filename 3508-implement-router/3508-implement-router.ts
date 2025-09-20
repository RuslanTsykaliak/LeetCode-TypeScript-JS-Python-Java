class Router {
    private memoryLimit: number;
    private packets: Set<string>; // track dupes
    private queue: Queue<number[]>; // @datastructures-js/queue
    private timestamps: Record<string, number[]>; // track timestamps by destination
    private removedCount: Record<string, number>; // track number removed for getCount efficiency 

    constructor(memoryLimit: number) {
        this.memoryLimit = memoryLimit;
        this.packets = new Set();
        this.queue = new Queue();
        this.timestamps = {};
        this.removedCount = {};
    }

    private removePacket(): number[] {
        const packet = this.queue.dequeue();
        if (!packet) {
            return [];
        }
        const [source, destination, timestamp] = packet;
        const hash = `${source}:${destination}:${timestamp}`;
        this.packets.delete(hash);
        if (!this.removedCount[destination]) {
            this.removedCount[destination] = 1;
        } else {
            this.removedCount[destination] += 1;
        }
        return packet;
    }

    addPacket(source: number, destination: number, timestamp: number): boolean {
        const hash = `${source}:${destination}:${timestamp}`;
        if (this.packets.has(hash)) {
            return false;
        }
        this.queue.enqueue([source, destination, timestamp]);
        this.packets.add(hash);
        if (!this.timestamps[destination]) {
            this.timestamps[destination] = [];
        }
        this.timestamps[destination].push(timestamp);
        if (this.queue.size() > this.memoryLimit) {
            this.removePacket();
        }
        return true;
    }

    forwardPacket(): number[] {
        return this.removePacket();
    }

    getCount(destination: number, startTime: number, endTime: number): number {
        let count = 0;
        const timestamps = this.timestamps[destination];
        if (!timestamps) {
            return 0;
        }
        const removed = this.removedCount[destination] || 0;
        const l = this.getLowerBound(timestamps, startTime, removed);
        const r = this.getUpperBound(timestamps, endTime, removed);
        return r - l;
    }

    private getLowerBound(timestamps: number[], startTime: number, removed: number) {
        let l = removed;
        let r = timestamps.length;
        while (l < r) {
            const mid = Math.floor((l + r) / 2);
            if (timestamps[mid] < startTime) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l;
    }

    private getUpperBound(timestamps: number[], endTime: number, removed: number) {
        let l = removed;
        let r = timestamps.length;
        while (l < r) {
            const mid = Math.floor((l + r) / 2);
            if (timestamps[mid] <= endTime) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l;
    }
}
