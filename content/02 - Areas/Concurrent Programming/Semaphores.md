> Trong lĩnh vực phần mềm, **semaphore** là một ***data structure*** được dùng để giải quyết các vấn đề liên quan đến **synchronization**. 

### I. Definition

Semaphore giống như một số integer, với 3 điểm khác biệt:

1. Giá trị khởi tạo của một semaphore có thể là một số nguyên (integer) bất kỳ. Tuy nhiên, sau khi gởi tạo, chúng ta chỉ có thể thực thi việc tăng hoặc giảm giá trị của semaphore 1 đơn vị. Ngoài ra, chúng ta không thể đọc được giá trị hiện tại của semaphore.    

2. Khi một thread thực hiện việc giảm giá trị của semaphore, nếu kết quả là số âm, thread đó sẽ khóa chính nó (blocks itself) cho đến khi một thread khác thực hiện việc tăng giá trị cho semaphore. 

3. Khi một thread tăng giá trị cho semaphore, nếu có các thread khác đang ở trạng thái chờ, thì một trong các thread này sẽ được unblock.  

### II. Ý nghĩa giá trị semaphore

Xét một semaphore $sem$, thì giá trị của $sem$ có thể là một trong 3 trường hợp sau:

1. $sem > 0$: Trong trường hợp này, giá trị $sem$ thể hiện số các thread có thể thực thi việc giảm mà không bị rơi vào trạng thái blocking.

2. $sem = 0$: Trong trường hợp này, không có thread nào đang ở trạng thái blocking. Tuy nhiên, nếu có một thread thực thi việc giảm, thread đó sẽ vào trạng thái blocking. 

3. $sem < 0$: Trong trường hợp này, giá trị $sem$ thể hiện số các thread đang trong trạng thái blocking.  

### III. Ứng dụng của semaphore

Mặc dù không nhất thiết phải dùng **semaphore** để giải quyết các vấn đề **synchronization**. Tuy nhiên, **semaphore** có một vài ưu điểm sau:

- **Semaphore** áp đặt các ràng buộc có chủ ý giúp cho các lập trình viên tránh được các lỗi. 

- Các giải pháp sử dụng **semaphore** thường `clean` và `organized` giúp cho chúng dễ dàng thể hiện tính đúng đắn của giải pháp. 

- Các **semaphore** có thể được triển khai hiệu quả trên nhiều hệ thống, do đó có giải pháp sử dụng **semaphore** có tính di động và thường hiệu quả. 
