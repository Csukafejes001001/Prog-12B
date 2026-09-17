szamok = []
for i in range(5):
    szam = int(input("Adj meg egy számot:"))
    szamok.append(szam)
    
atlag = 0.0

for szam in szamok:
    atlag += szam
    
atlag = atlag / len(szamok)
    
print(f"Átlag: {atlag}")