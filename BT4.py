# Phần 1: Phân tích Input/OutputInput của bài toán:Danh sách các cuốn sách hiện có trong hệ thống (dạng mảng các dictionary). 
# Mỗi phần tử đại diện cho một cuốn sách chứa các thông tin như id, title, và quantity (số lượng tồn kho).Output mong muốn:
# Một phản hồi định dạng JSON chứa hai thông tin chính: message (chuỗi thông báo kết quả) và 
# data (mảng danh sách các sách thỏa mãn điều kiện sắp hết hàng và hợp lệ)
# .Điều kiện để xác định sách sắp hết hàng:Trường quantity phải tồn tại, có giá trị hợp lệ ($\ge 0$) và thỏa mãn điều kiện: $\text{quantity} \le 5$.

# Phần 2: Đề xuất giải pháp duyệt danh sách và lọc sáchĐể thực hiện việc duyệt mảng dữ liệu gốc và lọc ra các cuốn sách thỏa mãn yêu cầu, 
# ta có 2 giải pháp phổ biến trong Python:
# Giải pháp 1: Sử dụng vòng lặp for truyền thống kết hợp câu lệnh điều kiện if
# Cách xử lý: Tạo một mảng rỗng low_stock_books = [].
# Duyệt qua từng cuốn sách bằng for book in books:. 
# Sử dụng if để kiểm tra sự tồn tại của trường quantity, kiểm tra tính hợp lệ ($>0$) và 
# điều kiện $\le 5$. Nếu thỏa mãn thì .append(book) vào mảng kết quả.
# Giải pháp 2: Sử dụng List Comprehension (Tạo list ngắn gọn)
# Cách xử lý: Sử dụng cú pháp rút gọn của Python để vừa duyệt vừa lọc dữ liệu trên một dòng code duy nhất:
# [book for book in books if "quantity" in book and 0 <= book["quantity"] <= 5].
# Phần 3: So sánh và lựa chọn giải pháp