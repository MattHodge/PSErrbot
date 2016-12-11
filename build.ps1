# python -m pip install --upgrade pip
virtualenv -p C:\Python35\python.exe errbot
.\errbot\Scripts\activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
& nuget pack -version $($env:APPVEYOR_BUILD_VERSION)
