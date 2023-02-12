def isPalindrome( s: str) -> bool:
        final=[]
        for i in s:
            if i.isalpha():
                final.append(i.lower())
        reversed=final[::-1]
        r_update="".join(x for x in reversed)
        final2="".join(x for x in final)
        if r_update==final2:
            return True
        print(reversed)
        return False

if __name__=="__main__":
    x=isPalindrome("OP")
    print(x)
