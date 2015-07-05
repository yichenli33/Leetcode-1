'''
http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=135449&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26sortid%3D311

1. 两个链表 求最大的公共后缀
'''

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_max_postfix(head1, head2):
    if not head1 or not head2: return None
    head1 = reverse_linkedlist(head1)
    head2 = reverse_linkedlist(head2)
    dummy = ListNode(0)
    result = dummy

    while head1 and head2:
        if head1.value == head2.value:
            tmp = head1.next  # Note bug here, we need to save the tmp, otherwise, head1.next will become None ! 
            result.next = head1
            result = result.next
            result.next = None 
            
            head1 = tmp
            head2 = head2.next
        else:
            break
    
    return dummy.next
    
def reverse_linkedlist(head1):
    pre = None
    cur = head1
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur 
        cur = next
    return pre

def print_list(head):
    while head:
        print "head.val: ", head.value
        head = head.next 


'''
2. permutations of a list without adjacent equal elements
'''

import collections
import heapq

def permutation_number(s):
    counts = collections.Counter(s)
    heap = [(-count, key) for key, count in counts.items()]
    heapq.heapify(heap)
    output = []
    last = None
    while heap:
        minuscount1, key1 = heapq.heappop(heap)
        if key1 != last or not heap:
            last = key1
            minuscount1 += 1
        else:
            minuscount2, key2 = heapq.heappop(heap)
            last = key2
            minuscount2 += 1
            if minuscount2 != 0:
                heapq.heappush(heap, (minuscount2, key2))
        output.append(last)
        if minuscount1 != 0:
            heapq.heappush(heap, (minuscount1, key1))
    return ''.join(output)

test1 = 'aaabbbccc'
test2 = 'aaaaaaaabbbddd'
print permutation_number(test1)
print permutation_number(test2)


# Best Reference: http://stackoverflow.com/questions/25285792/generate-all-permutations-of-a-list-without-adjacent-equal-elements

'''
3. find h index element in the array, at least n elements in the arrary larger than n, but here is no n+1 elements larger than n+1
'''
def find_h_index(arr):
    n = len(arr) - 1
    start = 0; end = n
    distance = 0
    while start <= end:
        if end % 2 == 0:
            mid = (start + end) / 2
        else:
            mid = (start + end) / 2 + 1
        
        if arr[mid] >= (n - mid):
            distance = n - mid
            end = mid - 1
        
        elif arr[mid] < (n - mid):
            start = mid + 1
            
    return distance

test1 = [0,3,4,7,8,9,10]
test2 = [0,3,4,7,8,9]
test3 = [1]

print find_h_index(test1)
print find_h_index(test2)
print find_h_index(test3)

'''
具体思路如下，其实就是binary search。 首先根据start和end得出mid，看A[mid]值是否大于数组长度减去mid
(假设A.length-mid = distance），如果是那么distance有可能成为h index. 因为数组有序，如果distance小于A[mid]，
那么有distance个元素的值大于distance。 此时如果A[mid]值小于distance，那么继续向高位找，start=mid+1。
如果A[mid]值大于distance，那么继续向低位找end=mid-1。如果低位找到更大的distance，那么返回低位的，
如果低位没找到更大的，就返回现在的distance。
'''




'''
4. 给一个数，要求把这个数分解成一些平方数的和，并且要求使用最短的平方数list 如 13 = 9 + 4 而不是 13 = 4+4+4+1
'''
def min_square(n):
    dp = [0 for i in xrange(n + 1)]
    dp[0] = 0; dp[1] = 1
    
    for i in xrange(2, n+1):
        res = 1<<31 - 1
        for j in xrange(1, i):
            if j * j  > i:
                break
            else:
                res = min(res, dp[i - j*j] + 1)
        dp[i] = res
        print "dp[%d]: %d" %(i, dp[i])
    return dp[n]

n = 12
print min_square(n)


'''
第二问本质上是个DP题。思路如下，要求和为n的最小平方数序列，先求出和为1到n-1的最小平方数序列。然后从1到n的平方根之间寻找和为（n-i*i）的数的最短平方序列。1<i<sqrt(n)
例如求和为12的最短的平方 序列 
f（12） = 3*3 + f（3） f（3） = 1 + 1 + 1  i = 3 结果为 12 = 9 + 1 + 1 + 1
f（12）=  2*2+ f( 8 )   f( 8 ) = 4 + 4   i = 2 结果为 12 = 4 + 4 + 4
f（12） = 1*1 + f（11） f（11）= 9+1+1 结果为 12 = 9 + 1 + 1 + 1
最后正确结果为 12 = 4 + 4 + 4
'''

