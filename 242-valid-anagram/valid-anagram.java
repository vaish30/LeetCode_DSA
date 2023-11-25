class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> map_s = new HashMap<>();
        HashMap<Character, Integer> map_t = new HashMap<>();

        char[] charArray_s = s.toCharArray();
        char[] charArray_t = t.toCharArray();

       for(int i = 0; i < charArray_s.length; i++) {
           if(map_s.get(charArray_s[i]) != null) {
            map_s.put(charArray_s[i], map_s.get(charArray_s[i]) + 1);
           } else {
               map_s.put(charArray_s[i], 1);
           }
       } 

        for(int i = 0; i < charArray_t.length; i++) {
           if(map_t.get(charArray_t[i]) != null) {
            map_t.put(charArray_t[i], map_t.get(charArray_t[i]) + 1);
           } else {
               map_t.put(charArray_t[i], 1);
           }
       } 

       if(map_s.equals(map_t)) {
           return true;
       }
       
       return false;

    }
}