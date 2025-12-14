---
title: Thread
type: note
domain: Concurrent Programming
tags:
  - common
  - draft
level: beginner
status: draft
created: 2025-03-12
updated: 2025-03-12
---

**I. Thread là gì?**

**Thread** (luồng) là đơn vị thực thi nhỏ nhất trong một tiến trình ([[Process|process]]). 

---
**II. Đặc điểm của thread**

Các thread thường có các đặc điểm sau đây:
- **Chia sẻ tài nguyên**: Các thread trong cùng một tiến trình sẽ chia sẻ các tài nguyên của tiến trình với nhau.
- **Yêu cầu đồng bộ hóa**: Vì các thread chia sẻ tài nguyên với nhau nên yêu cầu một cơ chế đồng bộ hóa để tránh các vấn đề liên quan đến việc tranh chấp tài nguyên như race condition, deadlock và sự không nhất quán dữ liệu (inconsistency data).  
- **Hiệu suất cao**: Đa luồng (multi-thread) cho phép tận dụng đối đa khả năng xử lý của CPU bằng cách chạy nhiều tác vụ đồng thời.  

---
**III. Thread với C programming**

Kể từ C11, ngôn ngữ C đã cung cấp thư viện `threads.h` và `stdatomic.h` hỗ trợ cho việc lập trình đồng thời (concurrent programming). 