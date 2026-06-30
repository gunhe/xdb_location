import csv
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable, Dict, Optional, Union


UNKNOWN = "未知"
DATA_FILE = Path(__file__).parent / "virtual_phone_data" / "data_virtual_number.csv"
FIELD_NAMES = ("section", "area", "network", "provider", "company")


VirtualNumberRecord = Dict[str, Any]
VirtualNumberData = Dict[str, Dict[str, str]]


def _normalize_section(phone_number: Any) -> str:
    return str(phone_number).strip()[:7]


def _unknown_record(section: str) -> VirtualNumberRecord:
    return {
        "section": section,
        "area": UNKNOWN,
        "network": UNKNOWN,
        "provider": UNKNOWN,
        "company": UNKNOWN,
        "is_virtual_number": False,
    }



@lru_cache(maxsize=None)
def virtual_number_loader(data_path: Optional[Union[str, Path]] = None) -> VirtualNumberData:
    """
    加载虚拟号段数据。

    CSV 字段:
    section,area,network,provider,company

    单条记录示例:
    {
        "section": "1704056",
        "area": "福建 漳州",
        "network": "联通网络",
        "provider": "京东通信",
        "company": "京东商城",
    }
    """
    if data_path is None:
        data_path = DATA_FILE

    with open(data_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return {row["section"]: row for row in reader if row.get("section")}

def virtual_number_searcher(phone_number):
    section = _normalize_section(phone_number)
    data_dict = virtual_number_loader()
    if not data_dict:
        return _unknown_record(section)
    record = data_dict.get(section)
    if record:
        record["is_virtual_number"] = True
    else:
        record = _unknown_record(section)
        record["is_virtual_number"] = False
    record["phone_number"] = phone_number
    return record


if __name__ == "__main__":
    print(virtual_number_searcher(phone_number="17040655743"))
    print(virtual_number_searcher(phone_number="15827327777"))