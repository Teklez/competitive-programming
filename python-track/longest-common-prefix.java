class Solution {

    public static String longestCommonPrefix(String[] strs) {
        String common = "";
        Arrays.sort(strs);
        int counter;
        if( strs[0].length() > strs[strs.length-1].length()){
            counter = strs[strs.length - 1].length();

        }
        else
            counter = strs[0].length();
        System.out.println("counter: " + counter );


        for(int i=0;i<counter;i++){
            if (strs[0].charAt(i) == strs[strs.length-1].charAt(i))
                common +=strs[0].charAt(i);
            else
                break;
        }
        if(common == "")
            return "";
        System.out.println("common: " + common);
        int slicer = common.length();
        for(String s:strs){
            String slice = s.substring(0,slicer);
            if (!slice.equals(common)){
                return "";
            }
        }
        return common;

    }
}