---
title: Mô hình thực thi
type: note
domain: Concurrent Programming
tags:
  - common
level: beginner
status: draft
created: 2025-03-12
updated: 2025-03-12
---
## 1. Mô hình tuần tự
Với mô hình này, máy tính thực thi các câu lệnh một cách tuần tự. Nếu một câu lệnh đến trước thì nó sẽ được thực thi trước.  

## 2. Mô hình song song 

Có 2 trường hợp máy tính sẽ thực thi chương trình theo mô hình này:
1. Khi máy tính được trang bị nhiều processors.
2. Khi một chương trình chứa nhiều threads chạy trên cùng một processor.

Trong trường hợp máy tính thực thi chương trình trên nhiều processors, việc xác định thứ tự thực thi các câu lệnh của chương trình trên các processor là rất khó khăn. Tương tự với các threads chạy trên cùng một processor, processor sẽ chạy một thread trong một khoảng thời gian, sau đó chuyển sang thread khác, và cứ như thế cho tất cả các thread. Lúc này việc xác định thứ tự thực thi các câu lệnh của các thread là một công việc phức tạp. 

Đối với trường hợp 1, chúng ta thường gọi là parallel programming, trường hợp 2 thường được gọi là concurrent programming.  

