---
title: Static and Dynamic Libraty
type: note
domain: C programming
tags:
  - common
  - draft
level: beginner
status: draft
created: 2025-03-12
updated: 2025-03-12
---

**I. Static Library (`.a`)**

**Khái niệm:** Một thư viện tĩnh (static library) là một tập hợp các pre-compiled object files (**`.o`**) được kết hợp cùng nhau dưới dạng một file lưu trữ (**`.a`**). Các object files chứa mã máy của các hàm và các cấu trúc dữ liệu của thư viện. 

**Linking:** Trong quá trình biên dịch chương trình, trình liên kết (**`linker`**) sẽ hợp nhất các object files cần thiết từ thư viện tĩnh trực tiếp vào file thực thi của chương trình. Quá trình này còn được gọi là **static linking**.

**Ưu điểm:** 
- **Self-contained executable:** Bởi vì thư viện tĩnh được liên kết trực tiếp vào chương trình để tạo ra file thực thi, cho nên chương trình không cần đến sự hiện diện của các thư viện này ở thời điểm runtime. Điều này có lợi cho việc phân phối chương trình trên các hệ thống mà ở đó thiếu vắng các thư viện được dùng cho chương trình.
- **Faster startup:** Bởi vì library code đã được tích hợp sẵn trong file thực thi, thời gian khởi động của chương trình có thể nhanh hơn một chút so với các chương trình sử dụng shared library. 

**Nhược điểm:**
- **Kích thước file thực thi lớn hơn:** Kích thước của chương trình tỉ lệ tuyến tính với kích thước của thư viện tĩnh, trong trường hợp một thư viện tĩnh được dùng trong nhiều chương trình khác nhau. Điều này yêu cầu việc sao chép thư viện tĩnh này vào từng chương trình. Trong trường hợp này, kích thước của chương trình tĩnh cần được xem xét, đặc biệt đối với các môi trường hạn chế về bộ nhớ (memory-constrained environments) vấn này càng nên được chú ý phân tích.
- **Cập nhật thư viện tĩnh yêu cầu biên dịch lại chương trình:** Nếu chúng ta cập nhật thư viện tĩnh, chúng ta cần phải biên dịch lại toàn bộ các chương trình sử dụng chương trình tĩnh đó để đảm bảo các chương trình sử dụng thư viện tĩnh bản mới nhất.

**II. Shared Libraries (`.so` on Linux/Unix, `.dll` on Windows):**

**Khái niệm:** Một thư viện chia sẻ (**`shared library`**) là một tập hợp các pre-compiled object files dưới dạng một file **`.so`** hoặc **`.dll`**. Hệ điều hành tải các shared libraries lên memory khi một chương trình sử dụng các thư viện này bắt đầu thực thi. Nhiều chương trình có thể chia sẻ chung một instance của shared library này trên memory.  

**Linking:** Trong quá trình biên dịch của chương trình, trình liên kết (**`linker`**) chỉ tạo các tham chiếu đến các hàm cũng như các cấu trúc dữ liệu của shared library. Các tham chiếu này sẽ được giải mã tại thời điểm runtime khi chương trình bắt đầu thực thi và shared library được hệ điều hành tải lên memory. Quá trình này còn được gọi là **dynamic linking**. 

**Ưu điểm:** 
- **Kích thước file thực thi nhỏ hơn:** Các chương trình sử dụng shared libraries tiết kiệm bộ nhớ bởi một bản sao chép của shared library trên memory có thể được sử dụng cho nhiều chương trình giúp giảm việc sử dụng bộ nhớ.  
- **Cập nhật shared library không yêu cầu biên dịch lại chương trình:** Chỉ cần các interface của shared library được duy trì tương thích, việc cập nhật shared library không yêu cầu phải biên dịch lại các chương trình sử dụng shared library này.  

**Nhược điểm:** 
- **External dependency:** Các chương trình sử dụng các shared libraries phụ thuộc vào sự hiện diện của các thư viện này tại thời điểm runtime. Nếu trong trường hợp shared libraries bị thiếu hoặc không tương thích, chương trình có thể bị lỗi khi thực thi.  
- **Slower startup:** So sánh với các thư viện tĩnh, các chương trình sử dụng các shared libraries có thể khởi động chậm hơn bởi the loader cần thời gian để tìm và tải các shared libraries lên memory.  
