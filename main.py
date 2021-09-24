#
# フレームバッファを直接叩いてスクショを撮る 
#
import sys, os
from DotenvLoader import load_dotenv
from datetime import datetime
from dateutil import tz
from typing import List

def main(args: List[str]) -> int:
    # 環境変数読み込み
    load_dotenv(__file__)

    # フレームバッファ取得
    framebuffer_path = os.getenv("FRAMEBUFFER_PATH")
    if framebuffer_path is None:
        print("Please specify the path to the framebuffer in FRAMEBUFFER_PATH.")
        return 1
    
    with open(framebuffer_path, 'rb') as frame_buffer:
        data: bytes = frame_buffer.read()

    # ファイル名生成
    now = datetime.now(tz.tzlocal())
    file_name_fmt = "screen_shot_%Y_%m_%d_%H_%M_%S.bin"
    file_name = now.strftime(file_name_fmt)

    # 書き込み
    save_dir = os.getenv("SCREENSHOT_SAVE_PATH")
    if save_dir is None:
        print("Please specify the path to the save path in SCREENSHOT_SAVE_PATH.")
        return 1

    with open(f"{save_dir}/{file_name}", "wb") as file:
        file.write(data)

    return 0

if __name__ == "__main__":
    result = 0
    try:
        result = main(sys.argv) or 0
    except KeyboardInterrupt: 
        print("Ctrl+C")
        exit(result)
