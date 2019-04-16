class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyrowset=[set('qwertyuiopQWERTYUIOP'),set('asdfghjklASDFGHJKL'),set('zxcvbnmZXCVBNM')]
        res = []
        for word in words:
            for keywordrow in keyrowset:
                if set(word).issubset(keywordrow):
                    res.append(word)
        
        return res

a = Solution()
print(a.findWords(["Hello", "Alaska", "Dad", "Peace"]))

'''
class Solution {
    public String[] findWords(String[] words) {
        char[] a = new char[]{'q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P'};
        char[] b = new char[]{'a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L'};
        char[] c = new char[]{'z','x','c','v','b','n','m','Z','X','V','C','B','N','M'};
        Arrays.sort(a);
        Arrays.sort(b);
        Arrays.sort(c);
        ArrayList<String> list=new ArrayList<String>();
        for(int i = 0; i < words.length;i++){
                char first_char = words[i].charAt(0);
               
                if(words[i].length() ==1){
                    list.add(words[i]);
                }
                if(Arrays.binarySearch(a,first_char) >= 0){
                    for(int j =1; j< words[i].length();j++){
                        
                        if(Arrays.binarySearch(a,words[i].charAt(j))<0){
                           
                            break;
             
                        }
                        else{
                            if(j==words[i].length() -1){
                                list.add(words[i]);
                                
                            }
                        }
                    }
                    
                }
            
                if(Arrays.binarySearch(b,first_char) >= 0){
                    
                    for(int j =1; j< words[i].length();j++){
                            
                            if(Arrays.binarySearch(b,words[i].charAt(j))<0){
                                
                                break;   
                            }   
                            else{
                                if(j==words[i].length() -1){
                                    list.add(words[i]);
                                   
                                }
                            }
                        
                        }    
                    }

                 if(Arrays.binarySearch(c,first_char) >= 0){
                    for(int j =1; j< words[i].length();j++){
                        
                        if(Arrays.binarySearch(c,words[i].charAt(j))<0){
                            
                            break;
                        }
                        else{
                            if(j==words[i].length() -1){
                                
                                    list.add(words[i]);
                                    
                            }
                        }   
                    }
                   
                }
        
        }
        String[] item = list.toArray(new String[list.size()]);
        return item;
    }
}
'''