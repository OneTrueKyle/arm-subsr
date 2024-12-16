.global _start

_start:
    MOV R0, #5       @ Load 5 into R0
    MOV R1, #10      @ Load 10 into R1
    ADD R2, R0, R1   @ R2 = R0 + R1
    @BKPT #0          @ Breakpoint to stop execution
