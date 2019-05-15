#assume s1<s2
class Sol:
    def add_strings(self,s1,s2):
        carry=0
        ans=''
        for i in range(1,len(s2)+1):
            if i<=len(s1):
                res=int(s1[-i])+int(s2[-i])+carry
                carry=res//10
                res=res%10
                ans+=str(res)
            else:
                res =int(s2[-i]) + carry
                carry = res // 10
                res = res % 10
                ans += str(res)
        if carry!=0:
            ans+=str(carry)
        return ans[::-1]

if __name__ == '__main__':
    p1=Sol()
    print(p1.add_strings('1','99'))
