# get-timezone-time

Cursor Agent Skill — 通过 [TimeAPI](https://timeapi.io/) 获取指定时区的当前时间。

## 安装

将本仓库克隆到 Cursor skills 目录：

```bash
# 个人 skill（所有项目可用）
git clone https://github.com/<your-username>/skills-time.git ~/.cursor/skills/get-timezone-time

# 或作为项目 skill（仅当前项目可用）
git clone https://github.com/<your-username>/skills-time.git .cursor/skills/get-timezone-time
```

## 依赖

- Python 3.6+
- [requests](https://docs.python-requests.org/)

```bash
pip install -r requirements.txt
```

## 使用

安装后，在 Cursor 对话中直接问时间相关的问题即可自动触发：

- "现在上海几点了？"
- "纽约现在什么时间？"
- "帮我查一下东京的当前时间"

也可以直接运行脚本：

```bash
python3 scripts/get_time.py              # 默认：Asia/Shanghai
python3 scripts/get_time.py Asia/Tokyo   # 指定时区
```

输出示例：

```json
{
  "date_time": "2026-03-05T20:05:23.547335+08:00",
  "date": "2026-03-05",
  "time": "20:05:23.547335",
  "day_of_week": "Thursday",
  "dst_active": false,
  "timezone": "Asia/Shanghai",
  "utc_offset_seconds": 28800
}
```

## 支持的时区

使用 [IANA 时区标识](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)，常用：

| 城市 | 时区 |
|------|------|
| 北京/上海 | `Asia/Shanghai` |
| 东京 | `Asia/Tokyo` |
| 纽约 | `America/New_York` |
| 伦敦 | `Europe/London` |
| 巴黎 | `Europe/Paris` |
| 悉尼 | `Australia/Sydney` |
| 迪拜 | `Asia/Dubai` |
| 洛杉矶 | `America/Los_Angeles` |

## License

[MIT](LICENSE)
