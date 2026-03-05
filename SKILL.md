---
name: get-timezone-time
description: Fetch current time for a specific timezone via TimeAPI. Use when the user asks for current time, world clock, timezone conversion, or needs to know what time it is in a specific city or region.
---

# Get Timezone Time

通过 [TimeAPI](https://timeapi.io/) 获取指定时区的当前时间。

## 使用方式

运行脚本获取时间：

```bash
python3 scripts/get_time.py [TIMEZONE]
```

- `TIMEZONE` 参数可选，默认为 `Asia/Shanghai`
- 时区格式遵循 IANA 标准，如 `America/New_York`、`Europe/London`、`Asia/Tokyo`

> **注意**：`scripts/` 路径相对于本 skill 目录，执行时请使用完整路径，例如：
> `python3 <SKILL_DIR>/scripts/get_time.py [TIMEZONE]`

## API 说明

- 端点：`GET https://timeapi.io/api/v1/time/current/zone?timezone={TIMEZONE}`
- 无需认证
- 返回 JSON，包含以下字段：

| 字段 | 说明 |
|------|------|
| `date_time` | 完整日期时间（含时区偏移） |
| `date` | 日期 (YYYY-MM-DD) |
| `time` | 时间 (HH:MM:SS) |
| `day_of_week` | 星期 |
| `timezone` | 时区名称 |
| `utc_offset_seconds` | UTC 偏移（秒） |
| `dst_active` | 是否处于夏令时 |

## 常用时区

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
