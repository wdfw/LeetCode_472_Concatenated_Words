from collections import defaultdict
class Solution:
    def findAllConcatenatedWordsInADict(self, words) :
        Word = defaultdict(bool)
        words.sort(key = lambda s : len(s))
        MiniLen = len(words[0])
        res = []
        def fun(w,index,passed) :
            passed[index] = True
            if index >= len(w) : return True
            
            for i in range(index+1,len(w) + 1) :
                if w[index:i] in Word and not passed[i]: 
                    if fun(w,i,passed) : return True
                    
            if index == 0 :  Word[w] = True
            return False
        
        for w in words :
            if len(w) == MiniLen : Word[w] = True
            else : 
                if fun(w,0, [False]*(len(w)+1)) : res.append(w)
                    
        return(res)
