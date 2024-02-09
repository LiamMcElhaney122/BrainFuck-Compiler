# Brainfuck LLVM Compiler

This is a Brainfuck compiler that translates Brainfuck code into LLVM Intermediate Representation (IR) and compiles it into an executable. The compiler follows a multi-stage process where Brainfuck code is first translated into a custom Intermediate Representation (IR) before being converted into LLVM IR. I was inspired by Tsoding's JIT compiler. I originally wanted to write it to compile directly into ASM, however, that would require a compiler for every architecture.

## Features

- Translates Brainfuck code into custom Intermediate Representation (IR)
- Converts custom IR into LLVM IR
- Generates executable from LLVM IR

## Getting Started

### Prerequisites

Before using the compiler, make sure you have the following installed:

- LLVM
- Python33

### Installation and use

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/brainfuck-compiler.git
   ```

2. Write your brainfuck code, or use the hello world example:

   ```bash
   cd brainfuck-compiler
   touch code.bf   
   ```
3. Compile into IR
    ```bash
    python ir.py -f code.bf -o code.ir
    ```
4. Compile into LLVM IR
    ```bash
    python compile.py -f code.ir -o main.ll
    ```
5. Compile and link into executable
    ```bash
    make && ./main
    ```

## TODO
Implement more optimization passes for generated LLVM IR
Add a linked list struct instead of a static array on the heap (dynamic resizing)
Add support for more instructions, ie * for multiply, / for divide
Add support for libc function calls and/or direct syscalls





## Acknowledgments

- Inspiration:
    https://www.youtube.com/watch?v=mbFY3Rwv7XM 
    https://llvm.org/docs/tutorial/


