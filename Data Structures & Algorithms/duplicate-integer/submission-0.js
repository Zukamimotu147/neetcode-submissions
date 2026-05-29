class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const hashset = new Set();

        for (let i = 0; i < nums.length; i++) {
            if (hashset.has(nums[i])) {
                return true;
            } else {
                hashset.add(nums[i])
            }
        }
        return false;
    }
}
