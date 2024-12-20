import itertools

def evaluate_kb(Q, P, R): 
    q_imp_p = (not Q or P) 
    p_imp_not_q = (not P or not Q) 
    q_union_r = (Q or R)
    r = R 
    r_imp_p = (not R or P) 
    q_imp_r = (not Q or R) 
    return q_imp_p, p_imp_not_q, q_union_r, r, r_imp_p, q_imp_r 

def truth_table(): 
    values = [True, False] 
    print(f"{'Q':<5}{'P':<5}{'R':<5}{'Q -> P':<10}{'P -> ¬Q':<10}{'Q ∪ R':<10}{'R':<5}{'R -> P':<10}{'Q -> R':<10}") 
    for Q, P, R in itertools.product(values, repeat=3): 
        q_imp_p, p_imp_not_q, q_union_r, r, r_imp_p, q_imp_r = evaluate_kb(Q, P, R) 
        print(f"{Q:<5}{P:<5}{R:<5}{q_imp_p:<10}{p_imp_not_q:<10}{q_union_r:<10}{r:<5}{r_imp_p:<10}{q_imp_r:<10}") 

        if q_imp_p and p_imp_not_q and q_union_r: 
            print(f"\nKB is true for Q = {Q}, P = {P}, R = {R}:") 
            print(f"- Q -> P: {q_imp_p}") 
            print(f"- P -> ¬Q: {p_imp_not_q}") 
            print(f"- Q ∪ R: {q_union_r}") 
            print(f"Entailments:") 
            print(f"- R: {r}") 
            print(f"- R -> P: {r_imp_p}") 
            print(f"- Q -> R: {q_imp_r}") 
            print("-" * 50) 

def main(): 
    truth_table() 

main()
