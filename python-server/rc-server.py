from jsonrpcserver import method, serve
import screen_brightness_control as sbc

# 方法用于接收并处理来自单片机的JSON请求
@method
def set_brightness(level: int):
    if 0 <= level <= 100:
        # 设置屏幕亮度
        sbc.set_brightness(level)
        return f"Brightness set to {level}%"
    else:
        return "Invalid brightness level. Must be between 0 and 100."

# 启动 JSON-RPC 服务器
if __name__ == "__main__":
    print("Starting JSON-RPC server...")
    serve()

