import numpy as np
import math as m
import copy


class Solution:


    def first(input):
        a,a1,b,b1 = input
        #(a+a1)/(b+b1)
        #((a+a1)*(b-b1))/(b**2-b1**2)  = ~/b**2+b1**2
        res1 = (a*b+a1*b1)/(b**2+b1**2) 
        res2 = (a1*b-a*b1)/(b**2+b1**2)
        return int(res1),int(res2)


    def second(input):
        a,a1,b,b1,a0,b0 = input
        res = round((a/a1)**a0 - (b/b1)**b0,2)
        return res


    def third(input):
        x1,x2,x3,x4,x5,y1,y2 = input
        #y1,y2 - корни
        fres = [x1]
        fres.append(x1*y1+x2)
        fres.append(fres[1]*y1+x3)
        fres.append(fres[2]*y1+x4)
        sres = [x1]
        sres.append(x1*y2+fres[1])
        sres.append(sres[1]*y2+fres[2])
        disc = sres[1]**2 - 4 * sres[0] * sres[2]
        res1 = round(((-sres[1] + m.sqrt(disc)) / (2 * sres[0])))
        res2 = round(((-sres[1] - m.sqrt(disc)) / (2 * sres[0])))
        return res1,res2


    def fourth(input):
        x1,x2,x3,x4,x5,x6,y1,y2,y3,y4 = input
        fd = x1 / y1
        x1 = 0
        x2 = x2 - fd*y2
        x3 = x3 - fd*y3
        x4 = x4 - fd*y4
        fd = x2 / y1
        x3 = x3 - fd*y2
        x4 = x4 - fd*y3
        x5 = x5 - fd*y4
        fd = x3 / y1
        x4 = x4 - fd*y2
        x5 = x5 - fd*y3
        x6 = x6 - fd*y4
        return round(x4, 2), round(x5, 2), round(x6, 2)


    def fifth(input) -> list:
        x1 = input[0]
        x2 = input[1]
        x3 = input[2]
        a = input[3:12]
        b = input[12:21]
        c = input[21:30]
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)
        res = list(a*x1+b*x2+c*x3)
        return res


    def sixth(input):
        a = input[:9]
        b = input[9:18]
        c = input[18:27]
        x1 = input[-2]
        t = input[-1]
        a = Solution.get_matrix(a)
        b = Solution.get_matrix(b)
        c = Solution.get_matrix(c)
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)
        if t == 1:
            a = np.transpose(a)
        elif t == 2:
            b = np.transpose(b)
        elif t == 3:
            c = np.transpose(c)
        res = a.dot(b) + x1*c
        return [a for b in res for a in b]

    def seventh(self,input):
        a = input[:4]
        b = input[4:8]
        c = input[8:12]
        a = self.get_matrix(a,2)
        b = self.get_matrix(b,2)
        a = np.array(a)
        b = np.array(b)
        x = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        #step1
        x[0][0] =  x[0][0]*a[0][0] + x[2][0]*a[0][1]
        x[0][1] = x[0][1]*a[0][0] + x[2][1]*a[0][1]
        x[0][2] =  x[0][2]*a[0][0] + x[2][2]*a[0][1]
        x[0][3] = x[0][3]*a[0][0] + x[2][3]*a[0][1]

        x[1][0] =  x[1][0]*a[0][0] + x[3][0]*a[0][1]
        x[1][1] = x[1][1]*a[0][0] + x[3][1]*a[0][1]
        x[1][2] =  x[1][2]*a[0][0] + x[3][2]*a[0][1]
        x[1][3] = x[1][3]*a[0][0] + x[3][3]*a[0][1]

        x[2][0] =  x[0][0]*a[1][0] + x[2][0]*a[1][1]
        x[2][1] = x[0][1]*a[1][0] + x[2][1]*a[1][1]
        x[2][2] =  x[0][2]*a[1][0] + x[2][2]*a[1][1]
        x[2][3] = x[0][3]*a[1][0] + x[2][3]*a[1][1]

        x[3][0] =  x[1][0]*a[1][0] + x[3][0]*a[1][1]
        x[3][1] = x[1][1]*a[1][0] + x[3][1]*a[1][1]
        x[3][2] =  x[1][2]*a[1][0] + x[3][2]*a[1][1]
        x[3][3] = x[1][3]*a[1][0] + x[3][3]*a[1][1]

        tmp = copy.deepcopy(x)
        #step2
        x[0][0] =  tmp[0][0]*b[0][0] + tmp[1][0]*b[1][0]
        x[0][1] = tmp[0][1]*b[0][0] + tmp[1][1]*b[1][0]
        x[0][2] =  tmp[0][2]*b[0][0] + tmp[1][2]*b[1][0]
        x[0][3] = tmp[0][3]*b[0][0] + tmp[1][3]*b[1][0]

        x[1][0] =  tmp[0][0]*b[0][1] + tmp[1][0]*b[1][1]
        x[1][1] = tmp[0][1]*b[0][1] + tmp[1][1]*b[1][1]
        x[1][2] =  tmp[0][2]*b[0][1] + tmp[1][2]*b[1][1]
        x[1][3] = tmp[0][3]*b[0][1] + tmp[1][3]*b[1][1]

        x[2][0] =  tmp[2][0]*b[0][0] + tmp[3][0]*b[1][0]
        x[2][1] = tmp[2][1]*b[0][0] + tmp[3][1]*b[1][0]
        x[2][2] =  tmp[2][2]*b[0][0] + tmp[3][2]*b[1][0]
        x[2][3] = tmp[2][3]*b[0][0] + tmp[3][3]*b[1][0]

        x[3][0] =  tmp[2][0]*b[1][0] + tmp[3][0]*b[1][1]
        x[3][1] = tmp[2][1]*b[1][0] + tmp[3][1]*b[1][1]
        x[3][2] =  tmp[2][2]*b[1][0] + tmp[3][2]*b[1][1]
        x[3][3] = tmp[2][3]*b[1][0] + tmp[3][3]*b[1][1]

        res = np.linalg.solve(x,c)
        res = list(res)
        for i in range(len(res)):
            res[i] = int(res[i])
        return res


    def eight(self,input):
        matrix = input[:16]
        x,y = input[-2::1]
        matrix = self.get_matrix(matrix,4)
        matrix.pop(x)
        for i in range(3):
            matrix[i].pop(y)
        if (x + y) % 2 == 0:
            sign = 1
        else:
            sign = -1
        res = np.linalg.det(matrix)
        return int(res * sign)
        
    def nineth(self,input):
        matrix = input[:9]
        arg = input[9:]
        matrix = self.get_matrix(matrix)
        res = np.linalg.solve(matrix,arg)
        res = list(res)
        for i in range(len(res)):
            res[i] = int(res[i])
        return res


    def tenth(self,input):
        x1,x2,y1,y2,a1,a2 = input
        matrix = [y1,a1,y2,a2]
        ans = [x1,x2]
        b = self.get_matrix(matrix,2)
        res = np.linalg.solve(b,ans)
        res = list(res)
        for i in range(len(res)):
            res[i] = int(res[i])
        return res



    def get_matrix(s:list,stepen = 3) -> list[list]:
        mas = []
        index = 0
        for i in range(stepen):
            mas.append([])
            for f in range(stepen):
                mas[i].append(s[index])
                index += 1
        return mas

