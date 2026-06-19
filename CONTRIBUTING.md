# Compiler Testing

To test the SnekScript compiler using `uv`, run:
```sh
uv run pytest
```

# Compiler Building

To build the SnekScript compiler using `uv`, run:
```sh
# Build ssc
uv run pyinstaller --onefile --name ssc --distpath . src/snekscript.py

# Remove artifacts
rm -rf build ssc.spec
```
