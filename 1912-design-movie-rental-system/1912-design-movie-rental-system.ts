import { PriorityQueue as PQ } from '@datastructures-js/priority-queue';

type Pair = [number, number];
type PairReport = [number, number, number];
class MovieRentingSystem {
    shopStore: Map<number, Map<number, number>>; // shop : {movie : price} (In this case we can take price in O(1))
    rentedShopMovie: Map<number, Map<number, number>>; // same logic as above but bookkeeping for rented once
    heapReport: PQ<PairReport>; //  Heap for not rented movies
    heap: Map<number, PQ<Pair>>; // Heap for rented
    constructor(shops: number, productInfo: number[][]) {
        this.shopStore = new Map();
        this.rentedShopMovie = new Map();
        this.heapReport = new PQ((a: PairReport, b: PairReport) => {
            if (a[0] !== b[0]) return a[0] - b[0];
            if (a[1] !== b[1]) return a[1] - b[1];
            return a[2] - b[2];
        }); //sort by -> price, shop, move THIS IS CRUCIAL!!!
        this.heap = new Map(); // here we need store not only PQ but movies -> to PQ to get fast access

        for (let i = 0; i < productInfo.length; i++) {
            let [shop, movie, price] = productInfo[i];
            if (!this.shopStore.has(shop)) this.shopStore.set(shop, new Map());
            if (!this.rentedShopMovie.has(shop))
                this.rentedShopMovie.set(shop, new Map());
            if (!this.heap.has(movie)) {
                this.heap.set(
                    movie,
                    new PQ((a: Pair, b: Pair) => {
                        if (a[0] !== b[0]) return a[0] - b[0];
                        return a[1] - b[1];
                    }),
                );
            }
            this.heap.get(movie)!.enqueue([price, shop]);
            this.shopStore.get(shop)!.set(movie, price);
        }
    }

    rent(shop: number, movie: number): void {
        let price = this.shopStore.get(shop)!.get(movie);
        this.shopStore.get(shop)!.delete(movie);
        this.rentedShopMovie.get(shop)!.set(movie, price!);
        this.heapReport.enqueue([price!, shop, movie]);
    }

    search(movie: number): number[] {
        const temp: Pair[] = [];
        const hashSet: Set<string> = new Set();
        const res: number[] = [];
        if (!this.heap.get(movie)) return [];
        while (temp.length < 5 && this.heap.get(movie)!.size() > 0) {
            let [price, shop] = this.heap.get(movie)!.dequeue()!;
            let key = `${shop}`;
            if (this.shopStore.get(shop)!.has(movie) && !hashSet.has(key)) {
                temp.push([price, shop]);
                hashSet.add(key);
                res.push(shop);
            }
        }
        for (let i = 0; i < temp.length; i++) {
            this.heap.get(movie)!.enqueue([...temp[i]]);
        }
        return res;
    }

    drop(shop: number, movie: number): void {
        let price = this.rentedShopMovie.get(shop)!.get(movie);
        this.rentedShopMovie.get(shop)!.delete(movie);
        this.shopStore.get(shop)!.set(movie, price!);
        this.heap.get(movie)!.enqueue([price!, shop]);
    }

    report(): number[][] {
        const temp: PairReport[] = [];
        const res: Pair[] = [];
        const hashSet: Set<string> = new Set();
        while (temp.length < 5 && this.heapReport.size() > 0) {
            let [price, shop, movie] = this.heapReport.dequeue()!;
            let key = `${shop}-${movie}`;
            if (this.rentedShopMovie.get(shop)!.has(movie) && !hashSet.has(key)) {
                temp.push([price, shop, movie]);
                hashSet.add(key);
                res.push([shop, movie]);
            }
        }
        for (let i = 0; i < temp.length; i++) {
            this.heapReport.enqueue(temp[i]);
        }
        return res;
    }
}
/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * var obj = new MovieRentingSystem(n, entries)
 * var param_1 = obj.search(movie)
 * obj.rent(shop,movie)
 * obj.drop(shop,movie)
 * var param_4 = obj.report()
 */