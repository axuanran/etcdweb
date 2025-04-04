from flask import Flask, request, jsonify, send_from_directory
from etcd3 import client
from flask_cors import CORS

app = Flask(__name__, static_folder='static')  # 指定静态文件目录
CORS(app)

# 配置ETCD连接（根据实际情况修改）
ETCD_HOST = '192.168.9.105'
ETCD_PORT = 2379

# 初始化ETCD客户端
etcd = client(host=ETCD_HOST, port=ETCD_PORT)

@app.route('/')
def index():
    """返回前端 HTML 页面"""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/etcd', methods=['POST'])
def handle_kv():
    data = request.json
    success = 0
    errors = []

    for item in data:
        key = item['key']
        value = item['value']

        try:
            etcd.put(key, value)
            success += 1
        except Exception as e:
            errors.append(f"{key}: {str(e)}")

    return jsonify({
        'successCount': success,
        'errors': errors
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)