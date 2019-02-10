'''
关于这个算法，我简单做了一个实现，每次从数组[1, -1, 2, -2]之间随机取一个数做累加，
共累计MAX_DEPTH层，使最终的和最大，我们根据运行结果可以看到，开始-1， -2的概率比较大，
但是随着训练层数的增大，越来越小，而1，2的比例会越来越大。
'''
import sys
import math
import random

MAX_CHOICE = 4
MAX_DEPTH = 50
CHOICES = [1, -1, 2, -2]

class State(object):
    # state中除了需要记录每一步的选择，还需要记录每一步的层数round值与reward值。
    # 需要注意的是，在模拟的过程中，只有state状态的模拟和更新，
    # 更新后记录的是最终的reward状态，而树结构却没有随着模拟的进行而增加结点。
    def __init__(self):
        self.value = 0
        self.round = 0
        self.choices = []

    def new_state(self):
        choice = random.choice(CHOICES)
        state = State()
        state.value = self.value + choice
        state.round = self.round + 1
        state.choices = self.choices + [choice]

        return state

    def __repr__(self):
        return "State: {}, value: {}, choices: {}".format(
            hash(self), self.value, self.choices)

class Node(object):
    # 首先树的每个节点Node需要记录其父节点Node parent，
    # 和子节点Node children[]，用于计算UCB的这个节点的quality值和visit次数。
    def __init__(self):
        self.parent = None
        self.children = []

        self.quality = 0.0
        self.visit = 0

        self.state = None

    def add_child(self, node):
        self.children.append(node)
        node.parent = self

    def __repr__(self):
        return "Node: {}, Q/N: {}/{}, state: {}".format(
            hash(self), self.quality, self.visit, self.state)

def expand(node):

    states = [nodes.state for nodes in node.children]
    state = node.state.new_state()

    while state in states:
        state = node.state.new_state()

    child_node = Node()
    child_node.state = state
    node.add_child(child_node)

    return child_node

# 选择， 扩展
# tree_policy：选择最合适的子节点，选择策略如下：
# 1，如果当前的根节点是叶子节点，即没有子节点可以扩展，以开头下棋的例子来讲，
# 即是已经判断出了胜负或者棋盘已满的情况下，则直接返回当前节点。
# 2，如果还有没有选择过的叶子节点（下一步的某个位置的着法还没有被模拟过），
# 就在没有选择过的方法中选择一个返回。
# 3，如果所有可选择的结点都已经选择过（当前环境下所有的着法都已经试过），
# 那么往下选择UCB值最大的子节点，直到满足1或2的情况，到达叶子节点或者出现未选择过的结点。
def tree_policy(node):

    # 选择是否是叶子节点，
    while node.state.round < MAX_DEPTH:
        if len(node.children) < MAX_CHOICE:
            node = expand(node)
            return node
        else:
            node = best_child(node)

    return node

# 模拟
# default_policy：对当前情况进行模拟，直到判断出胜负。
# 策略为：输入需要扩展的结点，随机操作后 创建新的结点，
# 直到最后遇到叶子节点，得到该次模拟的reward，然后将reward返回。
def default_policy(node):
    now_state = node.state
    while now_state.round < MAX_DEPTH:
        now_state = now_state.new_state()

    return now_state.value

def backup(node, reward):

    while node != None:
        node.visit += 1
        node.quality += reward
        node = node.parent

def best_child(node):

    best_score = -sys.maxsize
    best = None

    for sub_node in node.children:

        C = 1 / math.sqrt(2.0)
        left = sub_node.quality / sub_node.visit
        right = 2.0 * math.log(node.visit) / sub_node.visit
        score = left + C * math.sqrt(right)

        if score > best_score:
            best = sub_node
            best_score = score

    return best

# 整棵树需要实现的功能则是，在一个环境下，选择出一个最有可能获胜的策略。
# 选择的方法则是通过以上介绍的四个步骤不停模拟得到每个选择的value。
# 其中，tree_policy函数实现了Selection和Expansion，
# default_poliy函数实现的是Simulation过程，backup函数是BackPropagation的实现。
def mcts(node):

    times = 5
    for i in range(times):
        expand = tree_policy(node)
        reward = default_policy(expand)
        backup(expand, reward)

    best = best_child(node)

    return best

def main():
    init_state = State()
    init_node = Node()
    init_node.state = init_state
    current_node = init_node

    for i in range(MAX_DEPTH):
        a = 0.0
        b = 0.0
        c = 0.0
        d = 0.0
        current_node = mcts(current_node)

        for j in range(len(current_node.state.choices)):
            if current_node.state.choices[j] == -2:
                a += 1
            if current_node.state.choices[j] == -1:
                b += 1
            if current_node.state.choices[j] == 1:
                c += 1
            if current_node.state.choices[j] == 2:
                d += 1
        print("-2的概率为", round(a / (i + 1.0), 2),
              "-1的概率为", round(b / (i + 1.0), 2),
              "1的概率为", round(c / (i + 1.0), 2),
              "2的概率为", round(d / (i + 1.0), 2))

if __name__ == "__main__":
    main()

