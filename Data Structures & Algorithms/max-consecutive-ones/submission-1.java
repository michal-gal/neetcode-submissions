class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int wynik_temp = 0;
        int wynik = 0;
        for (int num : nums) {
            if (num == 1) {
                wynik_temp++;
            } else if (wynik_temp > wynik){
                wynik = wynik_temp;
                wynik_temp = 0;
            }
            else wynik_temp = 0;
            System.out.println("wynik: "+ wynik + ", temp: " + wynik_temp);
        }
        if (wynik_temp > wynik){
            wynik = wynik_temp;
        }
        return wynik;
    }
}