def isPalindrome(x: int) -> bool:
        # 不用字符串，则用数学思想解
        if x < 0 or (x % 10 == 0 and x !=0 ):
            print('211')
            return False
        rem = 0
        while x > rem:
            rem = rem*10 + x%10
            x = x//10
            print(x,rem)
        return  x == rem or x == rem//10
        
#print(isPalindrome(353))

def romanToInt(self, s: str) -> int:
        num = 0
        if 'IV' in s:
            num += 4
            s = s.replace('IV','')
        if 'IX' in s:
            num += 9
            s = s.replace('IX','')
        if 'XL' in s:
            num += 40
            s = s.replace('XL','')
        if 'XC' in s:
            num += 90
            s = s.replace('XC','')
        if 'CD' in s:
            num += 400
            s = s.replace('CD','')
        if 'CM' in s:
            num += 900
            s = s.replace('CM','')
        for i in s:
            if i =='I':
                num +=1
            if i=='V':
                num +=5
            if i=='X':
                num +=10
            if i =='L':
                num+=50
            if i=='C':
                num+=100
            if i =='D':
                num+=500
            if i=='M':
                num+=1000
        return num
print()
from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
    ans = ''
    for i in list(zip(*strs)):
        if len(set(i)) == 1:
            ans += i[0]
        else:
            break
    return ans
#print(longestCommonPrefix(['sdasd','sda','sghf','ss']))
#"flower","flow","flight"



def youxiaostr(s:str)-> bool:
    if s[:3]==s[4:]:
        return True
    else:
        return False
#print(youxiaostr('[]()[]'))

def isValid(s: str) -> bool:
        #判断字符串3种括号的个数
        while s.count('()') + s.count('[]') + s.count('{}') != 0:
        #当个数不为0的时候，以此替换3种括号为空,直到字符串中不存在完整的括号时退出循环
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        #退出循环后，如果字符串不为空，则字符串包含有效的括号；反之，则包含无效（不完整）括号
        if s:
            return False
        else:
            return True
#print(isValid('[]()'))
lt=[1,2]
#print(min(lt))

def xinlist(list1=[],list2=[]) -> []:
        list3=[]
        index=0
        if min(list1) < min(list2):
            list3.append(min(list1))
            list1.pop(index)
            return list3
        else:
            list3.append(min(list2))
            list2.pop(index)
            return list3
#print(xinlist(list1=[1],list2=[0]))
#
def mergeTwoLists( list1 = [], list2 = []):
        if list1==None:
            return list2
        if list2==None:
            return list1
        head=()
        dumpy=head
        while list1 and list2:
            if list1.val<list2.val:
                dumpy.next=list1
                dumpy=dumpy.next
                list1=list1.next
            else:
                dumpy.next=list2
                dumpy=dumpy.next
                list2=list2.next
        if list1:
            dumpy.next=list1
        if list2:
            dumpy.next=list2
        return head.next   
#print(mergeTwoLists( list1 = [1,2.3], list2 = [4,5]))     


def remove(nums=[int]) -> int:
    if len(nums)==1:
        print(nums)
    
    for a in nums:
        
        while len(nums)<2:
            s=0
            if nums[s] == nums[s+1]:
                nums.pop(s)
    return nums[0]
#print(remove(nums=[0,0,0,0]))
#
def removeDuplicates( nums: List[int]) -> int:
        # 快慢指针
    if not nums:
        return 0
    fast, slow = 0, 0
    while fast < len(nums):
        if nums[fast] == nums[slow]:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
    return (slow+1)
#print(removeDuplicates( nums=[0,2,3,3,3,4,4]))


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 快慢指针
        if not nums:
            return 0
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
        return slow+1
#print(Solution.removeDuplicates(Solution(),nums=[3,2,2,3]))

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left = 0 # 左指针从0开始,指向下一个将要赋值的位置
        # 右指针从0开始,指向当前将要处理的元素
        for right in range(0, n):
            # 右指针指向的元素不等于val,是输出数组的元素
            # 将右指针指向的元素复制到左指针位置,然后将左右指针同时右移
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            # 右指针指向的元素等于val,不在输出数组里,左指针不动,右指针右移一位
        return left # left的值就是输出数组的长度
#print(Solution.removeElement(Solution(),nums=[3,2,2,3],val=3))

obj = Solution()
#print(obj.removeElement([3, 2, 2, 3], 3))

obj2 = Solution()
#print(obj2.removeElement([3, 2, 2, 3], 3))


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        
        slow = 0
        fast = 0
        while(fast < n):
            # 用来收集不等于的值，如果fast对应值不等于val, 则把它和slow替换，并让slow前进。
            if (nums[fast] != val):
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
a = Solution()
#print(a.removeElement([3,2,2,3],3))


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target in nums:
            return nums.index(target)#target是查找的对象，该方法返回查找对象的索引位置，如果没有找到对象则抛出异常。
        else:
            nums.append(target)
            nums.sort()#sort是升序函数
            return nums.index(target)
shili = Solution()
#print(shili.searchInsert( nums = [1,3,5,6], target = 2))

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitted = s.split(" ")#split可以拆分字符串，并返回分割后的字符串列表
        for i in splitted[::-1]:
            if i!="":
                return len(i)
sl = Solution()
#print(sl.lengthOfLastWord(s="   fly me  to  the moon "))


