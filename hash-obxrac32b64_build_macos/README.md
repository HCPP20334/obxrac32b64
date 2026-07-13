# hash-obxrac32b64

## How to build and launch
```powershell
xmake
xmake run
```

## Requirements
* For Windows: [Xmake](https://xmake.io/#/guide/installation?id=windows) and [MinGW-w64](https://winlibs.com) or [MSVC](https://visualstudio.microsoft.com/vs)
* For Linux:
  ```sh
  sudo apt install g++ xmake
  ```
* For macOS:
  ```sh
  brew install llvm xmake
  echo -e '\nexport PATH="/opt/homebrew/opt/llvm/bin:$PATH"\nexport AS=clang\nexport CC=clang\nexport CXX=clang++' >> ~/.bash_profile
  ```
