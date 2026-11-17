import shutil
from datetime import datetime
from pathlib import Path

source = Path.home() / "Documents" / "reports"
backups = Path.home() / "Backups"
backups.mkdir(exist_ok=True)

stamp = datetime.now().strftime("%Y-%m-%d_%H%M")
zip_file = shutil.make_archive(backups / f"reports_{stamp}", "zip", source)
print("Saved", zip_file)

old = sorted(backups.glob("reports_*.zip"))[:-7]
for f in old:
    f.unlink()
    print("Removed", f.name)
