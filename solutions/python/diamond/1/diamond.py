def rows(letter):
    rows = ord(letter)-ord("A")
    htop = " "*rows + "A"
    hdiamond = [htop+htop[:-1][::-1]]
    for x in range(rows-1, -1, -1):
        hline = " "*x + chr(ord("A")+rows-x) + " "*(rows-x)
        hdiamond.append(hline+hline[:-1][::-1])
    return hdiamond + hdiamond[:-1][::-1]
    