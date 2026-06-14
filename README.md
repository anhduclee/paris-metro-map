# Paris Metro Map

## Introduction
Đây là một dự án đầy tâm huyết của tác giả giúp giải quyết vấn đề tìm đường đi trong mạng lưới metro dày đặc của Paris, phục vụ cho bà con nhân dân có trải nghiệm đi học và đi làm thuận tiện nhất.

---

## Tech Stack
* **Frontend:** HTML, JavaScript, Tailwind CSS, Leaflet.js
* **Backend:** FastAPI (Python)
* **Database:** MongoDB
* **DevOps:** Docker, NGINX

---

## Requirements
* **Docker**

---

## Guide

```bash
# Install
docker compose up -d
# Stop
docker compose stop
# Start
docker compose start
# Uninstall
docker compose down -v --rmi all
```

## Test
* **Backend:**: [https://localhost/docs](https://localhost/docs)
* **Frontend:** [https://localhost](https://localhost)

---

## Thuật toán

Điểm đặc biệt của thuật toán nằm ở tham số **Penalty**.
Trong khi thuật toán $A^*$ truyền thống chỉ tập trung vào việc cực tiểu hóa khoảng cách địa lý:

$$f(n) = g(n) + h(n)$$

Thuật toán này áp dụng thêm hệ số **Penalty**, bản chất là trọng số cho các cạnh chuyển tuyến.
* **Với Penalty = 0:** Thuật toán hoạt động như $A^*$ thuần túy, tìm đường ngắn nhất tuyệt đối về mặt địa lý.
* **Với Penalty = n:** Mỗi lần chuyển tuyến tương đương đi thêm *n* mét. Khi **Penalty** tăng lên, thuật toán sẽ ưu tiên lộ trình ít phải đổi tàu hơn.