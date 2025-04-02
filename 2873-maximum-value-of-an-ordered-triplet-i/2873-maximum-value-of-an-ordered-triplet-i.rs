impl Solution {
  pub fn maximum_triplet_value(nums: Vec<i32>) -> i64 {
    let n = nums.len();
    let (mut max_arr, mut res) = (vec![-1; n], 0);
    max_arr[n - 1] = nums[n - 1];
    for i in (0 .. n - 1).rev() {
      max_arr[i] = max_arr[i + 1].max(nums[i]);
    }
    
    let mut max_v = nums[0];
    for i in 1 .. n - 1 {
      res = res.max(((max_v - nums[i]) as i64) * (max_arr[i + 1]) as i64);
      max_v = max_v.max(nums[i]);
    }
    
    return res;
  }
}