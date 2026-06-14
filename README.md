
<h3 align="center">
	𓆩 𓂋 𓆪
	<br>
	HolyPython
</h3>

| `.hpy`                                    | → | `.py`                             |
|-------------------------------------------|---|-----------------------------------|
| ![HolyPython](screenshots/holypython.png) | → | ![Python](screenshots/python.png) |

## Syntax

### Summary

| Python         | HolyPython             | Notes                                  |
|----------------|------------------------|----------------------------------------|
| `a == b`       | `a = b`                |                                        |
| `a = b`        | `a <- b`               |                                        |
| `[a, ..., b]`  | `[a..b]`               | `type(a) == type(b) == int and a <= b` |
| `def f(): ...` | `function f() { ... }` |                                        |
| `class C: ...` | `class C { ... }`      |                                        |

### Highlighting

**VSCode and VSCodium**

```sh
# Create extension
cd holypython/packages/vscode
npx @vscode/vsce package --out holypython.vsix

# Install extension
code --install-extension holypython.vsix # for VSCode
codium --install-extension holypython.vsix # for VSCodium
```

## Transpilation

### HolyPython-to-Python

```sh
cd holypython
python holypython.py foo.hpy
```
