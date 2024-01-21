from pytube import YouTube
import ffmpeg
import os

# ユーザーからの入力を取得
url = input("YouTube動画のURLを入力してください: ")

# YouTubeオブジェクトの作成
yt = YouTube(url)

# 最高解像度のビデオストリームを選択しダウンロード
video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
downloaded_video_path = video_stream.download()

# ダウンロードしたファイルの拡張子をチェック
file_name, file_extension = os.path.splitext(downloaded_video_path)

# 拡張子に基づいてMP3に変換
if file_extension in ['.mp4', '.webm', '.3gp']:
    output_mp3 = f"{file_name}.mp3"
    (
        ffmpeg
        .input(downloaded_video_path)
        .output(output_mp3, format='mp3')
        .run()
    )
    print(f"MP3ファイルが保存されました: {output_mp3}")
else:
    print("サポートされていないファイル形式です。")
