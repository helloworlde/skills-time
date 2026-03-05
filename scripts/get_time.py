#!/usr/bin/env python3
import sys
import json

import requests


def get_time(timezone: str = "Asia/Shanghai") -> dict:
    url = "https://timeapi.io/api/v1/time/current/zone"
    try:
        resp = requests.get(url, params={"timezone": timezone}, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": type(e).__name__, "message": str(e)}


if __name__ == "__main__":
    tz = sys.argv[1] if len(sys.argv) > 1 else "Asia/Shanghai"
    result = get_time(tz)
    print(json.dumps(result, indent=2, ensure_ascii=False))
