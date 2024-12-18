.global substr
substr:
    @ r0 = src
    @ r1 = s
    @ r2 = n
    @ r3 = dst
    
    @ r4 - skaitomo baito adresas
    @ r5 - rašomo baito adresas
    @ r6 - ciklo skaitiklis 
    @ r7 - trumpalaikis laikiklis eilutės baigimo simboliui
    @ r7-11 - duomenų laikymo registrai

    push {r4, r5, r6, r7, r8, r9, r10, lr}   @ Išsaugomi naudojami registrai ir funkcijos grįžimo adreso registras

    add r4, r0, r1      @ r4 = src + s
    mov r5, r3          @ r5 = dst

    mov r6, r2          @ r6 saugos kiek ciklų liko

    cmp r6, #4          @ Tikriname ar pakankamai baitų greitąjam ciklui
    blt slow_loop       @ Jeigu ne praleidžiame greitąjį ciklą

fast_loop:              @ Greitojo ciklo žymė

    ldmia r4!, {r7-r10}   @ Įkrauti 4 baitus iš adminties adresu r4 į r7, r8, r9, r10 (atnaujiname r4)
    stmia r5!, {r7-r10}   @ Įrašyti registrų r7, r8, r9, r10 vertes į atmintį adresu r5 (atnaujinant r5)

    sub r6, r6, #4      @ Atiminti 4 iš baitų kopijavimui

    cmp r6, #4          @ Tikriname ar nukopijavome reikia pakankamai baitų greitąjam ciklui
    bge fast_loop       @ Jeigu užtenka tęsiame ciklą

slow_loop:
    ldrb r7, [r4], #1   @ Įkraunamas baitas esantis adresu r4 į r7 ir pridedamas 1 prie r4
    strb r7, [r5], #1   @ Baitas r7 išsaugomas adresu r3 ir prie r3 pridedamas 1

    sub r6, r6, #1      @ Atimamas 1 iš kiek liko baitų kopijavimui

    cmp r6, #0          @ Tikriname ar nukopijavome reikia baitų skaičių
    bne slow_loop       @ Jeigu r6 != 0, ciklas kartojamas

    mov r7, #0          @ Nustatyti r7 į simbolių eilutės baigimo simbolį
    strb r7, [r5]       @ Įrašyti simbolių eilutės baigimo simbolį į simbolių eilutės pabaigą

    pop {r4, r5, r6, r7, r8, r9, r10, pc} @ Restore registers and return to the caller
