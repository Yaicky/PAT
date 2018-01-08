# -*- coding: utf-8 -*-
__author__ = 'Yaicky'

import sys

rlt = []

class Node(object):
    def __init__(self, data=-1, lchild=None, rchild=None, parent=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild
        self.parent = parent
        self.count = 0

class BinaryTree(object):
    def __init__(self):
        self.root = Node()

    def add(self, data):
        cur_node = self.root
        # count = 0
        for n in data:
            while cur_node.count == 2:
                cur_node = cur_node.parent
            if n==0:
                # count += 1
                cur_node.count += 1
            else:
                node = Node(data=n, parent=cur_node)
                cur_node.count += 1
                if self.isEmpty():
                    self.root = node
                    self.root.parent = Node(data=-1, parent=-1)
                    cur_node = self.root
                else:
                    if cur_node.count == 1:
                        cur_node.lchild = node
                        cur_node = node
                    else:
                        cur_node.rchild = node
                        cur_node = node


            if cur_node.count == 2:
                if cur_node.parent != -1:
                    cur_node = cur_node.parent

            # print(cur_node.parent.data, cur_node.data)

    def post_order(self, start):
        node = start
        if node == None:
            return
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        rlt.append(str(node.data))

    def isEmpty(self):
        return True if self.root.data == -1 else False

all, cur = 0, 0
bTree = BinaryTree()
nums = []

# nums1 = [1,2,3,0,0,4,0,0,5,6,0,0]
# bTree.add(nums1)
# bTree.post_order(bTree.root)
for line in sys.stdin:
    if cur == 0:
        all = int(line)
        cur += 1
        continue
    else:
        op = line.split()
        if "Push" in op:
            nums.append(int(op[1]))
        else:
            nums.append(0)

    if cur == all*2:
        cur = 0
        bTree.add(nums)
        # print(nums)
        bTree.post_order(bTree.root)
        print(' '.join(rlt))

    cur += 1

'''
6
Push 1
Push 2
Push 3
Pop
Pop
Push 4
Pop
Pop
Push 5
Push 6
Pop
Pop
'''