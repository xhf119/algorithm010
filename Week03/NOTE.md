学习笔记

树一般都是递归（5-10行搞定）
1. 不要人肉进行递归（最大误区）

2. 找到最近最简方法，将其拆解成可重复解决的问题（重复子问题）
if else while loop 递归调用
3. 数学归纳法思维

Python 代码模板
# Python
def recursion(level, param1, param2, ...): 
    # recursion terminator  递归终结条件
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 处理当前层逻辑
    process(level, data...) 
    # drill down                     下探到下一层
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed 清理当前层

Java 代码模板
// Java
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


爬楼梯，括号，二叉搜索树

回溯 分治
power(x,n) 子集 电话号码字母组合，N皇后