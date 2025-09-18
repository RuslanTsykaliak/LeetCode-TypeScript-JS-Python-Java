class XPriorityQueueTreeNode<T> {
    public constructor(
        public val: T,
        public left: XPriorityQueueTreeNode<T> | null = null,
        public right: XPriorityQueueTreeNode<T> | null = null
    ) { }
}

type XPriorityQueueComparator<T> = (a: T, b: T) => number;
type XPriorityQueueOptions<T> = {
    comparator: XPriorityQueueComparator<T>
};

class XPriorityQueue<T> {
    private readonly comparator: XPriorityQueueComparator<T>;
    private root: XPriorityQueueTreeNode<T> | null;
    private _size: number;

    public constructor(options: XPriorityQueueOptions<T>) {
        this.comparator = options.comparator;
        this.root = null;
        this._size = 0;
    }

    public size() {
        return this._size;
    }

    public enqueue(val: T): this {
        const node = new XPriorityQueueTreeNode(val);

        if (this.root === null) this.root = node;
        else this.insert(node, this.root);

        this._size++;

        return this;
    }

    public dequeue(): T | null {
        const iterator = this.inorder();

        const firstResult = iterator.next();
        const node = firstResult.done ? null : firstResult.value;

        if (node === null) return null;

        this.remove(node.val);

        return node.val;
    }

    public peek(): T | null {
        const iterator = this.inorder();
        const node: XPriorityQueueTreeNode<T> = iterator.next().value;
        return node === null ? null : node.val;
    }

    public *[Symbol.iterator]() {
        for (const node of this.inorder()) {
            yield node.val;
        }
    }

    public remove(val: T): boolean {
        const { wasRemoved, root } = this.removeFromTree(val, this.root);

        this.root = root;

        if (wasRemoved) this._size--;

        return wasRemoved;
    }

    private removeFromTree(val: T, root: XPriorityQueueTreeNode<T> | null): { wasRemoved: boolean, root: XPriorityQueueTreeNode<T> | null } {
        if (root === null) return { wasRemoved: false, root: null };

        const diff = this.compareValues(val, root.val);

        if (diff > 0) root.left = this.removeFromTree(val, root.left).root;
        else if (diff < 0) root.right = this.removeFromTree(val, root.right).root;
        else {
            if (root.left === null) return { wasRemoved: true, root: root.right };
            if (root.right === null) return { wasRemoved: true, root: root.left };

            let successor = root.right;
            while (successor !== null && successor.left !== null) successor = successor.left;

            root.val = successor!.val;
            root.right = this.removeFromTree(successor!.val, root.right).root;

            return { wasRemoved: true, root: root };
        }

        return { wasRemoved: false, root: root };
    }

    private * inorder(node = this.root): Generator<XPriorityQueueTreeNode<T>> {
        if (node === null) return;

        if (node.left !== null) yield* this.inorder(node.left);

        yield node;

        if (node.right !== null) yield* this.inorder(node.right);
    }

    private compareValues(a: T, b: T): number {
        return this.comparator(a, b);
    }

    private compareNodes(a: XPriorityQueueTreeNode<T>, b: XPriorityQueueTreeNode<T>): number {
        return this.compareValues(a.val, b.val);
    }

    private insert(node: XPriorityQueueTreeNode<T>, parent: XPriorityQueueTreeNode<T>) {
        const { left, right } = parent;
        const parentDiff = this.compareNodes(node, parent);

        if (parentDiff === 0) {
            throw new Error(`${this.constructor.name} does not accept items with equal priorities: ${node.val} vs ${parent.val}`);
        }
        if (parentDiff < 0) {
            if (right === null) parent.right = node;
            else this.insert(node, right);
        } else {
            if (left === null) parent.left = node;
            else this.insert(node, left);
        }
    }
}


type XTaskId = number;
type XUserId = number;
type XPriority = number;
type XTask = [XUserId, XTaskId, XPriority];

class TaskManager {
    private readonly queue: XPriorityQueue<XTask>;
    private readonly map: Map<XTaskId, XTask>;

    public constructor(tasks: XTask[]) {
        this.queue = new XPriorityQueue({
            comparator: (a, b) => {
                if (a[2] !== b[2]) return a[2] - b[2];
                return a[1] - b[1];
            }
        });
        this.map = new Map();

        for (const task of tasks) {
            this.add(task[0], task[1], task[2]);
        }
    }

    public add(userId: XUserId, taskId: XTaskId, priority: XPriority): void {
        const task: XTask = [userId, taskId, priority];
        this.queue.enqueue(task);
        this.map.set(taskId, task);
    }

    public edit(taskId: XTaskId, newPriority: XPriority): void {
        if (this.map.has(taskId)) {
            const [userId] = this.map.get(taskId)!;

            this.rmv(taskId);

            this.add(userId, taskId, newPriority);
        }
    }

    public rmv(taskId: XTaskId): void {
        if (this.map.has(taskId)) {
            const task = this.map.get(taskId)!;
            this.queue.remove(task);
            this.map.delete(taskId);
        }
    }

    public execTop(): XUserId {
        const next = this.queue.dequeue();
        return next === null ? -1 : next[0];
    }
}
