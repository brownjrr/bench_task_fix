import json
from pathlib import Path


def test_report_exists():
    """1. Test report exists"""
    assert Path("/app/report.json").exists(), "no report.json found"

def test_report_total_requests():
    """2. 6 Total Requests found"""
    with open("/app/report.json") as f:
        report = json.load(f)
    assert report["total_requests"] == 6, "total_requests is not 6"

def test_report_unique_ips():
    """3. 3 Unique IP Adressess found"""
    with open("/app/report.json") as f:
        report = json.load(f)
    assert report["unique_ips"] == 3, "unique_ips is not 3"

def test_report_top_path():
    """4. /index.html is the most visited page"""
    with open("/app/report.json") as f:
        report = json.load(f)
    assert report["top_path"] == "/index.html", f"{report['top_path']} is not /index.html"

def test_report_nonempty():
    """5. Report is not empty"""
    assert Path("/app/report.json").stat().st_size > 0, "report.json is empty"
