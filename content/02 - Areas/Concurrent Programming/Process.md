---
title: Process
type: note
domain: Concurrent Programming
tags:
  - common
level: beginner
status: draft
created: 2025-03-12
updated: 2025-03-12
---

**I. Process là gì?**

**Process** (tiến trình) là một đơn vị thực thi cơ bản của hệ điều hành. Mỗi khi một chương trình hoặc một lệnh được thực thi, hệ điều hành sẽ tạo ra một process tương ứng.  

Với mỗi process, hệ điều hành sẽ cung cấp một phần tài nguyên hệ thống [^1] để process thực thi các tác vụ được giao.

---
**II. Đặc điểm của process**

Một process thường có các đặc điểm sau đây:
- **Độc lập**: Mỗi process sẽ được cấp phát một vùng nhớ riêng biệt, không ảnh hưởng đến các process khác.  
- **Đồng thời**: Nhiều process có thể chạy đồng thời trên hệ thống nhờ khả năng đa nhiệm của hệ điều hành. 
- **Đơn nhất**: Mỗi process được gán cho một mã định danh duy nhất gọi là Process ID (PID) để phân biệt với process khác.

---
**III. Process trong Linux**

Linux cung cấp một số công cụ để người dùng quản lý các process như sau:
- **ps**: Giúp hiển thị các thông tin liên quan đến các process đang chạy.
- **top**: Cung cấp một giao diện thời gian thực cho các thông tin liên đến các process, bao gồm thông tin về CPU và memory.
- **kill**: Gởi tín hiệu đến process, thường dùng để kết thúc một process.
- **jobs**: Hiện thị các process đang chạy dưới nền

Ví dụ về giao diện khi chạy lệnh `htop` 
![[99 - Meta/Preloaded Classes/Images/Pasted image 20240603230129.png]]

[^1]: Tài nguyên của hệ thống bao gồm: CPU, memory, file descriptor, register, program counter, etc.  

