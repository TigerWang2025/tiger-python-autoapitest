import os
import shutil
import sys


def invalidate_pycharm_caches():
    """
    清除 PyCharm 缓存的完整流程
    """
    # 获取 PyCharm 缓存目录路径
    cache_paths = []

    # 根据操作系统确定缓存路径
    if sys.platform.startswith('win'):
        # Windows 系统
        user_dir = os.path.expanduser('~')
        cache_paths = [
            os.path.join(user_dir, '.PyCharm2024', 'system', 'caches'),
            os.path.join(user_dir, 'AppData', 'Local', 'JetBrains', 'PyCharm2024', 'caches')
        ]
    elif sys.platform.startswith('darwin'):
        # macOS 系统
        user_dir = os.path.expanduser('~')
        cache_paths = [
            os.path.join(user_dir, 'Library', 'Caches', 'JetBrains', 'PyCharm2024', 'caches')
        ]
    else:
        # Linux 系统
        user_dir = os.path.expanduser('~')
        cache_paths = [
            os.path.join(user_dir, '.cache', 'JetBrains', 'PyCharm2024', 'caches')
        ]

    # 清理所有可能的缓存目录
    for cache_path in cache_paths:
        if os.path.exists(cache_path):
            try:
                print(f"正在清理缓存目录: {cache_path}")
                shutil.rmtree(cache_path)
                print(f"缓存目录已成功删除: {cache_path}")
            except Exception as e:
                print(f"删除缓存目录失败 {cache_path}: {e}")
        else:
            print(f"缓存目录不存在: {cache_path}")

    print("PyCharm 缓存清理完成，请重启 PyCharm")


if __name__ == "__main__":
    invalidate_pycharm_caches()
