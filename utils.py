class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return repr(f'Value: {self.val}, Next: {self.next}')


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(f'Value: {self.val}, Left: {self.left}, Right: {self.right}')
