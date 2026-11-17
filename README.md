# 5 Python Projects for Beginners That Actually Help at Work

The code from the video. Each script is about 10 to 15 lines and uses only Python's standard library:
nothing to install with pip.

| # | Script | What it does |
| --- | --- | --- |
| 1 | `1_is_it_up.py` | Checks if each server answers on port 443 (UP / DOWN). |
| 2 | `2_port_check.py` | Checks which common ports are open on a machine. |
| 3 | `3_log_report.py` | Counts ERROR lines in `app.log` and shows the top 3 IP addresses. |
| 4 | `4_cert_days.py` | Shows how many days are left before each site's HTTPS certificate expires. |
| 5 | `5_backup.py` | Zips a folder with the date in the name and keeps only the last 7 backups. |

## How to run

1. Install Python 3 (on Windows 11, see "How to Install Python on Windows 11 the Right Way").
2. Download this folder, open a terminal inside it, and run a script:

```
python 1_is_it_up.py
```

`3_log_report.py` reads the sample `app.log` in this folder. Point it at your own log by changing the file name.

## Notes

- **Only scan machines you own or have permission to test** (`2_port_check.py`).
- `5_backup.py` zips `Documents/reports` in your home folder into `Backups`. Change `source` to the folder you want.
  To run it every night, use Task Scheduler on Windows or cron on Linux and macOS.
- Change the lists of servers and sites to your own.

Tested with Python 3.15 on November 17, 2026.
