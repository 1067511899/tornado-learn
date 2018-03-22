    import xlrd
    
    datatmp = set()
    
    count = 0
    
    
    def addall(name):
        data = xlrd.open_workbook(name)
    
        table = data.sheet_by_index(0)
    
        for i in range(2, table.nrows):
            datatmp.add(str(table.cell(i, 0))[5:])
            
        return table.nrows - 2
    
    
    count = count + addall('d:/tmp/萝岗1.xlsx')
    count = count + addall('d:/tmp/萝岗2.xlsx')
    count = count + addall('d:/tmp/萝岗4.xlsx')
    count = count + addall('d:/tmp/萝岗5.xlsx')
    count = count + addall('d:/tmp/萝岗6.xlsx')
    count = count + addall('d:/tmp/萝岗7.xlsx')
    count = count + addall('d:/tmp/萝岗8.xlsx')
    count = count + addall('d:/tmp/萝岗9.xlsx')
    count = count + addall('d:/tmp/萝岗10.xlsx')
    print(len(datatmp))
    print(count)
    
