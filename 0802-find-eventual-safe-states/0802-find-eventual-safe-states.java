class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        List<List<Integer>> adj=new ArrayList<>();
         
         for (int i = 0; i < graph.length; i++) {
            adj.add(new ArrayList<>());
            for (int j : graph[i]) {
                adj.get(i).add(j);
            }
        }
        List<Integer> list=new ArrayList<>();
           boolean visited[]=new boolean[graph.length];
                       boolean inVisited[]=new boolean[graph.length];

        for(int i=0;i<graph.length;i++){
            if(!dfs(i,adj,visited,inVisited)){
                list.add(i);
            }
        }
        return list;
    }
    public boolean dfs(int i,List<List<Integer>> adj,boolean visited[],boolean inVisited[]){
        inVisited[i]=true;
        visited[i]=true;
        for(int j:adj.get(i)){
            if(!visited[j] && dfs(j,adj,visited,inVisited)){
                return true;
            }
            if(inVisited[j]){
                return true;
            }
        }
        inVisited[i]=false;
        return false;
        
    }
}