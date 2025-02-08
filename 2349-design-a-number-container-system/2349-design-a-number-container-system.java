class NumberContainers {
    Map<Integer, Integer> mapIdx;
    Map<Integer, TreeSet<Integer>> mapNum;

    public NumberContainers() {
        mapIdx = new HashMap<>();
        mapNum = new HashMap<>();
    }

    public void change(int index, int number) {
        Integer oldNum = mapIdx.get(index);
        if (oldNum != null) {
            mapNum.get(oldNum).remove(index);
        }
        mapIdx.put(index, number);
        mapNum.putIfAbsent(number, new TreeSet<>());
        mapNum.get(number).add(index);
    }

    public int find(int number) {
        TreeSet<Integer> set = mapNum.get(number);
        return set == null || set.isEmpty() ? -1 : set.first();
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers obj = new NumberContainers();
 * obj.change(index,number);
 * int param_2 = obj.find(number);
 */