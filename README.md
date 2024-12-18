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

### Bendras algoritmo viekimas
1. Prie src pridedamas s, taip gaunamas adresas į pirmajį baitą, kurį reikia kopijuoti į dst
2. Baitas esantis atmintyje adresu src kopijuojamas į atmintį adresu dst
3. Prie dst pridedamas vienetas, prie src pridedamas vienetas, iš n atimamas vienetas
4. Jeigu n yra nėra nulis, vykdoma nuo 2 punkto
5. Algoritmas baigtas

##### *Pastaba: konkreti implementacija* `program.s` *byloje*

# Instaliacija ir paleidimas

### Python3
Reikalavimas, instaliacija standartiška, visi moduliai nurodyti

### ./assemble.sh
Shell skriptas automatiškai kodo kompiliavimui

Instaliacijos komanda Fedora 41 (2024-12–10 atnaujinta sistema) `sudo dnf install arm-none-eabi-binutils arm-none-eabi-gcc arm-none-eabi-newlib`

### Unicorn engine
QEMU emuliatoriaus apvalkalas leidžiantis programatiškai nustatyti emuliaciją. Taip pat naudota python biblioteka 'unicorn'

Instaliacijos komanda Fedora 41 (2024-12–10 atnaujinta sistema) `sudo dnf install unicorn unicorn-devel python3-unicorn`


# Emuliatorius

Algoritmo leidimui naudojamas "Unicorn Engine" (QEMU emuliatoriaus apvalkalas). Visi nustatymai matomi leidimo programose: yra sukuriama atmintis, įrašomas algoritmo mašininis kodas, nustatomi reikiami registrai, į atmintį įkeliamas reikiama simbolių eilutė, pasibaigus algoritmo veikimui nuskaitoma išvesties simbolių eilutė esanti nurodytu adresu.

# Naudojimas

### Kompiliavimas

Programa kompiliuojama iš bylos `program.s`. Visoms kompiacijoms naudota komanda `./assemble.sh`

### Paleidimas

Emuliacjios nustatymai gali būti keičiami modifikuojant `run.py` bylą. Paleidimui naudota `python3 run.py` komanda

# Veikimo efektyvumas

Programa naudoja minimalų atminties kiekį išsaugant visas registrų vertes. 

Programa gali būti optimizuojama atliekant papildomą patikrą: Žiūrint ar kopijuojamoje simbolių eilutėje nėra simbolių eilutės baigties simbolio, tačiau tai prideda papildomą tikrinimą kiekvienam baitui, o pagerintų efektyvumą tik kai pradinė simbolių eilutė yra ženkliai trumpesnė nei pareikalauta skaityti. 

Kitas optimizavimas galėtų būti naudojant LDM instrukciją: instrukcija leidžia užkrauti duomenis į kelis registrus viena instrukcija iš nuoseklios atminties. Ši optimizacija didina algoritmo sudėtingumą. **(įgyvendintas)**


# Emuliacijos našumas

Algoritmo našumo lygis emuliatoriuje yra panašus į realioje mašinoje, nes ARM architektūros kompiutriai prilygsta (arba pranoksta "Apple silicon" atveju) daugumai modernių x86 procesorių. Gyvai patikrinti negalėjau, tačiau turint omenyje kad vykdoma JIT kompiliacija, galima nuspėti jog pirmo paleidimo metu būtų pastebimas sulėtėjimas, tačiau kartojant algoritmą vykdymo laiko skirtumas labiausiai priklausytų nuo konkrečių procesorių ir jų atminties greičio.

#  Šaltiniai

1. Wikipedia contributors. (2023, December 21). Substring. In Wikipedia, The Free Encyclopedia. Retrieved 18:33, December 18, 2024, from https://en.wikipedia.org/w/index.php?title=Substring&oldid=1190994581
<!-- todo format -->
https://developer.arm.com/documentation/ddi0403/ee/?lang=en
https://documentation-service.arm.com/static/6245c734b059dc5ff9a8bdab
GNU ARM
Unicorn engine
Unicorn engine python binding (docs)

