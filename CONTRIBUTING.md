To build SSC, run:
```sh
uvx pyinstaller --onefile --name ssc --distpath . src/snekscript.py
rm -rf build ssc.spec
```

To build the Visual Studio Code extension, run:
```sh
npx @vscode/vsce package --out snekscript.vsix
```
