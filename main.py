#
# フレームバッファを直接叩いてスクショを撮る 
#
import sys, os
from DotenvLoader import load_dotenv
from datetime import datetime
from dateutil import tz
from typing import List, Optional

def main(args: List[str]) -> int:
    # 環境変数読み込み
    load_dotenv(__file__)

    framebuffer_path = os.getenv("FRAMEBUFFER_PATH")
    if framebuffer_path is None:
        print("Please specify the path to the framebuffer in FRAMEBUFFER_PATH.")
        return 1
    
    save_dir = os.getenv("SCREENSHOT_SAVE_PATH")
    if save_dir is None:
        print("Please specify the path to the save path in SCREENSHOT_SAVE_PATH.")
        return 1

    command: str = input("> ")
    while command.find("q") == -1:

        # フレームバッファ取得
        data = get_frame_buffer(framebuffer_path)

        if data is None:
            print(f"Couldn't read frame-buffer: {framebuffer_path}")
            return 1

        # ファイル名生成
        now = datetime.now(tz.tzlocal())
        file_name = create_file_name("screen_shot", "bin", now)
        print(file_name)

        # 書き込み
        with open(f"{save_dir}/{file_name}", "wb") as file:
            file.write(data)

        command = input("> ")

    return 0

def get_frame_buffer(buffer_path: str) -> Optional[bytes]:
    """
    フレームバッファの内容をbytes形式で取得する。

    Args:
        buffer_path (str) : フレームバッファを示すファイルパス。
    
    Returns:
        Optional[bytes] : フレームバッファの内容。
    """

    try:
        with open(buffer_path, 'rb') as frame_buffer:
            data: Optional[bytes] = None
            if frame_buffer.readable():
                data = frame_buffer.read()
        
        return data

    except FileNotFoundError:
        return None    

def create_file_name(prefix: str, suffix: str, date_ref: datetime):
    """
    datetimeをフォーマットし、prefixおよびsuffixと結合して返します。

    Args:
        prefix (str) : 接頭語。
        suffix (str) : 接尾語。
        date_ref (datetime) : フォーマット対象となるdatetime。

    Returns:
        str : フォーマット結果。 {prefix}_{date_ref}.{suffix} の形式で帰ります。
    """
    return date_ref.strftime(f"{prefix}_%Y_%m_%d_%H_%M_%S.{suffix}")

if __name__ == "__main__":
    result = 0
    try:
        result = main(sys.argv) or 0
    except KeyboardInterrupt: 
        print("Ctrl+C")
        exit(result)
