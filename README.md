# Įvadas
### Funckija
    Substr: algoritmo tikslas yra iš nudrodytos simbolių eilutės nukopijuotį nurodytą dalį simbolių į kitą nurodytą simbolių eilutę. 

### Įvestis, išvestis ir rezultatai
    Funkcijos veikimui būtini 4 argumentai su prielaidomis:
    1. Kopijuojamų baitų skaičius (toliau n). Daroma prielaida, kad skaičius yra didesnis už nulį, kitaip funkcija yra beprasmė - 
    2. Nuo kelinto baito reikia kopijuoti duomenis (toliau s). Daroma prielaida, kad skaičius yra teigiamas, nes simbolių eilutės duomenys išdestomi baituose sekančiuose pradžios adresu esantį baitą
    3. Simbolių eilutės pradžios adresas iš kurios bus kopijuojami duomenys (toliau src). Daroma prielaida, kad simbolių eilutės duomenų talpa baitais yra bent 'n + s'
    4. Simbolių eilutės pradžios adresas į kurią bus kopijuojami duomenys (toliau dst). Daroma prielaida, kad simbolių eilutės duomenų talpa baitais yra bent 'n + 1', tam kad galima būtų sutalpinti duomenis ir simbolių eilutės pabaigos žėnklą
    Funkcija negražina jokių argumentų, tačiau tikimasi, kad bus šalutinis efektas: dts bus nukopijuoti nurodyti baitai iš src

### Algoritmo viekimas
    1. Prie src pridedamas s, taip gaunamas adresas į pirmajį baitą, kurį reikia kopijuoti į dst
    2. Baitas esantis atmintyje adresu src kopijuojamas į atmintį adresu dst
    3. Prie dst pridedamas vienetas, prie src pridedamas vienetas, iš n atimamas vienetas
    4. Jeigu n yra nėra nulis, vykdoma nuo 2 punkto
    5. Algoritmas baigtas


#  Šaltiniai

1. Wikipedia contributors. (2023, December 21). Substring. In Wikipedia, The Free Encyclopedia. Retrieved 18:33, December 18, 2024, from https://en.wikipedia.org/w/index.php?title=Substring&oldid=1190994581
<!-- todo format -->
GNU ARM
Unicorn engine
Unicorn engine python binding (docs)

