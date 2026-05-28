# Larget number trick
# Sorting the string greedily but making sure each is compared specially
# rule: a before b if a+b > b+a
# Repeating strings makes their hidden cyclic pattern visible long enough 
# that normal lexicographic comparison behaves like comparing a+b vs b+a.

# Link:  https://leetcode.com/problems/largest-number/
    def largestNumber(self, nums: List[int]) -> str:
        num_strings = [str(num) for num in nums]
        num_strings.sort(key=lambda a: a * 10, reverse=True)
        if num_strings[0] == "0":
            return "0"
        return "".join(num_strings)
