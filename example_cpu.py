import sys

# op codes, this is what you would give a programmer as "documentation"
PRINT_JONATHAN = 1
HALT = 2
PRINT_NUM = 3
SAVE = 4
PRINT_REGISTER = 5
ADD = 6
POP = 7
PUSH = 8

# sample programs that prints jonathans
print_jonathan_program = [
    PRINT_JONATHAN,
    PRINT_JONATHAN,
    PRINT_JONATHAN,
    PRINT_JONATHAN,
    HALT,
]

# sample program that prints some numbers
print_some_nums = [
    PRINT_NUM,
    15,
    PRINT_NUM,
    15,
    PRINT_NUM,
    37,
    PRINT_JONATHAN,
    HALT,
]

# sample program that saves and prints numbers from registers
save_num_to_reg = [
    SAVE,   # SAVE, VAL, REG_NUM
    65,
    2,
    PRINT_REGISTER,
    2,
    SAVE,   # SAVE, VAL, REG_NUM
    13558929,
    6,
    PRINT_REGISTER,
    2,
    PRINT_REGISTER,
    6,
    HALT
]

# sample program that adds two register values together
add_numbers = [
    SAVE,   # SAVE number 12 to reg 1
    12,
    1,
    SAVE,   # SAVE number 45 to reg 2
    45,
    2,
    ADD,  # Reg1 += Reg2 ( we add the two values in the two registers, and
    # store the result in the first register )
    1,
    2,
    PRINT_REGISTER,
    1,
    SAVE,
    10,
    2,
    ADD,
    1,
    2,
    PRINT_REGISTER,
    1,
    HALT,
]

# this is where we "initialize the memory"
memory = [0] * 256
# memory = add_numbers
# memory = save_num_to_reg

# Read from file and load into memory
# read the filename from command line arguments
# open the file, and load each line into memory
# lets try not to crash


def load_program_into_memory():
    # reset the memory first
    # memory = [] use global instead of local memory var here
    address = 0
    # get the filename from arguments here
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Need proper file name passed!")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as f:
        for line in f:
            # print(line)
            if line == '':
                continue
            comment_split = line.split('#')
            # print(comment_split) # [everything before #, everything after #]
            num = comment_split[0].strip()

            memory[address] = int(num)
            address += 1


# ALL THE CODE BELOW IS THE "COMPUTER"
running = True
pc = 0
registers = [0] * 8
SP = 7  # register location that holds top of stack address
# store the top of memory into Register 7
registers[SP] = len(memory) - 1


load_program_into_memory()
# running = False

while running:
    # lets receive some instructions, and execute them
    command = memory[pc]

    # if command is PRINT_JONATHAN
    if command == PRINT_JONATHAN:
        # print out jonathan's name
        print('Jonathan!')
        pc += 1

    # if command is HALT
    elif command == HALT:
        running = False
        pc += 1
        # shutdown

    elif command == PRINT_NUM:
        # look at the next line in memory
        # print the number thats in that spot
        num = memory[pc + 1]
        print(num)
        pc += 2

    elif command == SAVE:
        # we expect to see two numbers after the instruction
        # number to save, and register location
        num_to_save = memory[pc + 1]
        register = memory[pc + 2]
        registers[register] = num_to_save
        pc += 3

    elif command == PRINT_REGISTER:
        # we expect to see one number after the instruction
        # number of register location
        register = memory[pc + 1]
        print(registers[register])
        pc += 2

    elif command == ADD:
        # we expect to see two numbers after the instruction
        # both register locations
        # we will save the result into the first register given to us
        register1 = memory[pc + 1]
        register2 = memory[pc + 2]
        val1 = registers[register1]
        val2 = registers[register2]
        registers[register1] = val1 + val2
        pc += 3
    elif command == PUSH:
        # PUSH Register value to the stack
        register = memory[pc + 1]
        # decrement the Stack Pointer (SP)
        registers[SP] -= 1
        # read the next value for register location
        register_value = registers[register]
        # take the value in that register and add to stack
        memory[registers[SP]] = register_value
        pc += 2
    elif command == POP:
        # POP (register value)
        # POP value off stack at location SP
        value = memory[registers[SP]]
        register = memory[pc + 1]
        # store the value in register given
        registers[register] = value
        # increment the Stack Pointer (SP)
        registers[SP] += 1
        pc += 2
    else:
        # if command is unrecognizable
        print(f"Unknown instruction {command}")
        sys.exit(1)


# ram = [0] * 256

# def ram_read(self, mar):
#     return
