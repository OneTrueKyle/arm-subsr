from unicorn import *
from unicorn.arm_const import *
import sys


# DATA CONFIGURATION
INPUT = b"abcABC123"
FROM = 3
COUNT = 3


# Memory configuration
BASE_ADDR = 0x1000
STACK_ADDR = 2 * 1024 * 1024 + 0x1000       # Stack segment base address (arbitrary high address)
STACK_SIZE = 0x10000                        # 64 KB stack size

IN_ADDR = 0x1100
OUT_ADDR = IN_ADDR + len(INPUT)

MEM_SIZE = 2 * 1024 * 1024  # 2MB

def load_binary(file_path):
    try:
        with open(file_path, "rb") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)


def emulate_arm(binary_code):
    try:
        # Initialize Unicorn emulator in ARM mode
        uc = Uc(UC_ARCH_ARM, UC_MODE_ARM)

        # Map memory for code
        uc.mem_map(BASE_ADDR, MEM_SIZE)

        # Map memory for the stack
        uc.mem_map(STACK_ADDR, STACK_SIZE)

        # Write binary code to memory
        uc.mem_write(BASE_ADDR, binary_code)


        # Set the program counter (PC) to the start address
        uc.reg_write(UC_ARM_REG_PC, BASE_ADDR)

        # Set lr to the end of the emulation
        uc.reg_write(UC_ARM_REG_LR, BASE_ADDR + len(binary_code))

        # Set the Stack Pointer (SP) to the top of the stack
        uc.reg_write(UC_ARM_REG_SP, STACK_ADDR + STACK_SIZE)


        # Write input string to memory
        uc.mem_write(IN_ADDR, INPUT)

        # Set registers to required state
        uc.reg_write(UC_ARM_REG_R0, IN_ADDR)
        uc.reg_write(UC_ARM_REG_R1, FROM)
        uc.reg_write(UC_ARM_REG_R2, COUNT)
        uc.reg_write(UC_ARM_REG_R3, OUT_ADDR)
        
        
        # Start emulation
        uc.emu_start(BASE_ADDR, BASE_ADDR + len(binary_code))

        # Print results
        print(">>> Emulation done.")

        # TODO print out + in memory
        output = uc.mem_read(OUT_ADDR, COUNT + 1)
        print(output)


    except UcError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    binary_file = "program.bin"
    binary_code = load_binary(binary_file)
    emulate_arm(binary_code)
