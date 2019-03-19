'''
class Solution {
    public int compareVersion(String version1, String version2) {
        String[] version1list = version1.split("\\.");
        String[] version2list = version2.split("\\.");
        int i = 0;
        while(i < version1list.length && i < version2list.length){
            int num1 = Integer.parseInt(version1list[i]);
            int num2 = Integer.parseInt(version2list[i]);
            if(num1>num2){
                return 1;
            }
            else if(num1 < num2){
                return -1;
            }
            else{
                i++;
            }
        }
        if(i == version1list.length && i ==version2list.length){
            return 0;
        }
        else if(i == version1list.length){
            while(i<version2list.length){
                int num2 = Integer.parseInt(version2list[i]);
                if(num2 != 0){
                    return -1;
                }
                else{
                    i++;
                }
            }
            return 0;
        }
        else{
            while(i<version1list.length){
                int num1 = Integer.parseInt(version1list[i]);
                if(num1 != 0){
                    return 1;
                }
                else{
                    i++;
                }
            }
            return 0;
        }
    }
}
'''