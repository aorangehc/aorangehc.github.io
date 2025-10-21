#!/usr/bin/env python3
"""
简单的静态文件服务器，用于本地预览Jekyll网站
"""

import http.server
import socketserver
import os
import sys
import webbrowser
from pathlib import Path

# 配置
PORT = 4000
DIRECTORY = "."

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # 添加CORS头，允许跨域访问
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def guess_type(self, path):
        # 确保正确的MIME类型
        result = super().guess_type(path)
        if isinstance(result, tuple):
            mimetype, encoding = result
        else:
            mimetype, encoding = result, None
            
        if path.endswith('.yml') or path.endswith('.yaml'):
            return 'text/yaml'
        if path.endswith('.md'):
            return 'text/markdown'
        return mimetype

def main():
    # 检查是否在正确的目录
    if not os.path.exists('_config.yml'):
        print("❌ 错误：未找到 _config.yml 文件")
        print("请确保在Jekyll项目根目录下运行此脚本")
        sys.exit(1)
    
    print("🚀 启动Jekyll网站预览服务器...")
    print(f"📁 服务目录: {os.path.abspath(DIRECTORY)}")
    print(f"🌐 访问地址: http://localhost:{PORT}")
    print("📝 注意：这是静态文件预览，不包含Jekyll的动态功能")
    print("💡 要查看完整功能，请使用GitHub Pages或Jekyll服务器")
    print("-" * 50)
    
    try:
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print(f"✅ 服务器已启动在端口 {PORT}")
            print("按 Ctrl+C 停止服务器")
            
            # 自动打开浏览器
            try:
                webbrowser.open(f'http://localhost:{PORT}')
                print("🌐 已自动打开浏览器")
            except:
                print("⚠️  无法自动打开浏览器，请手动访问 http://localhost:4000")
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 服务器已停止")
    except OSError as e:
        if e.errno == 10048:  # Windows端口被占用
            print(f"❌ 端口 {PORT} 已被占用，请尝试其他端口或关闭占用该端口的程序")
        else:
            print(f"❌ 启动服务器时出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()