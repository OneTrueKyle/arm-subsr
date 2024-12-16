from unicorn import *
from unicorn.arm_const import *
import sys

# Memory configuration
BASE_ADDR = 0x1000

IN_BUF = 0x1020
OUT_BUF = 0X1040
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

        # Write binary code to memory
        uc.mem_write(BASE_ADDR, binary_code)

        # Set the program counter (PC) to the start address
        uc.reg_write(UC_ARM_REG_PC, BASE_ADDR)

        # Start emulation
        uc.emu_start(BASE_ADDR, BASE_ADDR + len(binary_code))

        # Print results
        print(">>> Emulation done.")

        # TODO print out + in memory


    except UcError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    binary_file = "program.bin"
    binary_code = load_binary(binary_file)
    emulate_arm(binary_code)
