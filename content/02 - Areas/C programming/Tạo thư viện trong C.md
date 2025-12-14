---
title: Tạo thư viện trong C
type: note
domain: C programming
tags:
  - common
level: beginner
status: draft
created: 2025-03-12
updated: 2025-03-12
---
Sau một thời gian làm việc với ngôn ngữ C, chúng ta chắc hẳn sẽ quen thuộc với các thư viện chuẩn của C như **`stdio.h`**, **`string.h`**, hay **`math.h`**. Tuy nhiên, có bao giờ bạn tự hỏi làm thế nào chúng ta có thể tạo ra một thư viện cho riêng mình? 

Trong bài viết này, hãy cùng nhau tìm hiểu cách tạo một thư viện cho riêng mình bằng ngôn ngữ C và cách sử dụng thư viện được tạo.

**I. Thư viện trong C**
Cũng giống như một hộp công cụ cho thợ cơ khí, [^1] nơi chứa các công cụ thiết yếu để người thợ có thể làm việc một cách hiệu quả. Thư viện C tập hợp các hàm, cấu trúc dữ liệu cũng như các thành phần có liên quan khác được viết sẵn và được đóng gói cùng nhau để cung cấp các chức năng cụ thể. 

Trong ngôn ngữ C, các thư viện khác nhau giải quyết các nhiệm vụ khác nhau. Ví dụ, khi cần xử lý các vấn đề liên quan đến dữ liệu dạng chữ, chúng ta có thư viện **`string.h`**, hay khi đối mặt với các vấn đề liên quan đến phép toán, chúng ta có thư viện **`math.h`**. 

Từ những ngày đầu phát triển với chỉ một vài thư viện cung cấp một số chức năng cơ bản thì cho đến ngày nay, ngôn ngữ C hiện tại [^2] đã được trang bị đa dạng các thư viện chuẩn giúp các lập trình viên giải quyết các vấn đề ngày càng phức tạp phát sinh trong lĩnh vực lập trình.

**II. Tự tạo riêng một thư viện cho mình**
Bây giờ hãy bắt tay vào tạo riêng cho mình một thư viện giống như các thư viện chuẩn được đề cập ở trên. 

Giả sử chúng ta muốn tạo một thư viện giúp chúng ta thực hiện các công việc tính toán đơn giản như cộng, trừ hai số nguyên. Ta có thể làm như sau:

>[!EXAMPLE]- Tạo danh sách các hàm mà thư viện cung cấp
Tạo một tệp có phần mở rộng **`.h`** (ví dụ: **`mylib.h`**). Tệp này khai báo các hàm mà thư viện có thể cung cấp. Trong **`mylib.h`**, chúng ta sẽ khai báo các hàm **`add`** và **`minus`** tương ứng với hàm thực hiện phép cộng và phép trừ.
> ```c 
> // mylib.h
> 
> #ifndef MYLIB_H
> #define MYLIB_H
> 
> int add(int a, int b);
> int minus(int a, int b);
> 
> #endif
> 
> ```

> [!EXAMPLE]- Xây dựng định nghĩa cho các hàm
> Tạo một tệp có phần mở rộng **`.c`** (ví dụ: **`mylib.c`**). Tệp này chứa mã định nghĩa cho các hàm được khai báo trong **`mylib.h`**.
> ```c
> // mylib.c
> #include "mylib.h"
> 
> int add(int a, int b)
> {
> 	return a + b;
> }
> 
> int minus(int a, int b)
> {
> 	return a - b;
> }
> ```

> [!EXAMPLE]- Biên dịch thư viện
> Sử dụng trình biên dịch **`gcc`** để dịch chương trình sang mã máy.
> ```bash
> gcc -c mylib.c
> ```
> Kết quả sau khi chạy dòng lệnh trên, một tệp đối tượng (**`mylib.o`**) sẽ được tạo ra.
> //todo: Add image

> [!EXAMPLE]- Đóng gói thư viện
> Ở bước cuối cùng, chúng ta sẽ đóng gói chương trình thành thư viện để có thể sử dụng sau này. Có 2 loại thư viện mà chúng ta có thể tạo ra là thư viện tĩnh (static library) hoặc thư viện động (dynamic library hay shared library). Chi tiết về 2 loại thư viện này, bạn có thể tham khảo tại bài viết: [[Static and Dynamic Library]]
> 
> a. Đóng gói thành thư viện tĩnh (static library)
>    Để đóng gói thành thư viện tĩnh, chúng ta sẽ sử dụng công cụ lưu trữ **`ar`** để kết hợp tệp đối tượng (**`mylib.o`**) thành thư viện tĩnh (**`mylib.a`**) bằng câu lệnh sau:
> ```bash
>    ar rcs mylib.a mylib.o
> ```
> b. Đóng gói thành thư viện động (dynamic library)
>    Để đóng gói thành thư viện động, sử dụng trình biên dịch **`gcc`** với cờ **`-shared`** để tạo thành thư viện chia sẻ (**`mylib.so`**) từ tệp đối tượng **`mylib.o`**.
> ```bash
> gcc -shared -o mylib.so mylib.o
> ```


**III. Sử dụng thư viện tùy chỉnh của bạn**
Bây giờ chúng ta đã có thư viện tùy chỉnh của mình, để sử dụng thư viện này trong các chương trình khác, chúng ta có thể thực hiện như sau:
1. Include the header file
Để sử dụng thư viện đã tạo, chúng ta cần thêm header file (**`mylib.h`**) vào trong mã nguồn của chương trình cần sử dụng thư viện này. 
```c
// myapp.c

#include <stdio.h>
#include "mylib.h"

int main()
{
	int x = 5, y = 3;
	// Using functions from mylib.h
	int sum = add(x, y);
	int difference = minus(x, y);

	printf("Sum of %d and %d is %d\n", x, y, sum);
	printf("Difference of %d and %d is %d\n", x, y, difference);

	return 0;
}

```

2. Link the library
Trong quá trình biên dịch chương trình, chúng ta cần liên kết thư viện đã tạo (cho dù là thư viện tĩnh hay thư viện động) để chương trình có thể sử dụng được thư viện. Cú pháp thực hiện như sau:
```bash
gcc -o myapp myapp.c -L./ -l:mylib.a
```
Trong câu lệnh trên, cờ  **`-L`** hướng dẫn cho trình liên kết (**`linker`**) tìm kiếm thư viện tại đường dẫn **`./`** (folder hiện tại), cờ **`mylib`** chỉ thị thư viện cần sử dụng có tên **`mylib`**.
![[99 - Meta/Preloaded Classes/Images/Pasted image 20240515163218.png]]













[^1]: Bộ công cụ cơ khí.![[99 - Meta/Preloaded Classes/Images/Pasted image 20240515115719.png]]

[^2]: C23 là phiên bản được đề trong bài viết này. C23 cung cấp 31 thư viện chuẩn. 

