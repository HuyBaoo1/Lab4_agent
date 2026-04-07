from langchain_core.tools import tool


FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1_450_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "14:00", "arrival": "15:20", "price": 2_800_000, "class": "business"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "11:00", "arrival": "12:20", "price": 1_200_000, "class": "economy"},
    ],
    ("Hà Nội", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1_350_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "16:00", "arrival": "18:15", "price": 1_100_000, "class": "economy"},
    ],
    ("Hà Nội", "Hồ Chí Minh"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "08:10", "price": 1_600_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "07:30", "arrival": "09:40", "price": 950_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "12:00", "arrival": "14:10", "price": 1_300_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3_200_000, "class": "business"},
    ],
    ("Hồ Chí Minh", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "09:00", "arrival": "10:20", "price": 1_300_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "13:00", "arrival": "14:20", "price": 780_000, "class": "economy"},
    ],
    ("Hồ Chí Minh", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "08:00", "arrival": "09:00", "price": 1_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "15:00", "arrival": "16:00", "price": 650_000, "class": "economy"},
    ],
}

HOTELS_DB = {
    "Đà Nẵng": [
        {"name": "Mường Thanh Luxury", "stars": 5, "price_per_night": 1_800_000, "area": "Mỹ Khê", "rating": 4.5},
        {"name": "Sala Danang Beach", "stars": 4, "price_per_night": 1_200_000, "area": "Mỹ Khê", "rating": 4.3},
        {"name": "Fivitel Danang", "stars": 3, "price_per_night": 650_000, "area": "Sơn Trà", "rating": 4.1},
        {"name": "Memory Hostel", "stars": 2, "price_per_night": 250_000, "area": "Hải Châu", "rating": 4.6},
        {"name": "Christina's Homestay", "stars": 2, "price_per_night": 350_000, "area": "An Thượng", "rating": 4.7},
    ],
    "Phú Quốc": [
        {"name": "Vinpearl Resort", "stars": 5, "price_per_night": 3_500_000, "area": "Bãi Dài", "rating": 4.4},
        {"name": "Sol by Meliá", "stars": 4, "price_per_night": 1_500_000, "area": "Bãi Trường", "rating": 4.2},
        {"name": "Lahana Resort", "stars": 3, "price_per_night": 800_000, "area": "Dương Đông", "rating": 4.0},
        {"name": "9Station Hostel", "stars": 2, "price_per_night": 200_000, "area": "Dương Đông", "rating": 4.5},
    ],
    "Hồ Chí Minh": [
        {"name": "Rex Hotel", "stars": 5, "price_per_night": 2_800_000, "area": "Quận 1", "rating": 4.3},
        {"name": "Liberty Central", "stars": 4, "price_per_night": 1_400_000, "area": "Quận 1", "rating": 4.1},
        {"name": "Cochin Zen Hotel", "stars": 3, "price_per_night": 550_000, "area": "Quận 3", "rating": 4.4},
        {"name": "The Common Room", "stars": 2, "price_per_night": 180_000, "area": "Quận 1", "rating": 4.6},
    ]
}

def format_vnd(amount: int) -> str:
    return f"{amount:,.0f}đ".replace(",", ".")

@tool
def search_flights(origin: str, destination: str) -> str:
    # Tra cứu chiều đi
    #is_weekend: true nếu là cuối tuần
    flights = FLIGHTS_DB.get((origin, destination))
    
    # Thử tra cứu ngược lại nếu không thấy
    if not flights:
        flights = FLIGHTS_DB.get((destination, origin))
        
    if not flights:
        return f"Không tìm thấy chuyến bay từ {origin} đến {destination}."

    result = [f"Danh sách chuyến bay giữa {origin} và {destination}:"]
    for f in flights:
        price_str = format_vnd(f['price'])
        result.append(f"- {f['airline']} ({f['class']}): {f['departure']} -> {f['arrival']} | Giá: {price_str}")
        
    return "\n".join(result)

@tool
def search_hotels(city: str, max_price_per_night: int = 999999999) -> str:
    hotels = HOTELS_DB.get(city)
    if not hotels:
        return f"Không tìm thấy dữ liệu khách sạn nào tại {city}."

    # Lọc khách sạn theo ngân sách
    filtered_hotels = [h for h in hotels if h["price_per_night"] <= max_price_per_night]

    if not filtered_hotels:
        return f"Không tìm thấy khách sạn tại {city} với giá dưới {format_vnd(max_price_per_night)}/đêm. Hãy thử tăng ngân sách."

    # Sắp xếp theo rating giảm dần
    filtered_hotels.sort(key=lambda x: x["rating"], reverse=True)

    result = [f"Danh sách khách sạn tại {city} (Ngân sách <= {format_vnd(max_price_per_night)}/đêm):"]
    for h in filtered_hotels:
        price_str = format_vnd(h['price_per_night'])
        result.append(f"- {h['name']} ({h['stars']} sao) | Khu vực: {h['area']} | Rating: {h['rating']} | Giá: {price_str}/đêm")

    return "\n".join(result)

@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    parsed_expenses = {}
    total_expense = 0

    # Xử lý chuỗi expenses và bắt lỗi format
    if expenses.strip():
        try:
            items = expenses.split(',')
            for item in items:
                if not item.strip():
                    continue
                name, price_str = item.split(':')
                price = int(price_str.strip())
                parsed_expenses[name.strip()] = price
                total_expense += price
        except ValueError:
            return "Lỗi: Đầu vào expenses sai định dạng. Vui lòng nhập đúng format 'tên_khoản:số_tiền,tên_khoản:số_tiền' (VD: vé_máy_bay:890000,khách_sạn:650000)."

    remaining_budget = total_budget - total_expense

    # Format bảng kết quả
    result = ["Bảng chi phí:"]
    for name, price in parsed_expenses.items():
        result.append(f"- {name.replace('_', ' ').capitalize()}: {format_vnd(price)}")
        
    result.append("---")
    result.append(f"Tổng chi: {format_vnd(total_expense)}")
    result.append(f"Ngân sách: {format_vnd(total_budget)}")
    result.append(f"Còn lại: {format_vnd(remaining_budget)}")

    # Nếu vượt ngân sách, thêm cảnh báo
    if remaining_budget < 0:
        result.append(f"\nCẢNH BÁO: Vượt ngân sách {format_vnd(abs(remaining_budget))}! Cần điều chỉnh.")

    return "\n".join(result)

