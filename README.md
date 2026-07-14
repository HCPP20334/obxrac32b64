# obxrac32b64 (cross-lang and crossplatform algorithm obfuscation)
# C++ 
- Windows x64-arm64 (Open obxrac32b64.sinx to Visual Studio 2026) & build_mingw.bat
- Linux x64-aarch64 (build_linux_g++.sh || build_linux_clang++.sh)
- Mac OS (Open folder hash-obxrac32b64_build_macos -> Open README.md )
# js and node.js
* Open Folder js->obxrac32b64.js
* test obxrac32b64.html
# link to My Projects
|  C++
``` C++
#include "obxrac32b64.hpp"
``` 
|  js
``` C++
<script src="obxrac32b64.js"></script>
``` 
# Example C++

``` C++
    #include <algorithm>
    #include <iostream>
    #include <string>
    #include <stdint.h>
    #include <cstring>
	#include "obxrac32b64.hpp"
	int main(){
	std::cout << "obxrac32b64 cryptor\n";
	std::cout << "e - encode\n";
    std::cout << "d - decode\n";
	bool dec = false;
        //	int k = _getch();
	std::cout <<">";
	uint8_t k = 0;
	std::cin >> k;
		dec = (k == 'e' ? false : true);
	std::string s_key = "";
	std::string s_data = "";
	std::cout <<" secret_key:";
	std::cin >> s_key;
	std::cin.ignore();
	std::cout <<" text:";
	std::getline(std::cin,s_data);
	std::cout << obxrac32b64(dec,s_data,s_key) << "\n";
	return 0;
	}
```
# Example Python
``` python
def main():
    print("obxrac32b64 python build\n")
    print("e - encode\nd - decode\n")  
    cmd = input()
    dec = False if cmd == 'e' else True
    print("text:")
    text = input() 
    print("secret key:")
    key = input()
    result = obxrac32b64(dec, text, key)
    print("Result:", result)

if __name__ == "__main__":
    main()
```
# Example HTML+JS

