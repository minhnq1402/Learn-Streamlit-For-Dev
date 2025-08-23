# A Collection of AI Applications with Streamlit

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/minhnq1402/Word-Correction-using-Levenshtein-Distance?style=for-the-badge)](https://github.com/minhnq1402/Word-Correction-using-Levenshtein-Distance/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/minhnq1402/Word-Correction-using-Levenshtein-Distance?style=for-the-badge)](https://github.com/minhnq1402/Word-Correction-using-Levenshtein-Distance/network)
[![GitHub issues](https://img.shields.io/github/issues/minhnq1402/Word-Correction-using-Levenshtein-Distance?style=for-the-badge)](https://github.com/minhnq1402/Word-Correction-using-Levenshtein-Distance/issues)
[![GitHub language](https://img.shields.io/github/languages/top/minhnq1402/Word-Correction-using-Levenshtein-Distance?style=for-the-badge)](https://github.com/minhnq1402/Word-Correction-using-Levenshtein-Distance)

**Một bộ sưu tập các ứng dụng trí tuệ nhân tạo (AI) được xây dựng bằng Python và Streamlit.**

</div>

## 1.Tổng quan

Đây là kho mã nguồn chứa ba ứng dụng độc lập, được xây dựng để minh họa các khái niệm khác nhau trong lĩnh vực AI, bao gồm Xử lý ngôn ngữ tự nhiên (NLP) và Thị giác máy tính (Computer Vision). Mỗi ứng dụng được triển khai với giao diện web tương tác bằng Streamlit.

1.  **Sửa lỗi từ (Word Correction):**
    * Sử dụng thuật toán khoảng cách Levenshtein để đo lường sự khác biệt giữa hai chuỗi ký tự.
    * Ứng dụng cho phép người dùng nhập một từ, sau đó tìm và gợi ý từ đúng nhất có trong từ điển dựa trên khoảng cách Levenshtein nhỏ nhất.

2.  **Phát hiện đối tượng (Object Detection):**
    * Sử dụng mô hình MobileNetSSD đã được huấn luyện trước và thư viện OpenCV để phát hiện các đối tượng trong hình ảnh.
    * Người dùng có thể tải lên một hình ảnh, và ứng dụng sẽ vẽ các hộp giới hạn (bounding box) xung quanh các đối tượng mà nó nhận diện được.

3.  **ChatBot đơn giản (Simple ChatBot):**
    * Một giao diện chatbot tương tác, tích hợp với các mô hình ngôn ngữ lớn thông qua Hugging Face.
    * Người dùng cần cung cấp thông tin đăng nhập Hugging Face để trò chuyện và nhận phản hồi từ AI.

## 2.Tính năng

### Đối với ứng dụng Sửa lỗi từ:
-   Tính toán khoảng cách Levenshtein giữa các từ một cách hiệu quả.
-   Tải và xử lý danh sách từ vựng từ file `vocab.txt`.
-   Gợi ý từ đúng với giao diện trực quan hiển thị các khoảng cách đã tính.

### Đối với ứng dụng Phát hiện đối tượng:
-   Cho phép tải lên hình ảnh định dạng `jpg`, `png`, `jpeg`.
-   Sử dụng mô hình Caffe (`MobileNetSSD`) để phát hiện đối tượng trong thời gian thực.
-   Vẽ hộp giới hạn và hiển thị kết quả xử lý ngay trên giao diện.

### Đối với ứng dụng ChatBot:
-   Giao diện trò chuyện thân thiện, lưu lại lịch sử phiên làm việc.
-   Yêu cầu đăng nhập an toàn qua sidebar để kết nối với Hugging Face.
-   Tương tác trực tiếp với các mô hình ngôn ngữ mạnh mẽ.

## 3.Công nghệ sử dụng

-   **Ngôn ngữ:** Python
-   **Thư viện:**
    -   **Streamlit:** Xây dựng giao diện web tương tác cho cả ba ứng dụng.
    -   **OpenCV (`cv2`):** Xử lý hình ảnh trong ứng dụng phát hiện đối tượng.
    -   **Numpy:** Thực hiện các phép toán số học hiệu quả.
    -   **HugChat:** Giao tiếp với API của Hugging Face Chat.
    -   **Pillow (PIL):** Xử lý và chuyển đổi định dạng hình ảnh.

## 4.Hướng dẫn cài đặt và sử dụng

### Yêu cầu
-   Python 3.7+
-   Git

### Cài đặt

1.  **Clone repository về máy:**
    ```bash
        git clone https://github.com/minhnq1402/Learn-Streamlit-For-Dev.git
        cd Learn-Streamlit-For-Dev
    ```

2.  **(Tùy chọn) Tạo và kích hoạt môi trường ảo:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # Trên Windows: .venv\Scripts\activate
    ```

3.  **Cài đặt các thư viện cần thiết:**
    ```bash
    pip install streamlit opencv-python numpy pillow hugchat
    ```

### Sử dụng

Bạn có thể chạy riêng lẻ từng ứng dụng bằng các lệnh sau từ thư mục gốc của dự án:

1.  **Để chạy ứng dụng Sửa lỗi từ:**
    ```bash
    streamlit run levenshtein_distance.py
    ```
    *Lưu ý: Cần có file `vocab.txt` trong cùng thư mục để ứng dụng hoạt động.*

2.  **Để chạy ứng dụng Phát hiện đối tượng:**
    ```bash
    streamlit run object_detection.py
    ```
    *Lưu ý: Cần có thư mục `model` chứa các file `MobileNetSSD_deploy.caffemodel` và `MobileNetSSD_deploy.prototxt.txt`.*

3.  **Để chạy ứng dụng ChatBot:**
    ```bash
    streamlit run chatbot.py
    ```
    *Lưu ý: Bạn cần có tài khoản Hugging Face và nhập email/mật khẩu trên giao diện để sử dụng.*

## 5.Cấu trúc thư mục:
```
Word-Correction-using-Levenshtein-Distance/
├── README.md
├── model/                          # Chứa các file model cho việc phát hiện đối tượng
│   ├── MobileNetSSD_deploy.caffemodel
│   └── MobileNetSSD_deploy.prototxt.txt
├── vocab.txt                       # Từ điển cho ứng dụng sửa lỗi từ
├── levenshtein_distance.py         # Mã nguồn ứng dụng sửa lỗi từ
├── object_detection.py             # Mã nguồn ứng dụng phát hiện đối tượng
└── chatbot.py                      # Mã nguồn ứng dụng chatbot
```
<div align="center">

### made by minhnq142

</div>