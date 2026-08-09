# 🖼️ BinarySecrets Image API

<div align="center">

**یک API سبک و سریع برای فشرده‌سازی و تغییر اندازه تصاویر**  
**A lightweight & fast API for image compression and resizing**

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.141+-009688.svg)](https://fastapi.tiangolo.com/)
[![Pillow](https://img.shields.io/badge/Pillow-12.3+-yellow.svg)](https://python-pillow.org/)

</div>

---

## ✨ ویژگی‌ها / Features

| فارسی | English |
|-------|---------|
| فشرده‌سازی تصاویر با کیفیت قابل تنظیم | Adjustable quality image compression |
| تغییر اندازه با الگوریتم LANCZOS | High-quality resize using LANCZOS |
| پشتیبانی از JPEG، PNG و AVIF | Supports JPEG, PNG and AVIF |
| مستندات زیبا با Scalar | Beautiful API docs with Scalar |
| ساختار تمیز و قابل توسعه | Clean and extensible architecture |

---

## 🛠️ تکنولوژی‌ها / Tech Stack

| تکنولوژی / Technology | نسخه / Version |
|-----------------------|----------------|
| Python                | ≥ 3.12         |
| FastAPI               | ≥ 0.141        |
| Pillow                | ≥ 12.3         |
| uv                    | Package Manager|

---

## 🚀 راه‌اندازی سریع / Quick Start

### ۱. کلون کردن پروژه / Clone the repository

```bash
git clone https://github.com/binarysecrets-ir/binarysecrets_api.git
cd binarysecrets_api
```

### ۲. نصب وابستگی‌ها / Install dependencies

```bash
uv sync
```

### ۳. اجرای سرور / Run the server

```bash
uv run uvicorn main:app --reload
```

سرور روی آدرس زیر در دسترس خواهد بود:  
The server will be available at:

```
http://127.0.0.1:8000
```

---

## 📖 مستندات API / API Documentation

مستندات تعاملی با **Scalar** در آدرس زیر قابل مشاهده است:  
Interactive documentation powered by **Scalar** is available at:

```
http://127.0.0.1:8000/scalar
```

---

## 📡 نحوه استفاده / Usage

### Endpoint

```
POST /image/compress
```

### پارامترها / Parameters

| نام / Name | نوع / Type       | توضیح / Description                          | پیش‌فرض / Default |
|------------|------------------|----------------------------------------------|-------------------|
| `image`    | File             | فایل تصویر (multipart/form-data)            | -                 |
| `config`   | JSON String      | تنظیمات فشرده‌سازی به صورت Form             | -                 |

### نمونه تنظیمات / Sample Config

```json
{
  "quality": 85,
  "width": 1280,
  "height": 720,
  "out_format": "AVIF"
}
```

- `quality`: عدد بین ۱ تا ۱۰۰ / Integer between 1 and 100  
- `width` و `height`: اختیاری / Optional (if not provided, original size is kept)  
- `out_format`: یکی از `JPEG`، `PNG`، `AVIF`

### نمونه درخواست با cURL / cURL Example

```bash
curl -X POST "http://127.0.0.1:8000/image/compress" \
  -F "image=@photo.jpg" \
  -F 'config={"quality":80,"width":800,"height":600,"out_format":"AVIF"}' \
  --output compressed.avif
```

---

## 📁 ساختار پروژه / Project Structure

```
binarysecrets_api/
├── main.py              # نقطه ورود FastAPI / FastAPI entry point
├── models.py            # مدل‌های Pydantic / Pydantic models
├── utils/
│   └── images.py        # منطق پردازش تصویر / Image processing logic
├── static/
│   └── standalone.js    # فایل Scalar / Scalar standalone file
├── pyproject.toml
└── uv.lock
```

---

## 🧩 معماری / Architecture

کلاس `ImageProcessor` با استفاده از الگوی **Strategy**، انکودرهای مختلف را مدیریت می‌کند:  
The `ImageProcessor` class uses the **Strategy** pattern to manage different encoders:

- `JPEGEncoder`
- `PNGEncoder`
- `AVIFEncoder`

این طراحی باعث می‌شود اضافه کردن فرمت‌های جدید بسیار ساده باشد.  
This design makes adding new formats very easy.

---

## 📌 نکات مهم / Notes

- تصاویر نامعتبر با خطای `406` برگردانده می‌شوند.  
  Invalid images return a `406` error.
- تصاویر RGBA هنگام تبدیل به JPEG به صورت خودکار به RGB تبدیل می‌شوند.  
  RGBA images are automatically converted to RGB when saving as JPEG.
- Resize فقط زمانی انجام می‌شود که `width` و `height` مشخص شده باشند.  
  Resize only happens when both `width` and `height` are provided.

---

## 🤝 مشارکت / Contributing

اگر ایده یا باگی پیدا کردی، خوشحال می‌شم Pull Request یا Issue باز کنی.  
Feel free to open an Issue or Pull Request if you find a bug or have an idea.

---

## 📄 لایسنس / License

این پروژه در حال حاضر لایسنس مشخصی ندارد.  
This project currently has no specific license.

اگر می‌خوای لایسنس اضافه بشه، بگو.  
Let me know if you'd like to add a license.

---
## توسعه دهندگان/dev team
[@parshan](https://github.com/parshanm)
<div align="center">

ساخته شده با ❤️ توسط [BinarySecrets](https://binarysecrets.ir)  
Made with ❤️ by [BinarySecrets](https://binarysecrets.ir)

</div>
```
