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
    ],
}

@tool
def search_flights(origin: str, destination: str) -> str:
    '''
    Tìm kiếm các chuyến bay giữa hai thành phố
    Tham số:
    - origin: thành phố khởi hành (ví dụ: 'Hà Nội', 'Hồ Chí Minh')
    - destination: thành phố đến (ví dụ: 'Đà Nẵng', 'Phú Quốc')
    Trả về danh sách chuyến bay với hãng, giờ bay và giá vé.
    Nếu không tìm thấy chuyến bay, trả về dòng thông báo không có chuyến
    '''

    flights = FLIGHTS_DB.get((origin, destination))
    
    if not flights:
        return f"Không tìm thấy chuyến bay nào từ {origin} đến {destination}."
    
    # Định dạng kết quả nếu tìm thấy
    result_lines = [f"Các chuyến bay từ {origin} đến {destination}:"]
    
    for flight in flights:
        airline = flight["airline"]
        departure = flight["departure"]
        arrival = flight["arrival"]
        flight_class = flight["class"]
        
        # Format giá tiền: dùng dấu phẩy phân cách hàng nghìn rồi đổi thành dấu chấm
        formatted_price = f"{flight['price']:,}".replace(",", ".") + " VNĐ"
        
        # Tạo chuỗi thông tin cho từng chuyến bay
        flight_info = f"- {airline}: {departure} -> {arrival} | Giá: {formatted_price} (Hạng: {flight_class})"
        result_lines.append(flight_info)
        
    return "\n".join(result_lines)

@tool
def search_hotels(city: str, max_price_per_night: int = 99999999) -> str:
    """
    Tìm khách sạn tại một thành phố, có thể lọc theo giá tối đa mỗi đêm.
    Tham số:
    - city: Tên thành phố (ví dụ: 'Hà Nội', 'Đà Nẵng')
    - max_price_per_night: giá tối đa mỗi đêm (VNĐ)
    Trả về danh sách khách sạn phù hợp, với tên, số sao, giá, khu vực, rating
    """
    # Tra cứu danh sách khách sạn theo thành phố
    city_hotels = HOTELS_DB.get(city)
    
    # Trường hợp thành phố không tồn tại trong database
    if not city_hotels:
        return f"Không tìm thấy thông tin khách sạn nào tại {city}."
        
    # Lọc khách sạn theo max_price_per_night
    filtered_hotels = [hotel for hotel in city_hotels if hotel["price_per_night"] <= max_price_per_night]
    
    # Xử lý trường hợp có thành phố nhưng không có khách sạn nào thỏa mãn mức giá
    if not filtered_hotels:
        formatted_max_price = f"{max_price_per_night:,}".replace(",", ".")
        return f"Không tìm thấy khách sạn nào tại {city} với giá dưới {formatted_max_price} VNĐ. Hãy thử tăng ngân sách của bạn!"
        
    # Sắp xếp danh sách đã lọc theo rating giảm dần (reverse=True)
    filtered_hotels.sort(key=lambda x: x["rating"], reverse=True)
    
    # Định dạng kết quả đầu ra
    result_lines = [f"Các khách sạn phù hợp tại {city} (Sắp xếp theo rating):"]
    
    for hotel in filtered_hotels:
        name = hotel["name"]
        stars = "⭐" * hotel["stars"] # Hiển thị số sao bằng icon cho trực quan
        rating = hotel["rating"]
        area = hotel["area"]
        
        # Format giá tiền: dùng dấu phẩy phân cách hàng nghìn rồi đổi thành dấu chấm
        formatted_price = f"{hotel['price_per_night']:,}".replace(",", ".") + " VNĐ"
        
        # Tạo chuỗi thông tin cho từng khách sạn
        hotel_info = f"- {name} {stars} | Đánh giá: {rating}/5.0 | Khu vực: {area} | Giá: {formatted_price}/đêm"
        result_lines.append(hotel_info)
        
    return "\n".join(result_lines)


@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """
    Tính toán ngân sách còn lại sau khi trừ các khoản chi phí.
    Tham số:
    - total_budget: tổng ngân sách ban đầu (VNĐ)
    - expenses: chuỗi mô tả các khoản chi, mỗi khoản cách nhau bởi dấu phẩy, 
      định dạng 'tên_khoản:số_tiền' (VD: 'vé_máy_bay:890000,khách_sạn:650000')
    Trả về bảng chi tiết các khoản chi và số tiền còn lại.
    Nếu vượt ngân sách, cảnh báo rõ ràng số tiền thiếu.
    """
    
    # Xử lý trường hợp chuỗi expenses rỗng
    if not expenses.strip():
        return "Không có khoản chi phí nào được ghi nhận."

    parsed_expenses = {}
    total_cost = 0

    # Parse chuỗi expenses thành dict
    items = expenses.split(',')
    for item in items:
        # Xử lý lỗi: nếu expenses format sai
        parts = item.split(':')
        if len(parts) != 2:
            return f"Lỗi định dạng: '{item.strip()}' không đúng cấu trúc 'tên_khoản:số_tiền'."
        
        name, amount_str = parts
        name = name.strip()
        amount_str = amount_str.strip()
        
        try:
            amount = int(amount_str)
        except ValueError:
            return f"Lỗi định dạng: Số tiền '{amount_str}' của khoản '{name}' không hợp lệ."
        
        # Làm đẹp tên khoản chi (VD: 'vé_máy_bay' -> 'Vé máy bay')
        formatted_name = name.replace('_', ' ').capitalize()
        parsed_expenses[formatted_name] = amount
        total_cost += amount

    # Tính toán
    remaining = total_budget - total_cost

    # Hàm phụ để định dạng số tiền (VD: 1000000 -> 1.000.000đ)
    def format_money(amount: int) -> str:
        return f"{amount:,}".replace(",", ".") + "đ"

    # Format bảng chi tiết
    result_lines = ["Bảng chi phí:"]
    for name, amount in parsed_expenses.items():
        result_lines.append(f"  - {name}: {format_money(amount)}")
        
    result_lines.append("  ---")
    result_lines.append(f"  Tổng chi: {format_money(total_cost)}")
    result_lines.append(f"  Ngân sách: {format_money(total_budget)}")
    
    # Kiểm tra vượt ngân sách
    if remaining >= 0:
        result_lines.append(f"  Còn lại: {format_money(remaining)}")
    else:
        result_lines.append(f"  Còn lại: {format_money(remaining)}")
        result_lines.append(f"Vượt ngân sách {format_money(abs(remaining))}! Cần điều chỉnh.")

    return "\n".join(result_lines)

# --- Code test thử ---
# expenses_str = "vé_máy_bay:890000,khách_sạn:650000,ăn_uống:1500000"
# print(calculate_budget(5000000, expenses_str))
# print("="*40)
# print(calculate_budget(2000000, expenses_str)) # Trường hợp bị âm tiền
# print("="*40)
# print(calculate_budget(5000000, "vé_máy_bay_890000")) # Trường hợp lỗi format
