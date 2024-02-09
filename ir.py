import argparse
import sys
import os



def main():
    # Create an argument parser object
    parser = argparse.ArgumentParser(description="Description of your script")

    # Define arguments
    parser.add_argument('-f', type=str, help='path/to/file')
    parser.add_argument('-o', type=str, help='path/to/file')
    

    # Parse the command-line arguments
    args = parser.parse_args()

    file_path = args.f
    output = args.o


    if not os.path.exists(file_path):
        sys.stderr.write(f"The file {file_path} could not be found at the specified path!" + "\n")
        return 0
    file = open(output, "w")
    output = parse(file_path)
    if output != None:
        file.write(output)



def parse(file_path):
    file = open(file_path).read()
    file = file.replace(" ", "").replace("\n", "")    
    file += "|"


    jumps = []


    buffer = ""
    i = 0
    while i < len(file)-1:
        counter = 0  
        char = file[i]
        while char == "+" and i < len(file) - 1:
            counter += 1
            i += 1 
            char = file[i]
        if(counter > 0):
            buffer += f"+:{counter}\n"
            continue

        while char == "-" and i < len(file) - 1:
            counter += 1
            i += 1 
            char = file[i]
        if(counter > 0):
            buffer +=  f"-:{counter}\n"
            continue
        while char == ">" and i < len(file) - 1:
            counter += 1
            i += 1 
            char = file[i]
        if(counter > 0):
            buffer +=  f">:{counter}\n"
            continue

        while char == "<" and i < len(file) - 1:
            counter += 1
            i += 1 
            char = file[i]
        if(counter > 0):
            buffer += f"<:{counter}\n"
            continue
        
        while char == "." and i < len(file) - 1:
            counter += 1
            i += 1 
            char = file[i]
        if(counter > 0):
            buffer += f".:{counter}\n"
            continue
        
        while char == "," and i < len(file) - 1:
            counter += 1
            i += 1 
            char = file[i]
        if(counter > 0):
            buffer += f",:{counter}\n"
            continue
            


        char = file[i]
        
        if char == "[":
            jumps.append(i)
            buffer += f"[:0\n"
        elif char == "]":
            if len(jumps) == 0:
                sys.stderr.write(f"Error found in code! Back jump with no closure found at position {i} \n")
                return None
            jumps.pop()
            buffer += f"]:0\n"
           
        else:
           buffer += char + "\n"     
        i+=1

    if(len(jumps) > 0):   
        sys.stderr.write(f"Error found in code! Unclosed jump found at positions [{', '.join(map(str, jumps))}]\n")
        return None
    return buffer



main()