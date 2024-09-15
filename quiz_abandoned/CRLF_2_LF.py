
def changeCodeceNewLine(fname):
    #fname = '1.out'
    try:
        f = open(fname,'r',encoding='big5')
        txt = f.read()
        print('big5',fname)
    except:
        f = open(fname,'r',encoding='utf-8')
        txt = f.read()
        print('utf-8',fname)
    f.close()

    #print(txt)

    f = open(fname,'wb')
    f.write(txt.encode('utf-8'))
    f.close()

if __name__=='__main__':
    import os
    files = [ s for s in os.listdir() if s.endswith('.in') or s.endswith('.out')]

    for f in files:
        changeCodeceNewLine(f)
