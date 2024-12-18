.global _start
_start:
    @ r0 = src
    @ r1 = s
    @ r2 = n
    @ r3 = dst
    
    @ r4 - skaitomo baito adresas
    @ r5 - rašomo baito adresas
    @ r6 - ciklo skaitiklis 
    @ r7 - trumpalaikis laikiklis eilutės baigimo simboliui


    push {r4, r5, r6, r7, lr}   @ Išsaugomi naudojami registrai ir funkcijos grįžimo adreso registras

    add r4, r0, r1      @ r4 = src + s
    mov r5, r3          @ r5 = dst

    mov r6, r2          @ r6 saugos kiek ciklų liko

copy_loop:          @ Ciklo žymė

    ldrb r7, [r4], #1   @ Įkraunamas baitas esantis adresu r4 į r7 ir pridedamas 1 prie r4
    strb r7, [r5], #1   @ Baitas r7 išsaugomas adresu r3 ir prie r3 pridedamas 1

    sub r6, r6, #1      @ Atimamas 1 iš kiek liko baitų kopijavimui

    cmp r6, #0          @ Tikriname ar nukopijavome reikia baitų skaičių
    bne copy_loop       @ Jeigu r5 == r2, ciklas kartojamas

    mov r7, #0          @ Nustatyti r6 į simbolių eilutės baigimo simbolį
    strb r7, [r5]       @ Įrašyti simbolių eilutės baigimo simbolį į simbolių eilutės pabaigą

    pop {r4, r5, r6, r7, pc} @ Atkuriami registrai ir programos skaitiklio registras nustatomas į grįžimo adresą
