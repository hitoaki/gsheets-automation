import json
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# GitHub Secrets から環境変数として渡された JSON 文字列を読み込み
creds_json = os.environ.get("GOOGLE_CREDENTIALS")
if not creds_json:
    raise ValueError("GOOGLE_CREDENTIALS environment variable is not set.")

# JSON 文字列を辞書に変換
creds_dict = json.loads(creds_json)

# Google Sheets API と Drive API のスコープを指定
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# サービスアカウント認証を作成
credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

# gspread クライアントの認証
gc = gspread.authorize(credentials)

# 対象のスプレッドシート名（必ず存在し、共有されていること）
spreadsheet = gc.open("Noke Hour Data")
worksheet = spreadsheet.sheet1

# 書き込むデータ（任意に変更可）
worksheet.append_row(["2025-05-10", "GitHub Actions 成功", "Secrets 経由で連携完了！"])

print("✅ Google Sheets に正常に書き込みました。")
