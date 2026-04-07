**Test 1**
{"timestamp": "2026-04-07T09:25:12.320940", "event": "USER_INPUT", "data": {"input": "Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu."}}
{"timestamp": "2026-04-07T09:25:16.172354", "event": "LLM_METRIC", "data": {"provider": "Azure", "model": "gpt-4o", "prompt_tokens": 734, "completion_tokens": 166, "total_tokens": 900, "latency_ms": 3844, "cost_estimate": 0.009000000000000001}}
Trả lời trực tiếp
{"timestamp": "2026-04-07T09:25:16.174510", "event": "AGENT_DIRECT_RESPONSE", "data": {"content": "Chào bạn! Việc chọn địa điểm du lịch phụ thuộc vào sở thích và ngân sách của bạn. Bạn có thể chia sẻ thêm thông tin như:\n\n1. **Bạn muốn đi những kiểu địa điểm nào?** (Ví dụ: biển, núi, thành phố sôi động, văn hóa lịch sử,...)\n2. **Ngân sách dự kiến là bao nhiêu?** (Tổng chi phí cho cả chuyến đi hoặc ngân sách hàng ngày).\n3. **Thời gian bạn có thể đi?** (Ví dụ: trong tuần/một ngày cụ thể hay cuối tuần).\n4. **Điểm xuất phát của bạn ở đâu?** (Ví dụ: Hà Nội, Hồ Chí Minh,...)\n\nCung cấp thêm chi tiết nhé, mình tư vấn cụ thể hơn!"}}

**Test 2**
{"timestamp": "2026-04-07T09:27:24.358452", "event": "USER_INPUT", "data": {"input": "TÌm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng"}}
{"timestamp": "2026-04-07T09:27:26.510569", "event": "LLM_METRIC", "data": {"provider": "Azure", "model": "gpt-4o", "prompt_tokens": 735, "completion_tokens": 26, "total_tokens": 761, "latency_ms": 2148, "cost_estimate": 0.0076100000000000004}}
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
{"timestamp": "2026-04-07T09:27:26.511568", "event": "AGENT_TOOL_CALL", "data": {"tool_name": "search_flights", "arguments": {"origin": "Hà Nội", "destination": "Đà Nẵng"}}}
{"timestamp": "2026-04-07T09:27:29.520482", "event": "LLM_METRIC", "data": {"provider": "Azure", "model": "gpt-4o", "prompt_tokens": 902, "completion_tokens": 172, "total_tokens": 1074, "latency_ms": 2996, "cost_estimate": 0.010740000000000001}}
Trả lời trực tiếp
{"timestamp": "2026-04-07T09:27:29.522407", "event": "AGENT_DIRECT_RESPONSE", "data": {"content": "Chuyến bay từ Hà Nội đi Đà Nẵng:\n\n- **Vietnam Airlines**:  \n  - 06:00 -> 07:20 | Giá: 1.450.000 VNĐ (hạng economy)  \n  - 14:00 -> 15:20 | Giá: 2.800.000 VNĐ (hạng business)  \n\n- **VietJet Air**:  \n  - 08:30 -> 09:50 | Giá: 890.000 VNĐ (hạng economy)  \n\n- **Bamboo Airways**:  \n  - 11:00 -> 12:20 | Giá: 1.200.000 VNĐ (hạng economy)  \n\nBạn thích chuyến nào nhất? Tôi sẽ tư vấn tiếp nếu bạn cần đặt phòng hoặc chi tiết thêm nhé!"}}

