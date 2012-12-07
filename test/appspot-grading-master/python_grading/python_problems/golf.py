from Problem import *    

problems = {}

def test(closure):
    laser=closure['laser']
    def laser2(b):
        l='>v<^';x={'/':'^<v>','\\':'v>^<',' ':l};r=p=0
        b=b.split('\n')
        b[0]=1
        for row in b[1:]:
            r+=1
            for g in l:
                c=row.find(g)
                if-1<c:p=c+1j*r;d=g
        while' '<d:z=l.find(d);p+=1j**z;c=b[int(p.imag)][int(p.real)];d=x.get(c,' '*4)[z]
        return '#'<c
    assert(laser(r"""
    ##########
    #   / \  #
    #        #
    #   \   x#
    # >   /  #
    ########## 
    """))
    assert(not(laser(r"""
    ##########
    #   v x  #
    # /      #
    #       /#
    #   \    #
    ##########
    """)))
    assert(not(laser(r"""
    #############
    #     #     #
    # >   #     #
    #     #     #
    #     #   x #
    #     #     #
    #############
    """)))
    assert(laser(r"""
    ##########
    #/\/\/\  #
    #\\//\\\ #
    #//\/\/\\#
    #\/\/\/x^#
    ##########
"""))

problems[1] = Problem(intro="""Simulate a laser when given a maze. 
From: <a href=http://stackoverflow.com/questions/1480023/code-golf-lasers> Code Golf: Lasers </a>
<br />
Sample testcase:
<pre>
assert(laser(r""\"##########
                 #   / \  #
                 #        #
                 #   \   x#
                 # >   /  #
                 ########## ""\") == True)
</pre>
""", test=test)


"""
def laser(b):
    l='>v<^';x={'/':'^<v>','\\':'v>^<',' ':l};r=p=0
    b=b.split('\n')
    b[0]=1
    for row in b[1:]:
        r+=1
        for g in l:
            c=row.find(g)
            if-1<c:p=c+1j*r;d=g
    while' '<d:z=l.find(d);p+=1j**z;c=b[int(p.imag)][int(p.real)];d=x.get(c,' '*4)[z]
    return '#'<c
"""

