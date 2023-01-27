from collections import defaultdict
class Solution:
    def findAllConcatenatedWordsInADict(self, words) :
        Word = defaultdict(bool)
        words.sort(key = lambda s : len(s))
        MiniLen = len(words[0])
        res = []
        def fun(w,index,passed) :

            
            if index >= len(w) : return True
            for i in range(index+1,len(w) + 1) :
                if not passed[i-1] : break
                if w[index:i] in Word : 
                    if fun(w,i,passed) : return True
                    else : passed[index-1] = False
                        
            if index == 0 :  Word[w] = True
            return False
        
        
        for w in words :
            if len(w) == MiniLen : Word[w] = True
            else : 
                a = [True]*len(w)
                if fun(w,0,a) : res.append(w)
                print(w,a)
                
        return(res)
