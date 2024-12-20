from itertools import combinations

def unify(term1, term2, substitution=None):
    """Unify two terms under the given substitution."""
    if substitution is None:
        return None
    elif term1 == term2:
        return substitution
    elif isinstance(term1, str) and term1.islower():
        return unify_var(term1, term2, substitution)
    elif isinstance(term2, str) and term2.islower():
        return unify_var(term2, term1, substitution)
    elif isinstance(term1, tuple) and isinstance(term2, tuple):
        if len(term1) != len(term2):
            return None
        if term1[0] != term2[0]:
            return None
        sub = substitution.copy()
        for t1, t2 in zip(term1[1:], term2[1:]):
            sub = unify(t1, t2, sub)
            if sub is None:
                return None
        return sub
    return None

def unify_var(variable, term, substitution):
    """Unify a variable with a term under the given substitution."""
    if variable in substitution:
        return unify(substitution[variable], term, substitution)
    elif isinstance(term, str) and term in substitution:
        return unify(variable, substitution[term], substitution)
    elif occurs_check(variable, term, substitution):
        return None
    else:
        # Create a new substitution to avoid modifying the original
        new_sub = substitution.copy()
        new_sub[variable] = term
        return new_sub

def occurs_check(variable, term, substitution):
    """Check if variable occurs in term under substitution."""
    if variable == term:
        return True
    elif isinstance(term, str) and term in substitution:
        return occurs_check(variable, substitution[term], substitution)
    elif isinstance(term, tuple):
        return any(occurs_check(variable, t, substitution) for t in term[1:])
    return False

def negate_term(term):
    """Negate a term by adding or removing 'not'."""
    if isinstance(term, str):
        return ('not', term)
    elif isinstance(term, tuple) and term[0] == 'not':
        return term[1]
    else:
        return ('not',) + term

def apply_substitution(clause, substitution):
    """Apply substitution to all terms in a clause."""
    return frozenset(apply_single_substitution(term, substitution) for term in clause)

def apply_single_substitution(term, substitution):
    """Apply substitution to a single term."""
    if isinstance(term, str):
        return substitution.get(term, term)
    return tuple(substitution.get(t, t) if isinstance(t, str) else t 
                for t in term)

def resolve_clause(clause1, clause2):
    """Resolve two clauses and return the set of resolvents."""
    resolvents = set()
    for literal1 in clause1:
        for literal2 in clause2:
            # Try to unify literal1 with the negation of literal2
            substitution = unify(literal1, negate_term(literal2), {})
            if substitution is not None:
                # Create new clause by applying substitution and removing resolved literals
                new_clause1 = apply_substitution(clause1 - {literal1}, substitution)
                new_clause2 = apply_substitution(clause2 - {literal2}, substitution)
                resolvents.add(frozenset(new_clause1 | new_clause2))
    return resolvents

def resolution_proof(kb, query):
    """Attempt to prove query from knowledge base using resolution."""
    clauses = kb | {frozenset({negate_term(query)})}
    new_clauses = set()
    
    while True:
        pairs = combinations(clauses, 2)
        for (clause1, clause2) in pairs:
            resolvents = resolve_clause(clause1, clause2)
            if frozenset() in resolvents:  # Empty clause found
                return True
            new_clauses.update(resolvents)
        
        if new_clauses.issubset(clauses):  # No new clauses generated
            return False
            
        clauses |= new_clauses
        new_clauses = set()

# Example knowledge base and query
kb = {
    frozenset({('Mother', 'Leela', 'Oshin')}),
    frozenset({('Parent', 'x', 'y'), ('not', 'Mother', 'x', 'y')}),  # If Mother(x,y) then Parent(x,y)
    frozenset({('Older', 'x', 'y'), ('not', 'Parent', 'x', 'y')}),  # If Parent(x,y) then Older(x,y)
}

query = ('Older', 'Leela', 'Oshin')

result = resolution_proof(kb, query)
if result:
    print("Proved by resolution: Leela is older than Oshin.")
else:
    print("Cannot prove: Leela is older than Oshin.")
