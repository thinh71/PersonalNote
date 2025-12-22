---
title: C pointer
type: note
domain: C programming
tags:
  - C_Pointer
  - draft
level: beginner
status: draft
created: 2025-03-12
updated: 2025-12-18
---
Trong ngôn ngữ C, con trỏ (pointer) là một biến dùng để lưu địa chỉ bộ nhớ của một đối tượng[^1], chẳng hạn như biến hoặc mảng. Nói cách khác, thay vì lưu giá trị trực tiếp, con trỏ lưu vị trí nơi mà giá trị đó được đặt trong bộ nhớ.

Mỗi đối tượng trong chương trình được lưu trữ tại một vị trí cụ thể trong bộ nhớ, được xác định bởi một địa chỉ. Con trỏ cho phép truy cập hoặc thao tác dữ liệu thông qua địa chỉ này.
##### Khai báo một con trỏ
Để khai báo một con trỏ, đặt ký tự * ngay sau kiểu dữ liệu, theo sau là tên biến con trỏ.
```c
// <data type> * <variable_name>
int * ptr; // Declaration of an integer pointer
char * str; // str is a char pointer
```
##### Khởi tạo giá trị cho con trỏ
Vì biến con trỏ lưu trữ địa chỉ, do đó chúng ta cần một cách để lấy địa chỉ của biến trong bộ nhớ.
Toán tử & được dùng cho mục đích này, nó trả về địa chỉ của biến. Sau đó, địa chỉ này có thể được gán cho biến con trỏ.
```C
int a = 5;
int * ptr = &a; // prt points to the memory address of variale a
```
##### Truy cập giá trị được lưu tại biến con trỏ
Tại địa chỉ mà con trỏ đang trỏ đến, nếu muốn truy cập hay sửa đổi giá trị, chúng ta dùng toán tử * (dereferencing operator), cú pháp như sau:
```C
// * <pointer name>
int a = 5; 
int * ptr = &a;
printf("[Before] The value of a is: %d\n", *ptr);
*ptr = 10; // changes value of variable a
printf("[After] The value of a is: %d\n", *ptr);
```

Kết quả nhận được sẽ như sau:

>\[Before\] The value of a is: 5
>\[After\] The value of a is: 10


[^1]: Đối tượng ở đây có thể là biến (variables), mảng (arrays), chuỗi ký tự (strings), cấu trúc (structs), hàm (functions) và đối tượng cấp phát động (dynamic memory).