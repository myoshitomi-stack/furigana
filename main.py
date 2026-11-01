import os
from fastapi import FastAPI
from pykakasi import kakasi
import uvicorn

app = FastAPI()

# 漢字を「ひらがな」に変換する設定
kks = kakasi()
kks.setMode("J", "H")
converter = kks.getConverter()


@app.get("/")
def read_root():
  return {"status": "ok"}


@app.get("/kanji2kana")
def convert_kanji(text: str = ""):
  if not text:
    return {"result": ""}
  # 漢字をひらがなに変換
  result = converter.do(text)
  return {"result": result}


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 8080))
  uvicorn.run(app, host="0.0.0.0", port=port)