class Node:
    def __init__(self,data =None,left = None,right = None) -> None:
        self.item = data
        self.left = left
        self.right = right
    
class BST:
    def __init__(self) -> None:
        self.root = None
        self.item_count = 0
    
    def insert(self,data):
        self.root = self.rinsert(self.root,data)
        self.item_count += 1
    
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        
        if data < root.item:
            root.left = self.rinsert(root.left,data)
        else:
            root.right = self.rinsert(root.right ,data)
        return root
    
    def search(self,key):
        return self.rsearch(self.root,key)
    
    def rsearch(self,root,key):
        if root is None or root.item == key:
            return root
        if key < root.item:
            return self.rsearch(root.left,key)
        else:
            return self.rsearch(root.right,key)
    
    def preorder(self):
        result = []
        self.rpreorder(self.root,result)
        return result
    
    def rpreorder(self,root,result):
        if root is None:
            return root
        result.append(root.item)
        self.rpreorder(root.left,result)
        self.rpreorder(root.right,result)
    
    def inorder(self):
        result = []
        self.rinorder(self.root,result)
        return result
    
    def rinorder(self,root,result):
        if root is None:
            return root
        self.rinorder(root.left,result)
        result.append(root.item)
        self.rinorder(root.right,result)
    
    def postorder(self):
        result = []
        self.rpostorder(self.root,result)
        return result
    
    def rpostorder(self,root,result):
        if root is None:
            return root
        self.rinorder(root.left,result)
        self.rinorder(root.right,result)
        result.append(root.item)
    
    def min_value(self,temp):
        curr = temp
        while curr.left is not None:
            curr = curr.left
        return curr.item
    
    def max_value(self,temp):
        curr = temp
        while curr.right is not None:
            curr = curr.right
        return curr.item
    
    def delete(self,data):
        self.root = self.rdelete(self.root,data)
        self.item_count -= 1
    
    def rdelete(self,root,data):
        if root is None:
            return root
        if data < root.item:
            root.left = self.rdelete(root.left,data)
        elif data > root.item:
            root.right = self.rdelete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item = self.min_value(root.right)
            root.right = self.rdelete(root.right,root.item)
        return root
    
    def size(self):
        return self.item_count
    
if __name__ == "__main__":
    bst = BST()
    bst.insert(10)
    bst.insert(20)
    bst.insert(37)
    bst.insert(1)
    bst.insert(23)
    bst.insert(65) 
    bst.delete(65)
    print(bst.inorder())
    print(bst.preorder())
    print(bst.postorder())
    
    sea = bst.search(40)
    
    print("Elements of the BST ",bst.size())
    
    if sea:
        print("Elemnet is Found")
    else:
        print("Elemnet is not Found")
        
        