**Test 3**
{"timestamp": "2026-04-07T09:29:07.646252", "event": "USER_INPUT", "data": {"input": "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp !"}}
{"timestamp": "2026-04-07T09:29:10.224237", "event": "LLM_METRIC", "data": {"provider": "Azure", "model": "gpt-4o", "prompt_tokens": 744, "completion_tokens": 67, "total_tokens": 811, "latency_ms": 2574, "cost_estimate": 0.008110000000000001}}
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
{"timestamp": "2026-04-07T09:29:10.225233", "event": "AGENT_TOOL_CALL", "data": {"tool_name": "search_flights", "arguments": {"origin": "Hà Nội", "destination": "Phú Quốc"}}}
Gọi tool: search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 2500000})
{"timestamp": "2026-04-07T09:29:10.226233", "event": "AGENT_TOOL_CALL", "data": {"tool_name": "search_hotels", "arguments": {"city": "Phú Quốc", "max_price_per_night": 2500000}}}
Đang gửi request tới Azure OpenAI...
{"timestamp": "2026-04-07T09:29:11.733655", "event": "LLM_METRIC", "data": {"provider": "Azure", "model": "gpt-4o", "prompt_tokens": 1339, "completion_tokens": 40, "total_tokens": 1379, "latency_ms": 1491, "cost_estimate": 0.01379}}
Gọi tool: calculate_budget({'total_budget': 5000000, 'expenses': 'vé_máy_bay:1100000,khách_sạn:1600000'})
{"timestamp": "2026-04-07T09:29:11.734655", "event": "AGENT_TOOL_CALL", "data": {"tool_name": "calculate_budget", "arguments": {"total_budget": 5000000, "expenses": "vé_máy_bay:1100000,khách_sạn:1600000"}}}
Đang gửi request tới Azure OpenAI...
{"timestamp": "2026-04-07T09:29:14.932606", "event": "LLM_METRIC", "data": {"provider": "Azure", "model": "gpt-4o", "prompt_tokens": 1459, "completion_tokens": 284, "total_tokens": 1743, "latency_ms": 3187, "cost_estimate": 0.01743}}
Trả lời trực tiếp
{"timestamp": "2026-04-07T09:29:14.933610", "event": "AGENT_DIRECT_RESPONSE", "data": {"content": "Dựa trên ngân sách 5 triệu của bạn, đây là gợi ý cho chuyến đi:\n\n**Chuyến bay:**  \n- VietJet Air: Khởi hành lúc 16:00, đến lúc 18:15 | Giá: 1.100.000 VNĐ  \n(Điều kiện hạng economy, tiết kiệm nhất)\n\n**Khách sạn:**  \n- Lahana Resort (3 sao): Khu vực Dương Đông | Đánh giá 4.0/5.0 | Giá: 800.000 VNĐ/đêm  \n=> Tổng chi phí khách sạn cho 2 đêm: 1.600.000 VNĐ  \n\n**Tổng chi phí ước tính:** 2.700.000 VNĐ  \nBạn sẽ còn dư: 2.300.000 VNĐ (dùng cho ăn uống, di chuyển và vui chơi).\n\n**Gợi ý thêm:**  \n- Với khoản dư, bạn có thể thoải mái thưởng thức hải sản, tham quan VinWonders Phú Quốc, hoặc thử lặn ngắm san hô.  \n- Nếu muốn tiết kiệm hơn, bạn có thể chọn ở hostel như 9Station Hostel với giá chỉ 200.000 VNĐ/đêm.\n\nBạn thấy kế hoạch này ổn không? Hoặc nếu cần gợi ý thêm, cứ nói nhé!"}}

**Test 4**
{"timestamp": "2026-04-07T09:32:02.310198", "event": "USER_INPUT", "data": {"input": "Tôi muốn đặt khách sạn"}}
{"timestamp": "2026-04-07T09:32:05.623434", "event": "LLM_METRIC", "data": {"provider": "Azure", "model": "gpt-4o", "prompt_tokens": 725, "completion_tokens": 65, "total_tokens": 790, "latency_ms": 3308, "cost_estimate": 0.0079}}
Trả lời trực tiếp
{"timestamp": "2026-04-07T09:32:05.624476", "event": "AGENT_DIRECT_RESPONSE", "data": {"content": "Bạn vui lòng cho biết rõ hơn những thông tin sau để mình tư vấn nhé:  \n- Thành phố bạn muốn tìm khách sạn?  \n- Ngân sách tối đa cho mỗi đêm nghỉ (nếu có)?  \n- Ngày bạn dự định check-in và check-out (nếu cần)?  "}}

**Test 5**
{"timestamp": "2026-04-07T09:32:58.950556", "event": "USER_INPUT", "data": {"input": "Giải giúp tôi bài tập lập trình về Python"}}
{"timestamp": "2026-04-07T09:33:01.252958", "event": "LLM_METRIC", "data": {"provider": "Azure", "model": "gpt-4o", "prompt_tokens": 728, "completion_tokens": 50, "total_tokens": 778, "latency_ms": 2298, "cost_estimate": 0.0077800000000000005}}
Trả lời trực tiếp
{"timestamp": "2026-04-07T09:33:01.253960", "event": "AGENT_DIRECT_RESPONSE", "data": {"content": "Mình chỉ chuyên về tư vấn du lịch thôi, không thể giúp bạn giải bài tập lập trình được. Nếu bạn cần lên kế hoạch cho chuyến đi hoặc tìm kiếm khách sạn hay vé máy bay thì cứ hỏi mình nhé!"}}