#print(Solution.first(-72,-48,2,-2))
#print(Solution.second(3,4,4,3,1,6))
#print(Solution.third(1,11,44,76,48,-3,-2))
#print(Solution.fourth(-4,-5,9,0,8,-3,8,-1,-7,4))
#print(Solution.fifth(4,-5,-5,[[1,-1,3],[1,0,1],[0,1,-1]],[[1,1,-1],[1,2,0],[-1,-3,0]],[[1,-1,1],[-1,2,-2],[-1,2,-1]]))
#a = Solution.get_matrix([3,-2,-3,-5,-3,3,5,-3,5],3)
#b = Solution.get_matrix([-1,0,2,2,1,1,1,0,-2],3)
#c = Solution.get_matrix([-3,-4,2,0,-4,5,5,4,-5],3)
#print(Solution.sixth(a,b,c,-1))
#print(Solution.seventh(Solution,[1,1,0,1],[1,1,1,2],[1,-2,-1,3]))
#print(Solution.eight(Solution,[1,-1,-1,-1,-1,2,2,1,0,-1,0,-1,1,0,-1,1],3,2))
#print(Solution.nineth(Solution,[1,-1,0,0,1,-1,-1,1,1],[0,0,-1]))
#print(Solution.tenth(Solution,0,4,1,-2,0,1))
#print(Solution.get_matrix([1,1,1,2,2,2,3,3,3],3))

f = open('input.txt')
input = []
for line in f:
    input.append(line.replace('\n',''))
f.close()
rinput = [[] for x in range(10)]
index = 0
for index,i in enumerate(input):
    for l in i.split():
        rinput[index].append(int(l))
    index += 1

ans = [[] for x in range(10)]

try:
    ans[0] = Solution.first(rinput[0])
except:
    ans[0] = 'что-то пошло не так...'
try:
    ans[1] = Solution.second(rinput[1])
except:
    ans[1] = 'что-то пошло не так...'
try:    
    ans[2] = Solution.third(rinput[2])
except:
    ans[2] = 'что-то пошло не так...'
try:
    ans[3] = Solution.fourth(rinput[3])
except:
    ans[3] = 'что-то пошло не так...'
try:
    ans[4] = Solution.fifth(rinput[4])
except:
    ans[4] = 'что-то пошло не так...'
try:    
    ans[5] = Solution.sixth(rinput[5])
except:
    ans[5] = 'что-то пошло не так...'
try:
    ans[6] = Solution.seventh(Solution,rinput[6])
except:
    ans[6] = 'что-то пошло не так...'
try:
    ans[7] = Solution.eight(Solution,rinput[7])
except:
    ans[7] = 'что-то пошло не так...'
try:    
    ans[8] = Solution.nineth(Solution,rinput[8])
except:
    ans[8] = 'что-то пошло не так...'
try:
    ans[9] = Solution.tenth(Solution,rinput[9])
except:
    ans[9] = 'что-то пошло не так...'

f = open('output.txt', 'w')
for i in range(10):
    f.write(str(ans[i]).replace('(','').replace(')','') + '\n')
f.close()