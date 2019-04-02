#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (59.61%)
# Total Accepted:    475.7K
# Total Submissions: 796.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its depth = 3.
# 
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth1(self, root: TreeNode):
        self.max = 0
        if not root:
            return 0
        self.dfs(root, 0)
        return self.max+1
    def dfs(self, root, level):
        if level > self.max:
            self.max = level
        if root.left:
            self.dfs(root.left, level+1)
        if root.right:
            self.dfs(root.right, level+1)
    def maxDepth(self, root: TreeNode):
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
