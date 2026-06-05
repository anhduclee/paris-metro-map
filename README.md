# Paris Metro Map

## Giới thiệu
Đây là một dự án đầy tâm huyết của tác giả giúp giải quyết vấn đề tìm đường đi trong mạng lưới metro dày đặc của Paris (hơn 300 ga), phục vụ cho bà con nhân dân có trải nghiệm đi học và đi làm thuận tiện nhất.

---

## Tech Stack
* **Frontend:** HTML, JavaScript, Tailwind CSS, Leaflet.js
* **Backend:** FastAPI, Motor
* **Database:** MongoDB 

---

## Hướng dẫn sử dụng

### Database
* Tải và cài đặt **MongoDB**.

### Environment Variables
- Tìm file `.env.example` trong thư mục **backend**.
- Đổi tên thành `.env`.
- Chỉnh sửa các biến môi trường bên trong cho phù hợp với cấu hình MongoDB của bạn.
> **Lưu ý:** Nếu bạn không thiết lập `MONGO_USER` và `MONGO_PASSWORD` cho database, hãy comment hai dòng đó lại.

### Backend
Thực hiện các bước sau trong Terminal:

```bash
cd backend

# Windows: 
python -m venv .venv
.venv\Scripts\activate

# Linux/macOS:
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
fastapi dev app/main.py
```

---

### Sử dụng

* **API:** Sau khi chạy backend thành công, truy cập API Docs tại:  
    [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

* **Frontend:**
    - Bấm **Go Live** ở góc dưới bên phải màn hình (Yêu cầu đã cài đặt Extension *Live Server*).
    - Truy cập bản đồ tại:  
    [http://localhost:5500](http://localhost:5500)
       
---

## Thuật toán

Điểm đặc biệt của thuật toán nằm ở tham số **Penalty**.
Trong khi thuật toán $A^*$ truyền thống chỉ tập trung vào việc cực tiểu hóa hàm chi phí $f(n)$ dựa trên khoảng cách:

$$f(n) = g(n) + h(n)$$

Thuật toán này áp dụng thêm hệ số **Penalty**, coi như trọng số *weight* cho các line *transfer*.
* **Với Penalty = 0:** Thuật toán hoạt động như $A^*$ thuần túy, tìm đường ngắn nhất tuyệt đối về mặt địa lý.
* **Với Penalty = n:** Mỗi lần chuyển tuyến tương đương đi thêm n (mét). Thuật toán
sẽ tính toán để làm giảm số lần chuyển tuyến.