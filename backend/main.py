بالتأكيد، إليك الكود لإنشاء نقطة نهاية FastAPI GET `/hello` التي ترجع `{"msg":"Hello Speedaf"}` بدون تبعيات إضافية (بمعنى أننا سنحتاج فقط إلى تثبيت FastAPI):

**1. التثبيت:**

إذا لم تكن قد قمت بتثبيت FastAPI و Uvicorn (خادم ASGI)، قم بتشغيل هذا الأمر في طرفيتك:

```bash
pip install fastapi uvicorn
```

**2. الكود:**

قم بإنشاء ملف Python (على سبيل المثال، `main.py`) وأضف الكود التالي:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def say_hello():
    return {"msg": "Hello Speedaf"}
```

**الشرح:**

*   `from fastapi import FastAPI`: نستورد فئة `FastAPI` الأساسية.
*   `app = FastAPI()`: ننشئ مثيلًا لتطبيق FastAPI.
*   `@app.get("/hello")`: هذا هو المُزخرف (decorator) الذي يخبر FastAPI أن الدالة التالية يجب أن تستجيب لطلبات `GET` على المسار `/hello`.
*   `async def say_hello():`: نعرف دالة غير متزامنة (async) باسم `say_hello`.
*   `return {"msg": "Hello Speedaf"}`: تقوم هذه الدالة بإرجاع قاموس Python، والذي سيتم تحويله تلقائيًا إلى JSON بواسطة FastAPI.

**3. التشغيل:**

افتح طرفيتك، انتقل إلى الدليل الذي يحتوي على ملف `main.py`، ثم قم بتشغيل الأمر التالي:

```bash
uvicorn main:app --reload
```

*   `main:app`: يخبر Uvicorn أن التطبيق موجود في ملف `main.py` وأن اسم مثيل FastAPI هو `app`.
*   `--reload`: هذا مفيد أثناء التطوير. سيقوم بإعادة تشغيل الخادم تلقائيًا عند اكتشاف تغييرات في الكود.

**4. الاختبار:**

افتح متصفح الويب الخاص بك أو استخدم أداة مثل `curl` أو Postman واطلب العنوان التالي:

```
http://127.0.0.1:8000/hello
```

يجب أن ترى الاستجابة التالية:

```json
{"msg":"Hello Speedaf"}
```

بهذا، تكون قد أنشأت نقطة نهاية GET بسيطة في FastAPI.