``` html
<html>
<style>
    html {
        background: #14141da4;
    }

    .input {
        background: transparent;
        color: #ccc;
        border: none;
        border-bottom: 1px solid #737383;
        width: 91%;
        height: 44px;
        display: block;
        margin: auto;
        outline: none;

    }

    .obxrac32b64-window {
        width: 100%;
        max-width: 440px;
        overflow: hidden;
        height: auto;
        min-width: 200px; border-radius: 30px;
        background: #1b1b25a3;
    min-height: 350px;
        display: block;
        margin: auto;
        backdrop-filter: blur(10px);

    }

    .generate {
        width: 90%;
        height: 34px;
        background: rgba(241,241,247,255);
        border: none;
        color: #07070a8d;
        font-size: 15px;

        
        display: block;margin: auto;
         border-radius: 20px;
         transform: translateY(10px);
         margin-top: 3;

    }

    .inputs {
        background: #07070a8d;
        display: inline-block;
        transform: translateY(1px);
        margin: auto; height: 90px;
        width: 80%;
        border-top-left-radius: 20px;
        border-bottom-left-radius: 20px;
        
    }

    .buttons {
        display: inline-block;
        transform: translate(-6px, -7px);
        background: #07070a8d;
        width: 120px;
        height: 90px;
        border-top-right-radius: 20px;
        border-bottom-right-radius:20px ;
    }

    @keyframes shin {
        0% {
            transform: translateX(-50%) translateY(-10px);
            opacity: 0;
        }

        100% {
            transform: translateX(-50%) translateY(0px);
            opacity: 1;
        }
    }

    @keyframes shout {
        100% {
            transform: translateX(-50%) translateY(-10px);
            opacity: 0;
        }

        0% {
            transform: translateX(-50%) translateY(0px);
            opacity: 1;
        }
    }

    .message {
        background: #15151eb2;
        width: 300px;
        height: 40px;
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        border-radius: 30px;
        z-index: 5;
        border: 1px solid #737383;
        display: none;
        transition: 2s;
        animation: shin 500ms ease-in;

    }

    * {
        font-family: monospace;
    }

    .message-t {
        color: #fff;
        font-size: 15px;
        position: absolute;
        left: 50%;
        transform: translate(-50%, -5px);
        font-family: monospace;
    }
    .textbuffer{
        width: 90%;
        display: block;
        margin: auto;
        height: 200px;
        background: #07070a8d;
         border-radius: 30px;
    }
    .input-speed{
        width: 87%;
        background: #07070a8d;
        height: 30px;
         border-radius: 30px;
          display: block;
          margin: auto;
          margin-top: 2px;overflow:hidden ;
          position: relative;
    }
    .s_text{
     width: 96%;
     display: block;
     margin: auto;height: 30px;
     appearance: none;overflow:hidden ;
     background: transparent;
     transform: translateY(1px);
     border-radius: 20px ;
    }
    .s_text::-webkit-slider-runnable-track{
        appearance: none;
        background: transparent;
        height: 20px;
        width: 100%;border-radius: 20px ;
        overflow:hidden ;
    }
    .s_text::-webkit-slider-thumb{
        appearance: none;
        background: transparent;
        height: 30px;
        width: 30px;
        background: #fff;
          box-shadow: -407px 0 0 400px #fff; 

            transform: translate(2px,-5px);
    }
    .s_text_d{
        color: #000000;
        font-size: 20px;
        position: absolute;
        left: 50%;
        transform: translate(-50%,-15px);
        z-index: 3;
    }
</style>
<div class="message">
    <p class="message-t">null</p>
</div>
<div class="obxrac32b64-window">
    <Br><center>
    <div class="inputs">
        <input type="text" class="key input" placeholder="введите ключ"">
        <input type=" text" class="text input" placeholder="введите любой текст" style=" border-bottom: none;">
    </div>
    <div class="buttons">
        <button class="generate">decode</button>
        <button class="generate">encode</button>
    </div>
</center>
    <div class="textbuffer">
        <textarea class="text-out input" value="" placeholder="тут тут"
        style="height: 180px;background: transparent;display: block;transform: translateY(7px);border: none;resize: none;">

    </textarea>
    </div>
    <div class="input-speed">
        <p class="s_text_d">0%</p>
        <input type="range" class="s_text">
    </div>
</div>
<script>
    var s_text = document.getElementsByClassName('s_text')[0];
    var s_text_d = document.getElementsByClassName('s_text_d')[0];
    var s_text_data = 0;
    s_text_data = s_text.value;
    s_text.oninput = function(){
        s_text_data = this.value;
        s_text_d.innerText = s_text_data;
    }
    function transform_text(out_text, item, d = 40, isInput = false) {
        if (out_text.length <= 0) {
            isInput ? item.value = "Error: transform_text() out_text null" : item.innerText = "Error: out_text null";
        } else {
            var g = 0; var b = ""; var stop_a = false;
            var a = setInterval(function () {
                b += out_text[g];
                if (g == out_text.length) { g = 0; b = ""; stop_a = true; } else { g++; }
                item.innerText = b + ("1234567890!@#%$%^&()_QWERTYUIOPASDFGHJKLZXCVNMqwertyuiopasdfghjjklzxcvbnm")[Math.floor(Math.random() * 64)];
                if (stop_a) {
                    clearInterval(a);
                    item.innerText = out_text;
                    stop_a = false;
                }
            }, d);

        }

    }
    var message = {
        send: function (text) {
            var mw = document.getElementsByClassName('message')[0];
            var mwt = document.getElementsByClassName('message-t')[0];
            mw.style.display = "block";
            mw.style.animation = "shin 500ms ease-in";
            mwt.innerText = transform_text(text, mwt, 40);
            var b = setTimeout(function () {
                mw.style.animation = "shout 500ms ease-in";
                var v = setTimeout(function () {
                    mw.style.display = "none";
                    clearTimeout(b);
                    clearTimeout(v);
                }, 400);
            }, 400);
        }
    };
    var video_player = {
        _video: "",
        init: function () {
            this._video = document.createElement('video');
            this._video.muted = true;
            this._video.src = "./livevideo.mp4";
            this._video.style.position = "absolute";
            this._video.style.objectFit = "cover";
            this._video.style.top = "50%";
            this._video.style.left = "50%";
            this._video.style.zIndex = "-1";
            this._video.play();
            this._video.loop = true;
            this._video.style.transform = "translate(-50%,-50%)";
            document.documentElement.appendChild(this._video);
        },
        unmuted: function () { this._video.muted = false; }
    };
    video_player.init();
    var inputs = document.getElementsByClassName('inputs');
    var main_window = document.getElementsByClassName('obxrac32b64-window')[0];
    var text_out = document.getElementsByClassName('text-out')[0];
    main_window.onclick = function () {
        video_player.unmuted();
    }
    function size_input_to() {
        inputs[0].style.width = main_window.offsetWidth - (5 + 164) + "px";
    } size_input_to();
    var info = "::obxrac32b64 (js build 0.6) by HCPP\n:: C++20 Builds - \n--------------\nx64 PC Builds\nobxrac32b64.exe          (msvc++ Compiler)\nobxrac32b64_linux_g++    (g++ compiler)\nobxrac32b64_linux_clang++(clang++ compiler) \n--------------\nARM64 and aarch64 Linux\nobxrac32b64_linux_aarc64_clang++ (clang++ aarch64 Compiler)";;
    function preload_text_out() {
        transform_text(info, text_out, 1, true);

    } preload_text_out();
    const obxrac32b64 = {
        gen: function (_key) {
            let hash = "";
            for (let i = 0; i < _key.length; i++) {
                hash = hash + _key[(_key.length - 1) - i];
            }
            return hash;
        },
        xor32: function (code, secret, e_b64 = false) {
            if (!secret) return code;
            let a = code.split('').map((c, i) =>
                String.fromCharCode(c.charCodeAt(0) ^ secret.charCodeAt(i % secret.length))
            ).join('');
            return unescape(a);
        },
        addc(s, i) {
            let d = 0;
            let od = "";
            for (let a = 0; a < i.length; a++) {
                d++;
                od += i[a];
                if (d == s) {
                    od += "$$";
                    d = 0;
                }
            }
            return od;
        },
        addce(s) {
            if (!s) return "";
            return s.toString().split("$$").join("");
        },
        a: "",
        b: "",
        c: "",
        // m0 - key m1 text
        decode: function (text, secret_key) {
            this.a = atob((text));
            this.b = (this.xor32(this.a, secret_key));
            this.b = this.addce(this.b);
            this.b = this.gen(this.b);
            return this.b;
        },
        encode: function (text, secret_key) {
            this.a = this.gen((text));
            this.a = this.addc(5, this.a);
            this.b = this.xor32(this.a, secret_key);
            this.b = btoa((this.b));
            return this.b;
        }
    };
    var decode_button = document.getElementsByClassName('generate')[0];
    var encode_button = document.getElementsByClassName('generate')[1];
    //
    var text = document.getElementsByClassName('text')[0];
    var key = document.getElementsByClassName('key')[0];
    // text buffer 
    var text_str = "";
    var key_str = "";
    text_str = text.value;
    text.oninput = function () {
        text_str = this.value;
    }
    key_str = key.value;
    key.oninput = function () {
        key_str = this.value;
    }
    decode_button.onclick = function () {
        transform_text(obxrac32b64.decode(text_str, key_str), text_out, s_text_data, true);
    }
    encode_button.onclick = function () {
        transform_text(obxrac32b64.encode(text_str, key_str), text_out, s_text_data, true);
    }
    text_out.onclick = function () {
        navigator.clipboard.writeText(text_out.value);
        message.send("Скопированно");
    }
     s_text_data = s_text.value;
     s_text_d.innerText = s_text_data + " ms";
    s_text.oninput = function(){
        s_text_data = this.value;
        s_text_d.innerText = s_text_data + " ms";
         s_text_d.style.color = (s_text_data > 38 ? "#070707" : "#fff");
    }
</script>

</html>
```
