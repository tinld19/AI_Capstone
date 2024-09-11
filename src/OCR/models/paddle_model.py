from paddleocr import PaddleOCR

img_path = "/Users/mac/Documents/AI_Capstone/AI_Capstone/src/OCR_file/images/Screenshot 2024-09-05 at 11.46.26.png"
ocr = PaddleOCR(use_angle_cls=True)

result = ocr.ocr(img_path)

print(result)