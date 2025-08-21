# Levenshtein Distance Word Corrector

Đây là một ứng dụng web đơn giản được xây dựng bằng Streamlit nhằm minh họa chức năng sửa lỗi chính tả bằng thuật toán khoảng cách Levenshtein. Ứng dụng sẽ đề xuất từ đúng có khả năng nhất từ một kho từ vựng được xác định trước dựa trên khoảng cách chỉnh sửa.

## Tổng quan

Dự án này cung cấp một cách triển khai thực tế của thuật toán khoảng cách Levenshtein cho một trường hợp sử dụng phổ biến: kiểm tra lỗi chính tả. Người dùng có thể nhập một từ có khả năng bị sai và ứng dụng sẽ tính toán "khoảng cách chỉnh sửa" tới mọi từ trong một tệp từ vựng cục bộ. Từ có khoảng cách ngắn nhất sẽ được gợi ý làm phương án thay thế chính xác.

Toàn bộ giao diện người dùng được xây dựng bằng Streamlit, giúp nó có tính tương tác và dễ sử dụng.

## Nguyên lý hoạt động

Cốt lõi của ứng dụng này là thuật toán **khoảng cách Levenshtein**. Thuật toán này đo lường sự khác biệt giữa hai chuỗi bằng cách tính toán số lượng chỉnh sửa ký tự đơn tối thiểu (chèn, xóa hoặc thay thế) cần thiết để biến đổi từ này thành từ kia.

Ví dụ, khoảng cách Levenshtein giữa "**kitten**" và "**sitting**" là 3, vì nó đòi hỏi ba lần chỉnh sửa:
1.  **k**itten → **s**itten (thay thế "k" bằng "s")
2.  sitt**e**n → sitt**i**n (thay thế "e" bằng "i")
3.  sittin → sittin**g** (chèn ký tự "g")

Ứng dụng tận dụng số liệu này để tìm ra từ "gần nhất" trong kho từ vựng so với từ mà người dùng nhập vào.

## Tính năng

-   Giao diện web đơn giản và trực quan được xây dựng bằng Streamlit.
-   Tính toán khoảng cách Levenshtein giữa từ do người dùng cung cấp và mọi từ trong kho từ vựng tùy chỉnh.
-   Gợi ý từ đúng có khả năng nhất dựa trên khoảng cách chỉnh sửa tối thiểu.
-   Hiển thị toàn bộ kho từ vựng và các khoảng cách đã được sắp xếp để đảm bảo tính minh bạch và dễ phân tích.

## Yêu cầu cài đặt

-   Python 3.7+
-   pip (Trình quản lý gói của Python)

## Cài đặt & Thiết lập

Làm theo các bước sau để thiết lập và chạy dự án trên máy của bạn.

1.  **Tải dự án về máy**
    -   Tải tệp `levenshtein_distance.py` về thư mục làm việc của bạn.

2.  **Tạo tệp từ vựng**
    -   Trong cùng thư mục với tệp script, hãy tạo một tệp có tên là `vocab.txt`.
    -   Thêm các từ bạn muốn vào tệp này, mỗi từ trên một dòng. Ví dụ:
        ```
        thuật toán
        ứng dụng
        chỉnh sửa
        khoảng cách
        levenshtein
        python
        streamlit
        ```

3.  **Cài đặt các thư viện cần thiết**
    -   Mở terminal (hoặc Command Prompt) và điều hướng đến thư mục dự án.
    -   Cài đặt thư viện Streamlit bằng lệnh sau:
        ```bash
        pip install streamlit
        ```

## Hướng dẫn sử dụng

1.  Đảm bảo rằng bạn đang ở trong thư mục dự án trên terminal.
2.  Chạy lệnh sau để khởi động ứng dụng Streamlit:
    ```bash
    streamlit run levenshtein_distance.py
    ```
3.  Trình duyệt web mặc định của bạn sẽ tự động mở một tab mới với ứng dụng đang chạy.
4.  Nhập một từ vào ô đầu vào và nhấp vào nút "Compute" để xem gợi ý và kết quả tính toán khoảng cách.

## Cấu trúc dự án

Dự án yêu cầu cấu trúc tệp như sau để hoạt động chính xác:

/your-project-folder
|
├── levenshtein_distance.py   # Tệp script chính của ứng dụng
└── vocab.txt                 # Tệp chứa kho từ vựng