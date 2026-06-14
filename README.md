🙏 **HolyPython.** *Python as God intended.*

| Python              | HolyPython             | Note                             |
|---------------------|------------------------|----------------------------------|
| `a == b`            | `a = b`                |                                  |
| `a = b`             | `a <- b`               |                                  |
| `[a, ..., b]`       | `[a..b]`               | `a`, `b` non-decreasing integers |
| `def f(): ...`      | `function f() { ... }` |                                  |
| `class C: ...`      | `class C { ... }`      |                                  |

## Compilation

### Standard
```sh
python holypython.py foo.hpy
```

### `uv`
```sh
uv run python holypython.py foo.hpy
```

## Testing

### Standard
```sh
pytest
```

### `uv`
```sh
uv run pytest
```
