# Run a test server.
import sys

# for i in sys.path:
#     print(i)

from app import app
# from datetime import timedelta
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1) # 修改缓存时间，秒做单位
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=1) # 修改回话存活时间，秒做单位
# app1.run(host='0.0.0.0', port=8080, debug=True)
app.run()

