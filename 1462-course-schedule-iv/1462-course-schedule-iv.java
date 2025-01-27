class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prereqs, int[][] queries) {
        HashMap<Integer, HashSet<Integer>> map = new HashMap<Integer, HashSet<Integer>>();
        HashMap<Integer, HashSet<Integer>> rev = new HashMap<Integer, HashSet<Integer>>();

        IntStream.range(0, numCourses).forEach(i -> map.put(i, new HashSet()));
        IntStream.range(0, numCourses).forEach(i -> rev.put(i, new HashSet()));

        for(int i = prereqs.length -1; i > -1; i--) {
            var p = prereqs[i];
            var list = map.get(p[0]);
            var two = map.get(p[1]);
            two.addAll(list);
            two.add(p[0]);

            list = rev.get(p[1]);
            var one = rev.get(p[0]);
            one.addAll(list);
            one.add(p[1]);
        }

        for(int[] p: prereqs) {
            var list = map.get(p[0]);
            var two = map.get(p[1]);
            two.addAll(list);
            two.add(p[0]);

            list = rev.get(p[1]);
            var one = rev.get(p[0]);
            one.addAll(list);
            one.add(p[1]);
        }

        

        List<Boolean> res = new ArrayList<Boolean>();

        for(int i = 0; i < queries.length; i++) {
            var p = queries[i];
            var x = new HashSet<>(map.get(p[1]));
            x.retainAll(rev.get(p[0]));
            res.add(!x.isEmpty() || map.get(p[1]).contains(p[0]) || rev.get(p[0]).contains(p[1]));
        }

        return res;
    }
}