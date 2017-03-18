# Use to tweak time-space balance
BUCKETS = 1000000

class Solution:
    def hash(self, num):
        return abs(num) % BUCKETS

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = []

        for i in range(len(nums)):
            current = nums[i]
            delta = target - current
            delta_h = self.hash(delta)
            bucket = lookup[delta_h] if delta_h < len(lookup) else None

            if bucket is not None:
                for (key, val) in bucket:
                    if key == delta:
                        return [val, i]

            current_h = self.hash(current)
            bucket = lookup[current_h] if current_h < len(lookup) else []
            if bucket is None:
                # Bucket is within range but empty
                lookup[current_h] = [(current,i)]
            elif len(bucket) == 0:
                # Bucket is out of range
                lookup.extend([None] * (current_h-len(lookup)))
                lookup.append([(current,i)])
            else:
                # Bucket already exists
                bucket.append((current,i))

        raise Exception("There is no solution")

print(Solution().twoSum([3,2,4],6))