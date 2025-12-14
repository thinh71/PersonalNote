---
title: Các kỹ thuật giải quyết bài toán đồng bộ
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
## 1. Giải pháp cho bài toán serialization
Như đã đề cập ở [[Synchronization]], bài toán về **Serialization** yêu cầu một sự kiện A phải được thực hiện trước sự kiện B, nói một cách khác **Serialization** quan tâm đến thứ tự thực hiện của các sự kiện trong một chương trình.

**Serialization** thường gặp khi chúng ta phải làm việc với các **shared variables**.  
### 1.1 Serialization with messages 
Để dễ hình dung, chúng ta có một bài toán như sau:

Có 2 thread A và B, thread A thực thi tuần tự 3 công việc $a_1, a_2, a_3$. Tương tự thread B cũng thực thi tuần tự 3 công việc $b_1, b_2, b_3$. Yêu cầu đặt ra là đảm bảo công việc $b_2$ chỉ được thực thi sau khi $a_3$ được thực thi.

Ta có thể gọi thứ tự thực thi công việc ở thread A là $a_1 < a_2 < a_3$, tương tự $b_1 < b_2 < b_3$ cho thread B. Chúng ta không thể xác định được liệu rằng giữa $a_1, a_2$ và $b_1$ cái nào xảy ra trước? Nên bài toán có thể được mô tả dưới dạng đảm thứ tự thực thi như sau: 
$$b_2 > a_3 > a_2 > a_1$$
Có một cách giải quyết đơn giản cho bài toán này, đó là thêm vào một *`message`* giữa $a_3$ và $b_2$. Sau khi $a_3$ được thực thi, thread A sẽ gởi một *`message`* đến thread B, và chỉ khi nhận được *`message`* thì $b_2$ mới được thực thi. 

Thread A                                      |              Thread B
1. $a_1$                                                               1. $b_1$   
2. $a_2$                                                               2. Wait *`message`*
3. $a_3$                                                               3. $b_2$
4. Send a *`message`*                                       4. $b_3$