#66
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[0] == 0 and len(digits) == 1:
            digits[0] = 1
            return digits
s = Solution()
#print(s.plusOne(digits = [0]))

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i]=0
        return [1]+digits
a = Solution()
#print(a.plusOne(digits = [0,4,3,2,9]))

#67
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ashi = int(a,2)
        bshi = int(b,2)
        he = ashi + bshi
        #hezi = str(he)
        #hezi = str(he)
        heer = bin(he)[2:]
        heerzi = str(heer)
        return heerzi
s = Solution()
#print(s.addBinary(a = "1010",b = "1011"))

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0' and b != '0':
            return b
        elif a != '0' and b == '0':
            return a
        elif a == '0' and b == '0':
            return '0'
        else:
            l = max(len(a), len(b))
            result = str(int(a) + int(b))
            for i in range(l-1, -1, -1):
                if result[i] > '1':
                    if i != 0:
                        result = result[:i-1] + str(int(result[i-1:i+1])+8) + result[i+1:]
                    else:
                        result = str(int(result[i])+8) + result[i+1:]

            return result
s = Solution()
#print(s.addBinary(a = "1010",b = "1011"))
#68
class Solution:
    def mySqrt(self, x: int) -> int:
        
        if a*a == x:
            if a >= 0:
                return a
s = Solution()
#print(s.mySqrt(x = 4))


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
s = Solution()
#print(s.mySqrt(x = 16))

#70
class Solution:
    def climbStairs(self, n: int) -> int:
        s = [1,2]
        if n<3:
            return s[n-1]
        while len(s) < n:
            s.append(s[-1]+s[-2])
        return s[-1]
s = Solution()
#print(s.climbStairs(n=4))

#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        rec = head
        while head:  #or while head
            nowval = head.val
            while head.next and head.next.val == nowval:
                head.next = head.next.next
            head = head.next
        return rec
s = Solution()
#print(s.deleteDuplicates(head = [1,2,3,3]))

#88
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1 + nums2
        #print(nums1)
        nums1.sort()
        
        nums1 = nums1[n:]
        print(nums1)
        
s = Solution()
#print(s.merge(nums1=[1,2,3,0,0,0],m=3,nums2=[2,5,6],n=3))


#
class Solutio:
    def maxProfit(self, prices: List[int]) -> int:
        a = min(prices)
        index_a = prices.index(a)
        #print(index_a)
        i = index_a
        if prices[i] == prices[-1]:
            return 0
        else:
            pricecut = prices[i+1:]
            big = max(pricecut)
            result = big - prices[i]
            return result
ab = Solutio()
#print(ab.maxProfit(prices = [7,1,5,3,6,4]))

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         minprice = float('inf')
#         maxprofit = 0
#         for price in prices:
#             minprice = min(minprice, price)
#             maxprofit = max(maxprofit, price - minprice)
#         return maxprofit
# s = Solution()
#print(s.maxProfit(prices = [7,1,5,3,6,4]))


#125
class Solution:
    def isPalindrome(self, s: str) -> bool:
        xiao = s.lower()
        import re
        final = re.sub(r'[^a-zA-Z0-9]', '',xiao)
        list1 = list(final)
        list2 = list1[::-1]
        if list1 == list2:
            return True
        else:
            return False
l = Solution()
#print(l.isPalindrome(s = 'race a car'))


#136
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()#对列表nums升序排列
        ji = nums[::2]#列表中奇数位置的元素
        #print(ji)
        ou = nums[1::2]#列表中偶数位置的元素
        #print(ou)
        result = list(set(ji).difference(set(ou)))#ji中有而ou中没有的
        return result[0]
e = Solution()
#print(e.singleNumber(nums = [2,1,2]))


#141
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber:
            if columnNumber % 26 == 0:
                res += 'Z'
                columnNumber //= 26
                columnNumber -= 1
            else:
                res += chr(columnNumber%26 + ord('A') - 1)
                columnNumber //= 26
        return res[::-1]
d = Solution()
#print(d.convertToTitle(columnNumber=701))


#169
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        num = sorted(nums)
        n = len(nums)
        return num[n//2]
g = Solution()
#print(g.majorityElement(nums=[3,2,3,3]))

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = nums.sort()
        return nums[len(nums)//2]
        
g = Solution()
#print(g.majorityElement(nums=[3,3,2,3]))

class Solution:
    def reverseBits(self, n: int) -> int:
        z = str(n)
        list1 = list(z)#字符串转列表
        list1.reverse()#将列表元素倒序排列
        str1 = "".join(list1)#列表转字符串
        #print(str1)
        shi = int(str1,2)#转10进制
        print(shi)
        return shi,(str1)
t = Solution()
#print(t.reverseBits(n = '11111111111111111111111111111101'))


#191
class Solution:
    def hammingWeight(self, n: int) -> int:
        q = str(n)
        list2 = list(q)
        a={}
        for i in list2:
            a[i] = list2.count(i)       
        return a['1']
y = Solution()
#print(y.hammingWeight(n = 11111111111111111111111111111101))



#202
class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0
        while count<50:
            a1 = n%10#个位
            a2 = (int(n/10))%10#十位
            a3 = (int(n/100))%10#百位

           
            n = a1**2+a2**2+a3**2
            count += 1
            #print(n)
        return n == 1
v = Solution()
print(v.isHappy(n = 19))
