# 기본적인 트라이 구조에 char 대신 string 넣어서하면 된다.

import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self,key,value=None):
        self.key = key
        self.value = value
        self.children = {}

class Trie :
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head

        for char in string :
            if char not in cur_node.children :
                cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]
        cur_node.value = '\\'.join(string)

    def printAll(self):
        def pri(cur_node, i) :
            if cur_node.children == {} :
                return
            sc = sorted(list(cur_node.children)) # sorted_children
            for c in sc :
                print(i+c)
                pri(cur_node.children[c], i+' ')

        cur_node = self.head
        pri(cur_node,'')

n = int(input())
trie = Trie()
for _ in range(n):
    lis = list(input().rstrip().split('\\'))
    trie.insert(lis)

trie.printAll()