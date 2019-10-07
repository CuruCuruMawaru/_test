from os import system

CTAGSFILENAME = "tags"
CTAGSCMD = "ctags --fields=+n --c-kinds=f --recurse=yes --language=c -f ./tags `pwd`".format(ctagsfile=CTAGSFILENAME)

INSERT_BEGINTAG = "func({filename}_ISEnum);"
INSERT_ENDTAG   = "func({filename}_ISEnum);func2({filename}_ISEnum);"

def InsertTags(ctagsParseData):
    def Insert(filename,ctagsData):
        with open(filename,"r") as f:
            data = f.read()
        

def CTagsParse(ctagsData):
    ret = dict()
    for i in ctagsData:
        filePath = i[1]
        if(filePath not in ret.keys()):
            ret[filePath] = []
        ret[filePath].append([i[0],i[4][i[4].rfind("line:")+1:]])
    return ret

def CTageSplit(ctagsData):
    lst = []
    for i in ctagsData:
        lst.append(i.split("\t"))
    return lst

def CTagsEraseComment(ctagsData):
    lst = []
    for i in ctagsData:
        if(i[0] != "!"):
            lst.append(i)
    return lst

def CTagsExecute():
    system(CTAGSCMD)
    with open(CTAGSFILENAME,"r") as f:
        data = f.read()
    return 

def IFBE_Main():


if __name__ == "__main__":
    IFBE_Main()

