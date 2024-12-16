from unicorn import *
from unicorn.arm_const import *
import sys

# Memory configuration
BASE_ADDR = 0x1000
MEM_SIZE = 2 * 1024 * 1024  # 2MB


# callback for tracing basic blocks
def hook_block(uc, address, size, user_data):
    print(f">>> Tracing basic block at {hex(address)}, block size = {hex(size)}")


# callback for tracing instructions
def hook_code(uc, address, size, user_data):
    print(f">>> Tracing instruction at {hex(address)}, instruction size = {hex(size)}")


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

        # Tracing all basic blocks with customized callback
        uc.hook_add(UC_HOOK_CODE, hook_code)

        # Start emulation
        uc.emu_start(BASE_ADDR, BASE_ADDR + len(binary_code))

        # Print registers
        print(">>> Emulation done. Below is the CPU context")

        r0 = uc.reg_read(UC_ARM_REG_R0)
        r1 = uc.reg_read(UC_ARM_REG_R1)
        r2 = uc.reg_read(UC_ARM_REG_R2)
        print(f">>> R0 = {hex(r0)} ({r0})")
        print(f">>> R1 = {hex(r1)} ({r1})")
        print(f">>> R2 = {hex(r2)} ({r2})")


    except UcError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    binary_file = "program.bin"
    binary_code = load_binary(binary_file)
    emulate_arm(binary_code)
