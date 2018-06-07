import sys,os

def net_stats(filepath):
    nds = set()
    with open(filepath, 'r') as objF:
        cnt = 0
        for ln in objF:
            elems = ln.strip().split()
            cnt += len(elems)-1
            nds.update(elems)
    return cnt, nds

if __name__=='__main__':
    if len(sys.argv)<2:
        print 'please input filepath'
        sys.exit(1)
    cnt, nds = net_stats(sys.argv[1])       
    print cnt, len(nds)