# http://www.mitbbs.com/article_t/JobHunting/32966491.html
'''
5. 一种encoding只有1 byte encode或者两byte encode两种形式，如果说第一byte的第一
个bit是0，那么这个bit开始的这个byte encode一个字符；如果第一个byte的第一位是
1，那么他一定是两个byte encode一个字符，并且他的第二个byte的首bit可以是1或者
0. 题目要求，给你一串encode，请问最后一个字符是一个byte encode的还是两个byte
encode的。不允许顺序parse bit串。
'''


// 末字节high bit为1，是非法单字节编码，所以必然是双字节编码
if (lastByte & 0x80 != 0) return DoubleByteEncoding;

// 末第二字节high bit为0，不带末字节混，所以末字节肯定是单字节编码
if (last2ndByte & 0x80 == 0) return SingleByteEncoding;

// 末字节high bit为0，末二字节high bit为1的情况，不能确定，需要检查末第三
if (last3rdByte & 0x80 == 0)
    return DoubleByteEncoding; // 末第3个高位0，不带末第2混，所以倒数2和1是
双字节码

if (last4thByte & 0x80 == 0) //末4不带末3混，末3和末2组成双字节，最末一个单了
    return SingleByteEncoding;
    
到此为止，不用再继续推理了，可以总结规律了：

if (n == 1) return 1;

// 末高位1，必然是双字节编码
if (bytes[n-1] & 0x80 != 0) return 2;
// 末高位0，需要倒着扫描
else {
    for (int i = n - 2; i --; i >= 0) {
      // 看到0，就可以确定答案了，因为0必然是一个编码序列的结尾，后面是11...
110
      // n - 1 - i是这个11...110的串的长度，如果是奇数，那么末字节单溜
      if (bytes[i] & 0x80 == 0)
         return 2 - (n - 1 - i) % 2;
      // 到了第1个字节，并且高位是1，那么11...110串的长度是n - i，包括当前字节
      if (i == 0)
         return 2 - (n - i) % 2;

      // else, 当前是字节高位是1，继续倒扫，直到看到0，或者扫描完
    }
}

'''
6. 题目： Given a rectangular grid of colored pixels and a particular 
pixel in the grid, find the perimeter of the same-colored blob containing that pixel.
补充一下，因为是求包含所给像素的图形的周长，所以就是DFS到每个相同颜色的邻接像素，然后检查这个像素周围四个像素的颜色，
如果颜色不同或者越界了，周长+1，否则就继续DFS到那个像素。最后得到周长

说是像素其实就是一个一个边长为1的正方形小格子，每个格子有一个颜色，所以就是从给定格子出发做DFS，直到抵达一个在边缘的格子
（也就是说这个格子周围四个方向有一个方向颜色不同或者越界），有几个边满足条件就加几
'''

def find_pixel(grid, pixel):
        if not grid or not grid[0]: return 0
        perimeter = [0]

        for i in xrange(len(grid)):
                for j in xrange(len(grid[0])):
                        if grid[i][j] == pixel:
                            find_pixel_helper(grid, pixel, i, j, perimeter) 
        return perimeter[0]

def find_pixel_helper(grid, pixel, x, y, perimeter):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != pixel:
                perimeter[0] += 1
                if x >= 0 and x < len(grid) and y>= 0 and y < len(grid[0]) and grid[x][y] == 'D':
                    perimeter[0] -= 1
                return
        grid[x] = grid[x][:y] + 'D' + grid[x][y+1:]  
        
        find_pixel_helper(grid, pixel, x+1, y, perimeter)
        find_pixel_helper(grid, pixel, x-1, y, perimeter)
        find_pixel_helper(grid, pixel, x, y+1, perimeter)
        find_pixel_helper(grid, pixel, x, y-1, perimeter)

grid = ['01100','00011','00011','01110','00000']
#grid = ['01100','00011']
print find_pixel(grid, '1')

'''
7. Median in stream data
'''

