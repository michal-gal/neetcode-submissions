class Solution {
    public boolean hasDuplicate(int[] nums) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int num : nums)
            list.add(num);
        System.out.println(list);
        Collections.sort(list);
        System.out.println(list);
        for (int num = 0; num < list.size()-1; num++) {
            if (list.get(num).equals(list.get(num+1)))
            {
                return true;
            }
        }
        return false;
    }
}