# Constraint Propagation AC3

def AC3(csp, queue=None):
    
    if queue == None:
        queue = list(csp.binary_constraints)

    while queue:

        (xi, xj) = queue.pop(0)

        if remove_inconsistent_values(csp, xi, xj):
            if len(csp.choices[xi]) == 0:
                return False
            for neighbor in csp.siblingsp[xi]:
                if neighbor != xi:
                    queue.append((neighbor,xi))

def remove_inconsistent_values(csp, xi, xj):
    
    removed = False

    for pick in csp.choices[xi]:
        