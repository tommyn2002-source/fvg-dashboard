import subprocess
import shutil
import os

CSV_SOURCE = r"C:\Users\tommyn2002\AppData\Roaming\MetaQuotes\Terminal\Common\Files\FVG_Bot_Logs\FVG_Bot_Trades.csv"
REPO_PATH  = r"C:\FVGDashboard"
DEST_FILE  = os.path.join(REPO_PATH, "FVG_Bot_Trades.csv")

try:
    if os.path.exists(CSV_SOURCE):
        shutil.copy(CSV_SOURCE, DEST_FILE)
        subprocess.run(["git", "-C", REPO_PATH, "add", "."], check=True)
        subprocess.run(["git", "-C", REPO_PATH, "commit", "-m", "auto sync"], capture_output=True)
        subprocess.run(["git", "-C", REPO_PATH, "push"], check=True)
        print("CSV synced successfully")
    else:
        print("CSV file not found")
except Exception as e:
    print("Error:", e)