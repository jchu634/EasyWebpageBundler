## Easy Webpage Bundler
### What it does?
This is a program which takes a React/Next.js/HTML project and provides a simple way to bundle it into a local application using PyWebview. 

### Platforms
- Windows
- Linux (Coming soon)

## Quick Start
### Installation
1. Clone the repository
    ```
    git clone https://github.com/jchu634/EasyWebpageBundler
    ```
2. Install the required packages
    ```
    pip install -r requirements.txt
    ```
3. Add your React/Next.js/HTML project to the `static` folder
    
4. Customise the build scripts to include your project name
    -   `package.iss`
        ```
        #define AppName "EasyWebPageBundler"
        #define AppVersion "1.0.0"
        #define AppPublisher "Example"
        #define AppExeName "EasyWebPageBundler"
        ```
    - `build.ps1`
        ```
        $applicationName = "EasyWebPageBundler"
        ```
5. Add environment variables as appropiate to the `.env` file (Optional)
    ```
        ENV = "production"
        ERR404 = True
        APPNAME  = "EasyWebPageBundler"
    ```
    - `ENV` - The environment the application is running in. (production/development)
    - `ERR404` - Whether you have a ```404.html``` page when a page is not found. (True/False)
    - `APPNAME` - The name of the application.
6. Run the build script
    ```
    .\build.ps1
    ```

### Technologies
- The webpages are rendered using PyWebview.
- The pages are served using FastAPI.
- The application is bundled using PyInstaller.
- The windows iinstaller is created using Inno Setup.


