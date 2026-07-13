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
        this.a = this.gen(text);
        this.a = this.addc(5, this.a);
        this.b = this.xor32(this.a, secret_key);
        this.b = btoa(this.b);
        return this.b;
    }
};
console.log(obxrac32b64.encode("Hello World!", "12345678"));
console.log(obxrac32b64.decode("Xl5fUX0VFg==","12345"));