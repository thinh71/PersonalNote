**Synchronization** - mô tả hai sự việc xảy ra tại cùng một thời điểm. 

Trong lĩnh vực khoa học máy tính, **synchronization** được sử dụng để mô tả mối quan hệ về mặt thời gian xảy ra giữa các sự kiện, một sự kiện có thể xảy ra trước, trong hoặc sau một sự kiện khác.

Có 2 vấn đề **synchronization constrains** nổi trội mà các lập trình viên quan tâm là: 
- **Serialization**: Sự kiện A phải xảy ra trước sự kiện B
- **Mutual exclusion**: Sự kiện A và B không được xảy ra tại cùng một thời điểm.

**Concurrent programming** cho phép nhiều threads được thực thi đồng thời, tuy nhiên, việc quản lý các threads hầu hết là do hệ điều hành quyết định, các lập trình viên hầu như rất khó để biết được khi nào thì một thread được thực thi và thứ thự thực thi của những threads là như thế nào. Điều này đặt ra nhu cầu cần phải có các cơ chế để kiểm soát các vấn đề liên quan đến **synchronization**.

