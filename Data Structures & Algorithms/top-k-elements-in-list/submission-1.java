class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        if (nums.length == 1 && k == 1) {
            return nums;
        } 

        Map<Integer, Integer> counter = new HashMap<>();

        for (int num : nums) {
            if (counter.containsKey(num)) {
                counter.put(num, counter.get(num) + 1);
            } else {
                counter.put(num, 1);
            }
        }

        int[] freq = new int[k];
        for (int i = 0; i < k; i++) {
            int highest = -1;
            int mostFreq = -1;
            for (Map.Entry<Integer, Integer> entry: counter.entrySet()) {
                int key = entry.getKey();
                int v = entry.getValue();
                if (v > highest) {
                    highest = v;
                    mostFreq = key;
                }
            }
            counter.remove(mostFreq);
            freq[i] = mostFreq;
        }

        return freq;
    }
}
