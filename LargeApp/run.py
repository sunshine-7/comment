# Run a test server.
import sys

# for i in sys.path:
#     print(i)

from app import app
# app1.run(host='0.0.0.0', port=8080, debug=True)
app.run()

