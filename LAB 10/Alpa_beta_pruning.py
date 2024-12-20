class GameNode: 
    def __init__(self, value=None, children=None): 
        self.value = value 
        self.children = children if children else [] 
 
def alpha_beta(node, depth, alpha, beta, is_maximizing): 
    if not node.children or depth == 0: 
        return node.value 
    if is_maximizing: 
        best_value = float('-inf') 
        for child in node.children: 
            value = alpha_beta(child, depth - 1, alpha, beta, False) 
            best_value = max(best_value, value) 
            alpha = max(alpha, value) 
            if beta <= alpha: 
                print(f"Pruned at MAX node with alpha={alpha}, beta={beta}") 
                break 
        node.value = best_value 
        return best_value 
    else: 
        best_value = float('inf') 
        for child in node.children: 
            value = alpha_beta(child, depth - 1, alpha, beta, True) 
            best_value = min(best_value, value) 
            beta = min(beta, value) 
            if beta <= alpha: 
                print(f"Pruned at MIN node with alpha={alpha}, beta={beta}") 
                break 
        node.value = best_value 
        return best_value 
 
def display_tree(node, level=0): 
    print("  " * level + f"Node Value: {node.value}") 
    for child in node.children: 
        display_tree(child, level + 1) 
 
if __name__ == "__main__": 
    root = GameNode(None, [ 
        GameNode(None, [ 
            GameNode(None, [GameNode(8), GameNode(7)]), 
            GameNode(None, [GameNode(12), GameNode(15)]) 
        ]), 
        GameNode(None, [ 
            GameNode(None, [GameNode(3), GameNode(2)]), 
            GameNode(None, [GameNode(25), GameNode(1)]) 
        ]) 
    ]) 
 
    print("Game Tree Before Alpha-Beta Pruning:") 
    display_tree(root) 
 
    final_value = alpha_beta(root, depth=3, alpha=float('-inf'), beta=float('inf'), is_maximizing=True) 
 
    print("\nGame Tree After Alpha-Beta Pruning:") 
    display_tree(root) 
 
    print("\nFinal Value at MAX node:", final_value)
