$applicationName = "EasyWebPageBundler"

python -m venv venv
.\venv\Scripts\activate
pip install --no-deps -r requirements.txt
pyinstaller .\main.py --add-data "static;static" --noconsole --noconfirm --clean --name $applicationName --contents-directory "."

# Package Backend + Frontend into Installation Executable
iscc .\package.iss