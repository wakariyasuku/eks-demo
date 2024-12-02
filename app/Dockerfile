# ベースイメージとしてPython 3.11を使用
FROM python:3.11

# OSのパッケージを更新
RUN apt-get update && apt-get upgrade -y && apt-get clean

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY app.py .

# Streamlitアプリケーションを起動
CMD ["streamlit", "run", "app.py", "--server.port=8501"]
