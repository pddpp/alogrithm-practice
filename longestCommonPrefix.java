public class Solution {
    /**
     * @param strs: A list of strings
     * @return: The longest common prefix
     */
    public String longestCommonPrefix(String[] strs) {
        // write your code here
        if (strs.length == 0) {
            return "";
        }
        String currentPrefix = strs[0];
        for (int i = 0; i < strs.length; i++) {
            currentPrefix = prefixOfTwo(currentPrefix, strs[i]);
        }
        return currentPrefix;
    }

    private String prefixOfTwo(String str1, String str2){
        String result = "";
        for (int i = 0; i < Math.min(str1.length(), str2.length()); i++) {
            if (str1.charAt(i) != str2.charAt(i)) {
                return result;
            }
            result += str1.charAt(i);
        }
        return result;
    }
}
