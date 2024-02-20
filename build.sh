applicationName="EasyWebPageBundler"

python3 -m venv venv
source venv/bin/activate
pip install -r linux_requirements.txt
pyinstaller main.py --add-data="static:static" --noconfirm --clean --name "$applicationName" --windowed --contents-directory "."

# Package Executable into Zip
cd "dist" && zip -r -Z bzip2 "$applicationName.zip" "$applicationName"

deactivate