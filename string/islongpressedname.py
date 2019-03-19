class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)

'''
class Solution {
    public boolean isLongPressedName(String name, String typed) {
        int i = 0;
        for(int j = 0; j<typed.length();++j){
            if(i<name.length() && name.charAt(i)==typed.charAt(j)){
                i++;
            }
            else if(j == 0 || typed.charAt(j)!= typed.charAt(j-1)){
                return false;
            }
        }    
        return i == name.length();    
    }
}
'''