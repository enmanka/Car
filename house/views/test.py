from flask import Flask, send_file
import os

app = Flask(__name__)


def getPaths(directory):
    paths = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        paths.append(path)

    return paths


# 文件下载
@app.route("/download/<file>")
def download(file):
    return send_file("D:/pyh/" + file, as_attachment=True)


def list_files_and_directories(directory):
    files = []
    directories = []

    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        print(path)
        if os.path.isfile(path):
            files.append(filename)
        else:
            files.append(filename)
            directories.append(filename)

    return files, directories


@app.route("/")
def browse_directory():
    # 获取 文件目录及文件名
    paths = getPaths("D:/pyh/")

    # 将 文件名 拼接到 html 中
    html = "<h1>Files:</h1>"
    for ph in paths:
        print(type(file))

    #     html += f"<p><a href ='/download/{file}'>{file}</a></p>"
    #
    # # 将 文件目录 拼接到 html 中
    # html += "<h1>Directories:</h1>"
    # for directory in directories:
    #     html += f"<p>{directory}</p>"
    #

    # 响应结果
    return html


if __name__ == '__main__':
    app.run()
