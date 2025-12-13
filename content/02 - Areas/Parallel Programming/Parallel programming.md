# 1. Parallel programming là gì?

Parallel programming, hay parallel computing, là một quá trình chia các vấn đề tính toán lớn thành các nhiều bài toán nhỏ có thể giải quyết đồng thời bởi nhiều processor. 

Các processor giao tiếp với nhau thông qua một bộ nhớ chung (shared memory) và các kết quả tính toán từ các processor được kết hợp lại bởi thuật toán, từ đó cho ra kết quả cho bài toán lớn ban đầu. 

Hình bên dưới mô tả cách hoạt động của parallel programming so với serial programming.

![[99 - Meta/Preloaded Classes/Images/Pasted image 20240719182905.png]] ![[99 - Meta/Preloaded Classes/Images/Pasted image 20240719182949.png]]

# 2. Parallel computing architectures
## 2.1 Shared memory

**Shared memory architecture** được sử dụng phổ biến trong các ứng dụng parallel computing, chẳng hạn như laptop hay điện thoại thông minh. Đối với kiến trúc này, các máy tính song song (parallel computer) dựa vào nhiều bộ xử lý (processor) để liên hệ với cùng một tài nguyên bộ nhớ dùng chung (shared memory resource). 

![[99 - Meta/Preloaded Classes/Images/Pasted image 20240721172709.png]]