class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = [False] * 1000000

    def add(self, key: int) -> None:
        self.stack[key] = True

    def remove(self, key: int) -> None:
        self.stack[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.stack[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
'''
class MyHashSet {
    private boolean[] stack;
    /** Initialize your data structure here. */
    public MyHashSet() {
        stack = new boolean[1000000];
        Arrays.fill(stack,false);
    }
    
    public void add(int key) {
        stack[key] = true;
    }
    
    public void remove(int key) {
        stack[key] = false;
    }
    
    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        return stack[key];
    }
}
'''