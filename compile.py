import argparse
import sys
import os



def add(count) -> str:
    return f"call void @add(i8** %ptr_ptr, i8 {count}) \n"

def sub(count) -> str:
    return f"call void @sub(i8** %ptr_ptr, i8 {count}) \n"

def lshift(count) -> str:
    return f"call i8** @lshift(i8** %ptr_ptr, i32 {count}) \n"

def rshift(count) -> str:
    return f" call i8** @rshift(i8** %ptr_ptr, i32 {count}) \n"

def get_char() -> str:
    return f"call void @input(i8** %ptr_ptr) \n"

def print_char() -> str:
    return f"call void @print_char(i8** %ptr_ptr)  \n"

def start_loop(loop_count) -> str:
    output = ""
    output += f"br label %loop_start_{loop_count}\n"
    output += f"loop_start_{loop_count}: \n"
    output += f"%ptr.{loop_count} = load i8*, i8** %ptr_ptr \n"
    output += f"%cell_value.{loop_count} = load i8, i8* %ptr.{loop_count} \n"
    output += f"%loop_cond.{loop_count} = icmp ne i8 %cell_value.{loop_count}, 0 \n"
    output += f"br i1 %loop_cond.{loop_count}, label %loop_body_{loop_count}, label %loop_end_{loop_count} \n"

    output += f"loop_body_{loop_count}: \n"
    return output

def end_loop(loop_index) -> str:
    output = f"br label %loop_start_{loop_index}\n"
    output += f"loop_end_{loop_index}:\n"
    return output
    

def main():
    parser = argparse.ArgumentParser(description="Description of your script")
    parser.add_argument('-f', type=str, help='path/to/ir/file')
    parser.add_argument('-o', type=str, help='path/to/llvm/file')
    parser.add_argument('-size', type=int, help='Size of tape')

    args = parser.parse_args()

    input_file = args.f
    output_file = args.o
    tape_size = args.size


    output_fd = open(output_file, 'w+')

    output_fd.write("""
declare void @add(i8**, i8)
declare void @sub(i8**, i8)
declare void @print_char(i8**)
declare i8** @lshift(i8**, i32)
declare i8** @rshift(i8**, i32)
declare void @input(i8**)
                    \n""")
    
    output_fd.write(f"@tape = global [{tape_size} x i8] zeroinitializer \n")
    
    output_fd.write("define i32 @main() { \n")
    output_fd.write("entry: \n")
    output_fd.write(f"%ptr = getelementptr [{tape_size} x i8], [{tape_size} x i8]* @tape, i64 0, i64 0 \n")
    output_fd.write(f"%ptr_ptr = alloca i8* \n")
    output_fd.write(f"store i8* %ptr, i8** %ptr_ptr \n") 
    
    ir = open(input_file, "r").readlines()

    ptr_count = 0
    loop_tracker = []
    loop_count = 0

    for line in ir:
        operation = line.split(":")[0]
        count = line.split(":")[1].strip()


        if operation == "+":
            output_fd.write(add(count))
        elif operation == "-":
            output_fd.write(sub(count))
        elif operation == "<":
            output_fd.write(lshift(count))
            ptr_count += 1
        elif operation == ">":
            output_fd.write(rshift(count))
            ptr_count += 1
        elif operation == ".":
            for i in range(max(int(count), 1)):
                output_fd.write(print_char())
        elif operation == ",":
            for i in range(max(int(count), 1)):
                output_fd.write(get_char())
        elif operation == "[":
           
            loop_tracker.append(loop_count)
            output_fd.write(start_loop(loop_count))
            loop_count += 1
        elif operation == "]":
            loop_i = loop_tracker.pop()
          
            output_fd.write(end_loop(loop_i))
        else:
            print("Error")

    output_fd.write("ret i32 0 \n}")
main()