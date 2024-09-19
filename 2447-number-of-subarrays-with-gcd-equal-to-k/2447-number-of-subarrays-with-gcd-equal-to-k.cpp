class Solution {
public:
    int subarrayGCD(vector<int>& nums, int k) {
        int ans = 0;
        int temp = 0;
        int i, j;
        int n = nums.size();
        
        for(i = 0; i < n; i++){
            temp = nums[i];
            for(j = i; j < n; j++){
                temp = __gcd(temp, nums[j]);

                if(temp == k){
                    ans++;
                }
                
            }
        }

        return ans;
    }
};