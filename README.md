🙏 **HolyPython.** *Python as God intended.*

## Programming

| Python              | HolyPython             | Note                                   |
|---------------------|------------------------|----------------------------------------|
| `a == b`            | `a = b`                |                                        |
| `a = b`             | `a <- b`               |                                        |
| `def`               | `function`             |                                        |
| `[-1, ..., 1]`      | `[-1..1]`              |                                        |
| `[f(a), ..., g(b)]` | `[f(a)..g(b)]`         | `f(a)`, `g(b)` non-decreasing integers |
| `def f(): ...`      | `function f() { ... }` |                                        |
| `class C: ...`      | `class C { ... }`      |                                        |

## Transpilation
<table>
	<tr>
		<td>Standard</td>
		<td>uv</td>
	</tr>
	<tr>
		<td>
			```sh
			python holypython.py foo.hpy
			```
		</td>
		<td>
			```sh
			uv run python holypython.py foo.hpy
			```
		</td>
	</tr>
</table>

## Testing
### Standard
```sh
pytest
```

### `uv`
```sh
uv run pytest
```
