# gather.py
# gather list items in equal length  tuples
def gather(lst, glen):
    """ Gather list elements into
    tuples
    :lst: list
    :glen: group length
    """
    glist = []
    g = []
    for le in lst:
        g.append(le)
        if len(g) == glen:
            glist.append(tuple(g))
            g = []
    if len(g) > 0:
        glist.append(tuple(g))  # Add shortened
    return glist

if __name__ == "__main__":
    llen = 20
    xl = list(range(llen))
    for glen in range(1, llen+2):        
        lsgrps = gather(xl, glen)
        print(f"glen:{glen}: lsgrps{lsgrps}")
              