impl Solution {
    pub fn most_points(questions: Vec<Vec<i32>>) -> i64 {
        let n = questions.len();
        let mut dp = vec![0i64; n + 1]; // dp[i] = max points starting from question i

        questions.iter().enumerate().rev().fold(0, |acc, (idx, vec)| {
            let [points, brainpower] = vec[..] else { unreachable!("unexpected input format") };
            let next = n.min(idx + brainpower as usize + 1);
            let take = points as i64 + dp[next]; // Solve this question
            dp[idx] = acc.max(take); // Max between solving and skip strategies
            dp[idx]
        })
    }
}