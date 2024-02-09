# Makefile

# Compiler settings
LLVM_COMPILER = llc
C_COMPILER = clang

# Source files
SOURCE_FILES = main.ll bflib.ll

# Object files
OBJECT_FILES = $(SOURCE_FILES:.ll=.o)

# Output executable
EXECUTABLE = main

# Compile LLVM IR files (.ll) to object files (.o)
%.o: %.ll
	$(LLVM_COMPILER) -filetype=obj $< -o $@

# Default target
all: $(EXECUTABLE)

# Link object files into the final executable
$(EXECUTABLE): $(OBJECT_FILES)
	$(C_COMPILER) $(OBJECT_FILES) -o $@

# Clean up
clean:
	rm -f $(OBJECT_FILES) $(EXECUTABLE)

.PHONY: all clean
