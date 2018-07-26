class Solution {
public:
    string addBoldTag(string s, vector<string>& dict) {
        string res = "";
        int n = s.size(), end = 0;
        vector<bool> bold(n, false);
        for (int i = 0; i < n; ++i) {
            for (string word : dict) {
                int len = word.size();
                if (i + len <= n && s.substr(i, len) == word) {
                    end = max(end, i + len);
                }
            }
            bold[i] = end > i;
        }
        for (int i = 0; i < n; ++i) {
            if (!bold[i]) {
                res.push_back(s[i]);
                continue;
            }
            int j = i;
            while (j < n && bold[j]) ++j;
            res += "<b>" + s.substr(i, j - i) + "</b>";
            i = j - 1;
        }
        return res;
    }
};