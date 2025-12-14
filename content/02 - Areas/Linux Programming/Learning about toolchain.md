---
title: Learning about toolchain
type: note
domain: Linux Programming
tags:
  - Linux_programming
level: beginner
status: draft
created: 2025-03-12
updated: 2025-03-12
---

### 1. Tổng quan về toolchain

**Toolchain** là một tập hợp các công cụ cần thiết để chuyển đổi mã nguồn (source code) thành tệp thực thi (executable) có thể chạy được trên một thiết bị cụ thể (target device).

Toolchain thường chứa nhiều công cụ, tuy nhiên ba công cụ chính thường  là:
-  Compiler
-  Linker
-  Runtime libraries

Hiện nay, GNU Project và LLVM (Low-level Virtual Machine) Project là hai cộng đồng lớn nhất trong việc phát triển các toolchain cho Linux. GNU Project gắn liền với trình biên dịch **GCC**, có lịch sử phát triển lâu đời và được sử dụng rộng rãi. Ngược lại, LLVM Project cung cấp trình biên dịch **Clang**, được phát triển sau nhưng được đánh giá là có nhiều ưu điểm về tính năng và hiệu suất so với GCC.

Một GNU toolchain tiêu chuẩn bao gồm ba thành phần chính:
-  **Binutils**: tập hợp các tiện ích như assembler và linker.
-  **GCC**: trình biên dịch cho C cũng như các ngôn ngữ lập trình khác.
-  **C library**: một standardized ***Application Program Interface (API)*** dựa trên POSIX specification. Đây là thành phần giúp chương trình giao tiếp với kernel.

### 2. Các loại toolchain

Toolchain thường được chia thành **native toolchain** và **cross toolchain**.  

**Native toolchain**, là toolchain mà cả toolchain và chương trình được xây dựng bởi toolchain chạy trên cùng một hệ thống.

Ngược lại, **cross toolchain**, là toolchain mà chương trình được tạo ra bởi toolchain và toolchain được chạy trên hai hệ thống riêng biệt. 

Các thiết bị nhúng (embedded system) thường có tài nguyên hạn chế, do đó môi trường phát triển ứng dụng thường được tách riêng ra khỏi môi trường thực thi chương trình.
Chính vì lý do này, ***cross toolchain*** được sử dụng rộng rãi hơn ***native toolchain*** trong phát triển ứng dụng nhúng.




