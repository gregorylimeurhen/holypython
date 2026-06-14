
<h1 align="center">🙏 HolyPython</h1>
<p align="center">
	<img src="carbon.png" style="width: min(640px, 80vw)">
</p>

| Python         | HolyPython             | Note                             |
|----------------|------------------------|----------------------------------|
| `a == b`       | `a = b`                |                                  |
| `a = b`        | `a <- b`               |                                  |
| `[a, ..., b]`  | `[a..b]`               | `a`, `b` non-decreasing integers |
| `def f(): ...` | `function f() { ... }` |                                  |
| `class C: ...` | `class C { ... }`      |                                  |

### How to transpile HolyPython to Python?

**Standard**

```sh
python holypython.py foo.hpy
```

**`uv`**

```sh
uv run python holypython.py foo.hpy
```

### How to enable syntax highlighting?

**VSCode**

Create extension:
```sh
cd packages/vscode
npx --yes @vscode/vsce package
```

Install extension:
```sh
code --install-extension holypython-0.0.1.vsix
```
