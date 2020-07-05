class Solution {
private:
    unordered_map < int, int > index;

    public:
    TreeNode * myBuildTree(const


vector < int > & preorder, const
vector < int > & inorder, int
preorder_left, int
preorder_right, int
inorder_left, int
inorder_right) {
if (preorder_left > preorder_right)
{
return nullptr;
}

// ǰ������еĵ�һ���ڵ���Ǹ��ڵ�
int
preorder_root = preorder_left;
// ����������ж�λ���ڵ�
int
inorder_root = index[preorder[preorder_root]];

// �ȰѸ��ڵ㽨������
TreeNode * root = new
TreeNode(preorder[preorder_root]);
// �õ��������еĽڵ���Ŀ
int
size_left_subtree = inorder_root - inorder_left;
// �ݹ�ع����������������ӵ����ڵ�
            // ��������С���
��߽� + 1
��ʼ��
size_left_subtree����Ԫ�ؾͶ�Ӧ����������С���
��߽�
��ʼ��
���ڵ㶨λ - 1����Ԫ��
root->left = myBuildTree(preorder, inorder, preorder_left + 1, preorder_left + size_left_subtree, inorder_left,
                         inorder_root - 1);
// �ݹ�ع����������������ӵ����ڵ�
            // ��������С���
��߽� + 1 + �������ڵ���Ŀ
��ʼ��
�ұ߽硹��Ԫ�ؾͶ�Ӧ����������С���
���ڵ㶨λ + 1
��
�ұ߽硹��Ԫ��
root->right = myBuildTree(preorder, inorder, preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1,
                          inorder_right);
return root;
}

TreeNode * buildTree(vector < int > & preorder, vector < int > & inorder) {
int
n = preorder.size();
// �����ϣӳ�䣬�������ǿ��ٶ�λ���ڵ�
for (int i = 0; i < n; ++i) {
    index[inorder[i]] = i;
}
return myBuildTree(preorder, inorder, 0, n - 1, 0, n - 1);
}
};

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:  # �ݹ���ֹ����
            return
        root = TreeNode(preorder[0])  # ����Ϊ�������ҡ������Ը���preorder����ȷ��root
        idx = inorder.index(preorder[0])  # ����Ϊ������ҡ�������root���Ի��ֳ���������
        # ����ݹ��root������������⼴��
        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return root

