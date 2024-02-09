; Declare i32 @main()
declare i32 @putchar(i32)
declare i32 @getchar()
declare i32 @printf(i8*, ...)


@format_str_int = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
@format_str_char = private unnamed_addr constant [3 x i8] c"%c\00", align 1



define void @add(i8** %ptr_ptr, i8 %val) {
  ; Read from the tape
  %ptr = load i8*, i8** %ptr_ptr  
  %currentVal = load i8, i8* %ptr
  ; Add the value
  %newVal = add i8 %currentVal, %val
  ; Write back to the tape
  store i8 %newVal, i8* %ptr
  ret void
}

define void @sub(i8** %ptr_ptr, i8 %val) {
  %ptr = load i8*, i8** %ptr_ptr  
  ; Read from the tape
  %currentVal = load i8, i8* %ptr
  ; Subtract the value
  %newVal = sub i8 %currentVal, %val
  ; Write back to the tape
  store i8 %newVal, i8* %ptr
  ret void
}

define void @print_char(i8** %ptr_ptr) {
  %ptr = load i8*, i8** %ptr_ptr  
  ; Load the value from the tape
  %val = load i8, i8* %ptr
  ; Extend i8 to i32
  %valExt = sext i8 %val to i32
  ; Call putchar
  call i32 (i8*, ...) @printf(i8* @format_str_char, i32 %valExt)
  ret void
}

define void @print_int(i8** %ptr_ptr){
  %ptr = load i8*, i8** %ptr_ptr  
  ; Load the value from the tape
  %val = load i8, i8* %ptr
  ; Extend i8 to i32
  %valExt = sext i8 %val to i32
  ; Call putchar
  call i32 (i8*, ...) @printf(i8* @format_str_int, i32 %valExt)

  ret void
}



define void @lshift(i8** %ptr_ptr, i32 %increments){
    %ptr = load i8*, i8** %ptr_ptr
    %dec_inc = sub i32 0, %increments
    %incPtr = getelementptr i8, i8* %ptr, i32 %dec_inc
    store i8* %incPtr, i8** %ptr_ptr
    ret void

}

define void @rshift(i8** %ptr_ptr, i32 %increments){
    %ptr = load i8*, i8** %ptr_ptr
    %incPtr = getelementptr i8, i8* %ptr, i32 %increments
    store i8* %incPtr, i8** %ptr_ptr
    ret void

}

define void @input(i8** %ptr_ptr){
    %ptr = load i8*, i8** %ptr_ptr
    %char = call i32 @getchar()
    %char_i8 = trunc i32 %char to i8
    store i8 %char_i8, i8* %ptr
    ret void
}


