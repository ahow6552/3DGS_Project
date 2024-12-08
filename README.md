10/21 完成基本rendering test 

11/4 AR test

the project based on https://github.com/mkkellogg/GaussianSplats3D

establish local server 

```
python -m http.server 8080
ngrok http 8080 --request-header-add='Cross-Origin-Opener-Policy: same-origin' --request-header-add='Cross-Origin-Embedder-Policy: require-corp' 
--request-header-remove='referrer'
```