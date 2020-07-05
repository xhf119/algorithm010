java
class Solution {
    public boolean lemonadeChange(int[] bills) {
        int five = 0, ten = 0;
        for (int bill: bills) {
            if (bill == 5)
                five++;
            else if (bill == 10) {
                if (five == 0) return false;
                five--;
                ten++;
            } else {
                if (five > 0 && ten > 0) {
                    five--;
                    ten--;
                } else if (five >= 3) {
                    five -= 3;
                } else {
                    return false;
                }
            }
        }

        return true;
    }
}
python
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        i=j=0
        for k in bills:
            if k==5:i+=1
            elif k==10:j+=1;i-=1
            else:
                if j==0:i-=3
                else:i-=1;j-=1
            if i<0 or j<0:return False
        return True
