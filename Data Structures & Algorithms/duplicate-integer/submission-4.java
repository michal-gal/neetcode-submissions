class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> zbior = new HashSet<>();
        for (int num : nums) {
            if (zbior.contains(num))
                return true;
            else zbior.add(num);
            }
        return false;
    }
}