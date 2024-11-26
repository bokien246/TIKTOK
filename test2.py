import tkinter as tk
from tkinter import filedialog, ttk
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

# Cấu hình OCR với PaddleOCR
ocr = PaddleOCR(
    use_angle_cls=True, 
    lang="vi",
    det_db_box_thresh=0.5,  
    use_gpu=False
)

# Hàm chọn ảnh và chạy OCR
def select_image_and_run_ocr():
    file_path = filedialog.askopenfilename(
        title="Chọn ảnh",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")]
    )
    if not file_path:
        status_label.config(text="Không có tệp nào được chọn.", foreground="red")
        return
    
    result = ocr.ocr(file_path, cls=True)
    
    if len(result[0]) == 0:
        status_label.config(text="Không phát hiện được văn bản trong ảnh.", foreground="red")
    else:
        status_label.config(text="Phân tích ảnh thành công!", foreground="green")
        for line in result[0]:
            print(f"Văn bản: {line[1][0]}")
            print(f"Chi tiết dòng: {line}")
        
        # Xử lý ảnh và hiển thị kết quả
        image = Image.open(file_path).convert('RGB')
        boxes = [line[0] for line in result[0]]
        texts = [line[1][0] for line in result[0]]

        font_path = 'C:/Windows/Fonts/Arial.ttf'
        # Bỏ qua scores trong hàm draw_ocr
        image_with_boxes = draw_ocr(image, boxes, texts, None, font_path=font_path)

        # Hiển thị ảnh kết quả
        plt.figure(figsize=(15, 10))
        plt.imshow(image_with_boxes)
        plt.axis("off")
        plt.show()

# Tạo giao diện bằng Tkinter
root = tk.Tk()
root.title("OCR với PaddleOCR")
root.geometry("500x300")
root.configure(bg="#f7f9fc")

# Tiêu đề
title_label = tk.Label(
    root, text="OCR với PaddleOCR", font=("Helvetica", 20, "bold"), bg="#f7f9fc", fg="#2d89ef"
)
title_label.pack(pady=20)

# Khung nút bấm
button_frame = tk.Frame(root, bg="#f7f9fc")
button_frame.pack(pady=20)

# Nút chọn ảnh
select_image_button = ttk.Button(button_frame, text="Chọn Ảnh", command=select_image_and_run_ocr)
select_image_button.grid(row=0, column=0, padx=10)

# Nhãn trạng thái
status_label = tk.Label(
    root, text="", font=("Helvetica", 12), bg="#f7f9fc", fg="#333"
)
status_label.pack(pady=10)

# Nút thoát
exit_button = ttk.Button(button_frame, text="Thoát", command=root.quit)
exit_button.grid(row=0, column=1, padx=10)

# Chạy vòng lặp giao diện
root.mainloop()