* [Median in Stream Data](https://github.com/UmassJin/Leetcode/blob/master/Experience/Median_in_stream_data.py)



'''
CTCI: from random5 to get random7
'''

import random

def rand5():
    return random.randint(0,4)

def rand7():
    num = 5 * rand5() + rand5()
    print num
    if num < 21:
        return num % 7

print rand7()


'''
8. Google Interview
from random2 to get random6
'''

# 思路:这道题的核心是保证产生random的概率一样，比如random7，则每个数字0到6产生的概率都为1/7,
# 对于random5来说，我们通过5*random5 + random5产生数字 0到24，然后取最小的3*7=21，所以取20
# 再mod7, 这里我们可以将random2先产生random4，然后通过random4产生

import random

def rand2():
    return random.randint(0,1)

def rand6():
    rand4 = 2*rand2() + rand2() 
    num = 4 * rand4 + rand4 # 0 to 9
    if num < 12:
        return num % 6

print rand6()

'''
9. 让你设计个matrix class，提供两个方法：update(x, y) & query(x1, y1, x2, y2)，update方法是update matrix上一个cell的值，
query方法是查询matrix上用(x1, y1)和(x2, y2)确定的矩形内所有值的总和。
有三种scenario，
第一种是update方法调用的次数远大于query方法的调用次数，
第二种是query方法的调用次数远大于update方法的调用次数，
第三种是两种方法调用次数一样多。
'''
'''
分析：
第一种情况，因为update次数多，那就不用对matrix做任何预处理，这样update是O(1)，query是O(N^2)。
第二种情况，因为query次数多，那就预处理一下matrix，新建一个辅助二维数组dp,使得dp[y][x]等于以(0,0)和(x,y)
两点确定的矩阵内的值的总和。这样update是O(N^2), query是O(1)
第三种情况，我们可以改变辅助二维数组dp的构成，使得dp[y][x]等于(0,y)到(x,y)的所有值的和，这样update是O(N)，query也是O(N)

这里可以考虑用segment tree(http://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/)
'''

'''
10. 题目是给一个string,一个set of string, 问string里面是否包含一个substring，使得这个substring的任意一个prefix + suffix能
组合成set里面的任意一个string，能就返回true，否则返回false
是这样，我少说了个条件，输入除了一个string和一个set of string,还有个整形变量len表示set里面每个string的长度（
也就是说set里的string长度都是一样的）。比如input string is "whoisyourdaddy", input set 包含两个 string "whu" and "ddy"，
那么function应该返回true，因为给的input string里面的substring "whoisyou" 的 prefix "wh" 和 suffix "u" 组成了 "whu"，
而另一个substring "daddy" or "ddy" 的 prefix "d" 和 suffix "dy" 组成了 "ddy"，因此这个例子里set里面所有的string都可以在
input string里面找到一个substring的一个prefix+suffix组合构成。
'''


'''
11. 给一个List，里面存着一些一个双向链表上的结点，这个List里面所有在双向链表上邻接的结点组成一个strong component，
求List里strong component的个数

给你个双向链表 1 <-> 2 <-> 4 <-> 7 <-> 9 <-> 11
给你个List里面有1,2,7,9,11, 那么 1,2组成一个strong component，7,9,11组成一个strong component。
解法就是建个HashSet然后把List里面的结点全丢进去，遍历一遍double linked List，遇到一个在HashSet里面的结点就从这个结点开始把所有
能到的在List里面的邻接结点从HashSet里面删掉，count++。换言之就是简易版的图遍历。
'''
class DoubleList_Node:
    def __init__(self, val = 0, pre = None, inext = None):
        self.val = val
        self.pre = pre
        self.next = inext

class Solution:
    def find_strong_comp(self, nodelist):
        if not nodelist: return []
        idict = { node.val: node for node in nodelist}
        count = 0

        for node in nodelist:
            if idict and (node.val in idict):
                tmp_pre = node.pre
                tmp_next = node.next
                while tmp_pre and (tmp_pre.val in idict):
                    del idict[tmp_pre.val]
                    tmp_pre = tmp_pre.pre
                while tmp_next and (tmp_next.val in idict):
                    del idict[tmp_next.val]
                    tmp_next = tmp_next.next
                del idict[node.val]
                count += 1
            elif not idict:
                break
        return count 
    
'''
test:
node1 = DoubleList_Node(2)
node2 = DoubleList_Node(3)
node3 = DoubleList_Node(5)
node4 = DoubleList_Node(7)
node5 = DoubleList_Node(9)
node6 = DoubleList_Node(8)
node7 = DoubleList_Node(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node2.pre = node1
node3.pre = node2
node4.pre = node3
node5.pre = node4
node6.pre = node5
node7.pre = node6

l = [node2, node1, node5, node4, node6, node7]
test = Solution()
print test.find_strong_comp(l)
'''


'''
12.
实现linux的diff命令，我就好好的问清楚了她期望的输入和输出，然后用java开始写，期间写遍历文件系统的function的时候一时半会想不起来java里相关的API了，
就跟妹子问咋办，妹子说不要求非要死记硬背API，你自己想想有什么API比较make sense的在白板上注明一下就行了，我正好这段时间上班就是写python干类似的事，
就一股脑把python的相关API在白板上注明出来，然后接着写代码。。写完后又大概跟妹子提了提如果给的路径下如果有symbolic link该怎么处理，妹子表示很满意。。
follow-up是怎么判断两个文件内容是否相同，文件太大怎么优化。.

第三题主要思路就是遍历两个输入路径，把路径树中的所有叶子结点找到（包括file和empty folder），把对应的相对路径拿出来放进对应的两个set里，
然后就是同时遍历两个set，找第一个set里没有的而第二个set里有的（+），以及第一个set里有的而第二个set里没有的（-），遇到相对路径相同的file
就转化为绝对路径读file content用md5算下hash value，比较看看内容是否一致。
'''


'''
13. 设计一个SparseVector class，包含set(long idx, int val), get(long idx), dotProduct(SparseVector otherVec)三个方法
'''


'''
14. 有一排数量无限的object，每个object有两个状态，可以用true和false来表示，object的状态是可切换的，初始情况下所有object的状态都是false。
让你设计一个class，实现两个方法：isToggled(long idx), toggle(long start, long end)。这题没记错的话之前面经里也出现过。我最后给出的方法是
维护一个list of intervals, 每次执行toggle时都要新加入一个新interval，然后把这个新interval merge进已有的interval list里面，这个解法的问题
在于实现起来非常复杂，因为做merge操作时你需要反转所有和新interval重叠的interval的状态，最后才把新interval里不重叠的部分加进list里面。最后
代码也没写完，但是写到中间我突然想起来之前看到一个面经里的比较类似的题，可以只记录每个object的toggle操作的次数，最后根据操作次数的奇偶来
判断object的状态，如此一来就不需要实际记录状态，只需要维护一个balanced interval tree，每次toggle就把新interval加进tree里，执行isToggled(long idx)时
计算所有包含给定idx的interval的数量就能决定对应的object的状态了。跟面试官提了提这个做法，面试官表示这就是他的解法，但是他觉得我给的解法也不错，
查询的复杂度要比他的方法低，就是难实现

不，面试官就是期待我提出这样的解法，他也说了如果写对应的代码的话不需要实现balanced interval tree，假设有这么个现成的数据结构给你用就行了。
因为interval tree不难写，但是balanced的就没那么好写了。。

https://github.com/UmassJin/Leetcode/blob/master/Algorithm/Segment_Tree.md

'''

'''
15. 设计一个random queue，支持push，pop，要求pop是random的
follow-up，每次push的时候会有相应的权重，要求pop按照权重random，换句话说，push 1,2,3，相应的权重1,2,3。那第一次pop需要保证1被pop的概率是1/6，
以此类推。有一个类似b+ tree的结构能解决follow-up。
'''

'''
16. 第二轮，偏向c++功底跟concurrency。实现memcopy，还有就是实现一个银行的类里面的几个算法，都很简单，但是对多线程调用的加锁需要有了解。
最后又问了一个实现每次调用，运行5秒，期间不停循环自增的简单算法，follow-up是如何应对系统管理员尴尬地恰巧在这段时间内改了系统时间。
'''


# http://www.1point3acres.com/bbs/thread-137081-1-1.html
'''
17. 
UTF8 validation
http://codereview.stackexchange.com/questions/59428/validating-utf-8-byte-array

0xxxxxxx  single byte
10xxxxxx  continous byte
110xxxxx  2 bytes sequence
1110xxxx  3 bytes sequence
11110xxx  4 bytes sequence
111110xx  5 bytes sequence
1111110x  6 bytes sequence
11111110  7 bytes sequence
11111111  8 bytes sequence
Valid    0xxxxxxx
Valid    110xxxxx 10xxxxxx
Valid    1110xxxx 10xxxxxx 10xxxxxx. 
Valid    0xxxxxxx 110xxxxx 10xxxxxx 0xxxxxxx
invalid  10xxxxxx
invalid  110xxxxx 0xxxxxxx 10xxxxxx
invalid  110xxxxx
'''

def validUTF8(data):
    if not data: return False
    
    size = 0
    for c in data:
        if size == 0 and c >> 7 == 0b0:
            continue
        elif size == 0:
            if c >> 5 == 0b110: size = 1
            elif c >> 4 == 0b1110: size = 2
            elif c >> 3 == 0b11110: size = 3
            elif c >> 2 == 0b111110: size = 4
            elif c >> 1 == 0b1111110: size = 5
            else:
                return False
        else:
            if (c >> 6) != 0b10:
                return False
            size -= 1
    return size == 0

data1 = [0b00000000] # T
data2 = [0b11011111,0b10000000] # T
data3 = [0b11011111,0b10000000,0b11000000] # F
data4 = [0b11011111,0b00000000, 0b10111111] # F
data5 = [0b00000000, 0b00011111, 0b11110111, 0b10111111,0b10111111] #F
data6 = [0b00000000, 0b00011111, 0b11110111, 0b10111111,0b10111111, 0b10000000] #T
print validUTF8(data1)
print validUTF8(data2)
print validUTF8(data3)
print validUTF8(data4)
print validUTF8(data5)
print validUTF8(data6)

# wiki: https://en.wikipedia.org/wiki/UTF-8#Description
# Reference: http://codereview.stackexchange.com/questions/59428/validating-utf-8-byte-array
# http://www.fgdsb.com/2015/01/10/valid-utf8/


'''
18.
Symetric rotation number boolean checkNum(String num)
ex: 16891 旋轉 180 以後還是 180 確認這個數有沒有符合這個規則
Follow Up: List<String> genNum(int len)

產生所有這個長度以下的所有組合
ex: len=3, {0,1,8,00,11,88,69,96,000,010,080,101,111,181,808,818,888,609,619,689,906,916,986}
'''

def rotation_number(number):
    if not number: return False
    idict = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
    n = len(number)
    left = 0; right = n - 1

    while left <= right:
        if number[left] not in idict or \
                number[right] not in idict:
                    return False
        if idict[number[left]] != number[right]:
            return False
        left += 1
        right -= 1
    return True


number1 = '8'
number2 = '7'
number3 = '609'
number4 = '321'
number5 = '916'
print rotation_number(number1)
print rotation_number(number2)
print rotation_number(number3)
print rotation_number(number4)
print rotation_number(number5)

'''
19. Followup question

思路：
奇数: 0, 1, 8
偶数：00, 11, 88, 69, 96
奇数：000, 010, 080, 101, 111, 181, 808, 818, 888, 609, 619, 689.....
偶数：0000, 0110, 0880, 0690, 0960, 1001, 1111, 1881, 1691, 1961, 8008, 8118, 8888, ......

奇数可以通过偶数加0, 1, 8 得到
偶数则可以通过加上00, 11, 88, 69, 96得到
'''
def find_rotate_number(n):
    if n < 1: return []
    res = []; pre = ['']
    list1 = ["0", "1", "8"]
    idict = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
    i = 1
    while i < n + 1:
        cur = []
        if i % 2 == 1:
            if pre == ['']:
                cur = list1
            else:
                for num in pre:
                    for digit in list1:
                        index = len(num)/2
                        newnum = num[:index] + digit + num[index:]
                        cur.append(newnum)
        elif i % 2 == 0:
            for num in pre:
                for digit in idict:
                    newnum = digit + num + idict[digit]
                    cur.append(newnum)
            pre = cur
        res.extend(cur)
        i += 1
    return res

print find_rotate_number(4)



'''
20. The pattern could be across the given set of strings.
只要他給的 pattern 在連續的 strings 可以組合起來成為 pattern string, return true-google 1point3acres

ex:
pattern: "horse"
strings: ["ah", "or", "settle"]

boolean contains(String pattern, Iterable<String> strs)
pattern: "abc"
strs : "ab", "cd"  -> true
strs : "aa", "bcd" -> true
strs : "ab", "ac"  -> false
'''


'''
Leetcode: count islands
-google 1point3acres
後面的 follow up 都是討論而已, 沒寫 code
Follow up: 如果是大地圖怎麼處理, 要你切 map, 考慮每個 submap 之間的關係. visit 1point3acres.com for more.
Follow up2: 平行化處理, 這個條件, 可能會讓你前面所想方法要重新思考

這時剩下15分鐘, 他就說再來個 follow up 好了 = =, 跟大圖無關, 一樣是 count island, 假設已經做了第一次的處理
Follow up3: 如果他現在要新增島到地圖上, 請回傳最新的 count
ex: int add(int x, int y), the function should return the new count

Follow up3.1 這個 function 能不能做到比 O(N*N) 還要好? (N為 map 邊長)

最後結束的時候, 他有跟我說解法, 就是當初在 count islands 的時候把每個 island 都建成一顆 tree
所以再判斷新加上去的 island 周圍的時候, 只要判斷周圍的 island 是不是有 common ancestor O(lgN)
如果是分開的兩個島, 現在被新的島串起來了的話, 就將兩顆 tree 接起來就好

思路[转发]：
本帖最后由 stellari 于 2015-6-29 20:44 编辑


今天在Lintcode上刷到Number of Islands II这道题，发现恰好和前两天面经版的一个Youtube面试出现的题的follow up是相同的。在网上简单搜了一下并没有看到关于这道题的详细解法，所以自己写了一个，分享给大家。

原题是这样的：

----------------------
Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there in the matrix after each operator.

Example 

Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].

return [1,1,2,2].

Note 

0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent
复制代码

大意就是在一个由grid组成的海洋上，每次将一个方格从海洋改变成陆地。在每次完成这个操作后，都要得到此时的岛屿数目。
--------------------

这实际上就是要动态维护一个图的Connected Component。这是并查集(Union-find set)的典型应用。所谓并查集，就是满足下列特征的数据结构：

1. 能表示一组不相交的集合，比如{{1, 2, 3}, {4, 5}, {6}, {7}}；
2. 最少支持以下三个操作:
    make-set(v): 加入一个新的集合，其中只有一个元素v。
    find(v): 给定元素v，查询v在哪一个集合当中。
    union(v1, v2): 给定元素v1和v2，将它们所在的集合合并为一个。

并查集通常用树形结构来表示。每一个集合是一棵多叉树，所以一组不相交集合构成了一个“forest”。比如{{1, 2, 3}, {4, 5}, {6}, {7}}这组不相交集合，可以用四棵树来表示:
   
   1           4       6         7
  / \         / 
  2   3      5
复制代码
其中每棵树的root可以是这个集合中的任意元素（一般是第一个加入该集合的元素）。其他元素都是root的子node，或子node的子node……等等。

我们可以用root来代表集合本身。这样，当给定树中的任何一个节点，我们就希望能够快速地找到这个节点所在的集合，也就是树的root。所以，每个节点必须储存它的parent节点。但是反过来，我们不需要在已知root的情况下，查找树中的一个节点，所以并不需要储存child节点。也就是说，并查集树和普通的树恰好相反。

这样的话，find函数就很容易写了
find(v)
  while (v is not root) 
        v = v->parent
  return v
复制代码
至于union函数，我们可以先找到两个节点所在的树的root，然后把较浅的树插入到较深的树中去。这样做的原因是希望得到的树能尽量平衡。为此，我们在每个节点中保存“以这个节点为root的树的深度”。如果树中只有root一个元素时，深度为0。

综合上述讨论，并查集树节点定义如下：
struct DJSetNode{
  int rank;
  DJSetNode* parent;
  DJSetNode(int r, DJSetNode* parent): 
        rank(r), parent(p) 
  {}
};
复制代码
这里的rank就是深度。之所以不叫“depth”，是因为以后我们可以对上述的并查集实现做进一步优化，称为Path Compression（本文不作讨论）。在作完这步优化以后，这个rank就和深度不对应了。

union函数可以实现如下：
union(v1, v2)
  root1 = find(v1)
  root2 = find(v2)
  if (root1 is root2) 
    return root1
  if (root1 has lower rank) 
    root2.parent = root1
    return root1
  else if (root2 has lower rank)
    root1.parent = root2
    return root2
  else // root1 and root2 have same depth
    root2.parent = root1
    root1.rank ++
    return root1
复制代码
----------------

在本题当中，我们可以将创建一个M x N的数组SEAMAP，类型为DJSetNode*。每次将一个坐标点(i, j)位置设为陆地时，我们做3件事：

1. 创建一个新的DJSetNode对象N
2. 将N作为一棵孤立的树插入到forest当中
3. 让SEAMAP[i, j]指向N

然后，我们查询SEAMAP[i, j]的四个邻位置。如果其中某些位置的值不为NULL，那么说明这里已经存在有岛屿，那么我们将N与那些位置所在的集合合并即可。对于四个邻位置，我们最多只要进行四次union操作即可。合并完成之后，forest中剩余的孤立树的个数即为孤立岛屿的个数。

由于并查集树都是平衡树，所以find和union都有O(logn)复杂度（其中n为岛屿位置的个数）。也就是说每添加一块岛屿，都仅需要O(logn)时间。

------------------
代码如下:
struct DJSetNode {
    int label;  // 保留字。本程序中并未用到。
    int rank;   // 在本程序中就是树的深度。
    DJSetNode* parent;
    DJSetNode(int lb, int r, DJSetNode* p): label(lb), rank(r), parent(p) {}
};
class Solution {
    unordered_set<DJSetNode*> forest;   // 包含当前所有树的根
    
    // MAKESET: 产生一个仅含一个元素的set，并将其作为一棵树加入forest
    DJSetNode* makeSet() {
        DJSetNode* cur = new DJSetNode(0, 0, nullptr);    
        forest.insert(cur);
        return cur;
    }

    // FIND: 给定任意一个元素，找到这个元素所在树的root
    DJSetNode* find(DJSetNode* n) {
        if (n == nullptr) return nullptr;
        while (n->parent) {
            n = n->parent;
        }
        return n;
    }

    // MERGE: 给定两个元素，合并这两个元素所在的树，并返回合并后树的root
    DJSetNode* merge(DJSetNode* n1, DJSetNode* n2) {
        DJSetNode* r1 = find(n1);   // 分别找到两元素所在的树的root
        DJSetNode* r2 = find(n2);
        if (r1 == r2) {             // 如果本来就在同一树，则不做任何事
            return r1;
        }

        if (r1->rank > r2->rank) {  // 如果树1的“深度”大于树2，
            r2->parent = r1;        // 则以树1为基础合并
            forest.erase(r2);       // 然后从forest中除去树2
            return r1;              // 这是为了保证合并后树的深度尽可能小
        }
        else if (r1->rank < r2->rank) { // 反之则以树2为基础合并，
            r1->parent = r2;
            forest.erase(r1);
            return r2;
        }
        else {                      // 若深度相同，则任选一树为基础合并
            r2->parent = r1;        // 此处选为树1
            forest.erase(r2);
            r1->rank++;             // 合并以后，树1的深度增加了1
            return r1;
        }
    }

    int add(const Point& p) {
        vector<DJSetNode*> nbs;     
        // 查看当前位置的四个邻点，如果为island，则将其加入队列
        if (p.x > 0 && seaMap[p.y][p.x-1]) nbs.push_back(seaMap[p.y][p.x-1]);
        if (p.y > 0 && seaMap[p.y-1][p.x]) nbs.push_back(seaMap[p.y-1][p.x]);
        if (p.x < NC-1 && seaMap[p.y][p.x+1]) nbs.push_back(seaMap[p.y][p.x+1]);
        if (p.y < NR-1 && seaMap[p.y+1][p.x]) nbs.push_back(seaMap[p.y+1][p.x]);

        DJSetNode* cur = makeSet(); // 先把当前加入的点看做一个新的孤立岛屿。
        seaMap[p.y][p.x] = cur;     // 

        for (int i = 0; i < nbs.size();++i) {
            cur = merge(cur, nbs[i]);   // 将这个岛屿分别与周围的邻岛合并
        }
        return forest.size();       // 此时forest中的tree数就是孤立岛屿的数目
    }
public:
    vector<vector<DJSetNode*> > seaMap;
    int NR, NC;
    vector<int> numIslands2(int n, int m, vector<Point>& operators) {
        seaMap = vector<vector<DJSetNode*> >(m, vector<DJSetNode*>(n, nullptr));
        NR = m, NC = n;

        vector<int> res;
        // 
        for (int i = 0; i < operators.size(); ++i) {
            int a = add(operators[i]);
            res.push_back(a);
        }
        return res;
    }
};
复制代码
------------------------------



# http://www.1point3acres.com/bbs/thread-137081-1-1.html
# http://www.1point3acres.com/bbs/thread-137243-1-1.html
'''
