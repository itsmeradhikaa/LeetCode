class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # we start our right pointer from the end of the array.
        right = len(digits) - 1
        while right >= 0:
            # We add 1 to wherever index our right pointer is.
            digit = digits[right] + 1
            if digit > 9:
                # if we did a 9 + 1 = 10
                digits[right] = 0
                right -= 1
            else:
                # otherwise, we may break the loop prematurely
                # as we do not need to go any backwards
                digits[right] = digit
                break

        # If our right pointer reached the start of the array,
        # that means our array now only consists of 0s
        # in which case, we add a 1 to the start.
        if right == -1:
            digits.insert(0, 1)
        return digits