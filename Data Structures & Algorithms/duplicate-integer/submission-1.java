class Solution {
    public boolean hasDuplicate(int[] nums) {
        for (int num = 0; num < nums.length; num++) {
            for (int num1 = 0; num1 < num; num1++) {
                if (nums[num1] == nums[num]) {
                    return true;
                }
            }
        }
        return false;
    }
}