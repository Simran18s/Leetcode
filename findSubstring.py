from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words
        word_count = Counter(words)
        
        result = []
        
        # Only need word_len starting offsets
        for i in range(word_len):
            left = i
            seen = defaultdict(int)
            count = 0
            
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]
                
                if word in word_count:
                    seen[word] += 1
                    count += 1
                    
                    # If word appears too many times, shrink window
                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    # If window size matches
                    if count == total_words:
                        result.append(left)
                else:
                    # Reset window
                    seen.clear()
                    count = 0
                    left = right + word_len
        
        return result
