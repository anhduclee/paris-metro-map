# Paris Metro Map

## Giới thiệu
Đây là một dự án đầy tâm huyết của tác giả giúp giải quyết vấn đề tìm đường đi trong mạng lưới metro dày đặc của Paris, phục vụ cho bà con nhân dân có trải nghiệm đi học và đi làm thuận tiện nhất.

---

## Tech Stack
* **Frontend:** HTML, JavaScript, Tailwind, Leaflet
* **Backend:** FastAPI
* **Database:** MongoDB

---

## Requirements
* Docker

---

## Hướng dẫn

```bash
# .env
cp ./backend/.env.example ./backend/.env
# Install
docker compose up -d
# Uninstall
docker compose down -v --rmi local
```

## Test
* **Backend:**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **Frontend:** [http://localhost:5500/frontend](http://localhost:5500/frontend)

---

## Thuật toán

Điểm đặc biệt của thuật toán nằm ở tham số **Penalty**.
Trong khi thuật toán $A^*$ truyền thống chỉ tập trung vào việc cực tiểu hóa khoảng cách địa lý:

$$f(n) = g(n) + h(n)$$

Thuật toán này áp dụng thêm hệ số **Penalty**, bản chất là trọng số cho các cạnh chuyển tuyến.
* **Với Penalty = 0:** Thuật toán hoạt động như $A^*$ thuần túy, tìm đường ngắn nhất tuyệt đối về mặt địa lý.
* **Với Penalty = n:** Mỗi lần chuyển tuyến tương đương đi thêm *n* mét. Khi **Penalty** tăng lên, thuật toán sẽ ưu tiên lộ trình ít phải đổi tàu hơn.