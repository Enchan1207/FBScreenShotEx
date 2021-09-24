#
# フレームバッファを直接叩いてスクショを撮る 
#
import sys
from DotenvLoader import load_dotenv
from typing import List

def main(args: List[str]) -> int:
    # 環境変数読み込み
    load_dotenv(__file__)


    
    return 0

if __name__ == "__main__":
    result = 0
    try:
        result = main(sys.argv) or 0
    except KeyboardInterrupt: 
        print("Ctrl+C")
        exit(result)
