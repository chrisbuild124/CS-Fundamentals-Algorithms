# Traverse a binary search tree with Morris Traversal with O(1) memory and O(1) space complexity
# This is acoomplished by creating branches between the left right'th most child back to the parent 
# Note that time will be O(n) for this problem but could be O(h) in some, and space is always O(1)
# Leetcode problem for smallest kth that uses this: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root

        while cur:
            if not cur.left:
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right
            else:
                pred = cur.left
                while pred.right and pred.right != cur:
                    pred = pred.right
                
                if not pred.right:
                    pred.right = cur
                    cur = cur.left

                else:
                    pred.right = None
                    k -= 1
                    if k == 0:
                        return cur.val
                    cur = cur.right
