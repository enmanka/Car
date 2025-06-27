from house.config import app
from house.views.data_view import data
from house.views.page_view import page

app.register_blueprint(data, url_prefix="/data")
app.register_blueprint(page, url_prefix="/")


# 2113041705 赵嵘
# 2113042911 何其明
# 2113041206 康美玉
# 曹鑫荣
# 2113040548 杜委旗
# 2113041704 张嘉祺
# 2113041221 李浩然
# 2113040819 李鑫

if __name__ == '__main__':
    app.run()
