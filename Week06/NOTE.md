学习笔记
动态规划
分治 + 回溯 + 递归 + 动态规划

递归代码模版
public void recur(int level, int param) { 
 // terminator 
 if (level > MAX_LEVEL) { 
 // process result 
 return; 
 } 
 // process current logic 
 process(level, param); 
 // drill down 
 recur( level: level + 1, newParam); 
 // restore current status 
 
}

分治代码模板
def divide_conquer(problem, param1, param2, ...): 
# recursion terminator 
if problem is None: 
 print_result 
 return 
# prepare data 
 data = prepare_data(problem) 
 subproblems = split_problem(problem, data) 
# conquer subproblems 
 subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
 subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
 subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
… 
# process and generate the final result 
 result = process_result(subresult1, subresult2, subresult3, …) 
 
 # revert the current level states

1. 人肉递归低效、很累

2. 找到最近最简方法，将其拆解成可重复解决的问题

3. 数学归纳法思维

寻找重复性

动态规划 和 递归或者分治 没有根本上的区别（关键看有无最优的子结构） 
共性：找到重复子问题
差异性：最优子结构、中途可以淘汰次优解

1、斐波拉契数列
2、路径计算
状态转移方程（DP 方程）
opt[i , j] = opt[i + 1, j] + opt[i, j + 1]

完整逻辑：

if a[i, j] = ‘空地’: 

 opt[i , j] = opt[i + 1, j] + opt[i, j + 1]

else:

 opt[i , j] = 0

动态规划关键点
1. 最优子结构 opt[n] = best_of(opt[n-1], opt[n-2], …)

2. 储存中间状态：opt[i]

3. 递推公式（美其名曰：状态转移方程或者 DP 方程） 
Fib: opt[i] = opt[n-1] + opt[n-2] 
二维路径：opt[i,j] = opt[i+1][j] + opt[i][j+1] (且判断a[i,j]是否空地）

3、最长公共子序列
4、字符串问题

动态规划小结
1. 打破自己的思维惯性，形成机器思维

2. 理解复杂逻辑的关键

3. 也是职业进阶的要点要领

