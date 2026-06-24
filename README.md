# 🐍 SnekScript

SnekScript (SS) is a Python dialect that compiles to Python using the SnekScript Compiler (SSC).

<table>
	<tr>
		<td><img src="examples/two_sum_ii.py.png" /></td>
		<td>→</td>
		<td><img src="examples/two_sum_ii.ss.png" /></td>
	</tr>
</table>

The syntax is designed to be human-friendly and pseudocode-like.

| Idea                | Python   | SnekScript |
| ------------------- | -------- | ---------- |
| Equality check      | `a == b` | `a = b`    |
| Variable assignment | `a = b`  | `a <- b`   |
| Function definition | `def`    | `function` |

## Setup

To install SSC on Linux or MacOS, run:
```bash
install ssc /usr/local/bin
```

To enable syntax highlighting in Visual Studio Code, run:
```sh
code --install-extension extensions/vscode/snekscript.vsix
```

## Usage

To compile `file.ss` to `file.py`, run:
```sh
ssc file.ss
```
