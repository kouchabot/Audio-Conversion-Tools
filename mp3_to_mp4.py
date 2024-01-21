import ffmpeg
import os

# 入力ファイルのパスをユーザーに入力させる
input_file = input("変換するファイルのパスを指定してください: ")

# 入力ファイルと出力ストリームを設定
input_stream = ffmpeg.input(input_file)
audio = input_stream.audio

# 出力ファイルの名前を入力させる
output_file_name = input("変換が完了しました。ファイル名を決めてください（拡張子不要）: ")

# ユーザーに保存先のパスを入力させる
output_path = input("保存先のパスを入力してください: ")

# 完全な出力ファイルパスの生成
output_file = os.path.join(output_path, f"{output_file_name}.mp3")

# 出力ストリームの設定
output_stream = ffmpeg.output(audio, output_file)

# 実行
ffmpeg.run(output_stream)

# 完了メッセージ
print(f"ファイルは {output_file} に保存されました。")

