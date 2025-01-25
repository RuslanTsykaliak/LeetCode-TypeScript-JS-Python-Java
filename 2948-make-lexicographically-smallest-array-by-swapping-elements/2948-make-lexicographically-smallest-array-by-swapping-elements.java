class Solution {
    public int[] lexicographicallySmallestArray(int[] nums, int limit) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->a[0]-b[0]);
        for (int i =0;i<nums.length;i++){
            pq.add(new int[]{nums[i],i});
        }
        while (!pq.isEmpty()){
            List<Integer> l = new ArrayList<>();
            List<Integer> idx  = new ArrayList<>();
            int[] ele = pq.remove();
            l.add(ele[0]);
            idx.add(ele[1]);
            while (!pq.isEmpty() && pq.peek()[0]<=ele[0]+limit){
                ele = pq.remove();
            l.add(ele[0]);
            idx.add(ele[1]);
            }
            Collections.sort(idx);
            for (int i=0;i<l.size();i++){
                nums[idx.get(i)]=l.get(i);
            }
        }
        return nums;
    }
}
