from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from tools import search_flights, search_hotels, calculate_budget 
from dotenv import load_dotenv

load_dotenv()

# Đọc prompt hệ thống
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# Thiết lập LLM và Tools
tools_list = [search_flights, search_hotels, calculate_budget]
llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools(tools_list)

def agent_node(state: AgentState):
    messages = state["messages"]
    # Thêm SystemMessage vào đầu nếu chưa có
    if not any(isinstance(m, SystemMessage) for m in messages):
        messages = [SystemMessage(content=system_prompt)] + messages

    response = llm_with_tools.invoke(messages)

    if response.tool_calls:
        for tc in response.tool_calls:
            print(f"--- Gọi tool: {tc['name']} ---")
    else:
        print("--- Trả lời trực tiếp ---")

    return {"messages": [response]}

# 1. Khởi tạo Builder
builder = StateGraph(AgentState)

# 2. Thêm các Nodes
builder.add_node("agent", agent_node)
tool_node = ToolNode(tools_list)
builder.add_node("tools", tool_node)


# Bắt đầu luồng tại agent
builder.add_edge(START, "agent")

# Kiểm tra điều kiện: Nếu LLM yêu cầu gọi tool thì sang node 'tools', nếu không thì kết thúc
builder.add_conditional_edges(
    "agent",
    tools_condition,
)

# Sau khi tool thực thi xong, bắt buộc quay lại agent để tổng hợp câu trả lời
builder.add_edge("tools", "agent")

# Compile Graph
graph = builder.compile()

if __name__ == "__main__":
    print("=" * 60)
    print("TravelBuddy - Trợ lý du lịch cá nhân của bạn!")
    print("   Gõ 'exit' để kết thúc cuộc trò chuyện.")
    print("=" * 60)

    while True:
        user_input = input("Bạn: ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("TravelBuddy: Hẹn gặp lại! Chúc bạn có những chuyến đi tuyệt vời!")
            break

        print("\nTravelBuddy đang suy nghĩ...")
        # Sử dụng stream hoặc invoke để nhận kết quả cuối cùng
        result = graph.invoke({"messages": [{ "role": "human", "content": user_input }]})
        
        # Lấy tin nhắn cuối cùng trong danh sách
        final_message = result["messages"][-1]
        print(f"\nTravelBuddy: {final_message.content}\n")
