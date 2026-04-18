class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean flag=false;
        for (int num:nums)
        {
            for (int num1: nums)
            {
                if (num1==num)
                {
                    if (flag) {
                        return true;
                    }
                    else flag=true;
                }
                System.out.println(num1 + " " + num + " " + flag);
            }
            flag=false;
        }
        return (flag);
    }
}