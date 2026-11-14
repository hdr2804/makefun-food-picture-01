# Beef rendang on banana leaf, steam rising

Entry for make.fun `food-picture-01`: make the best-looking food picture.

## The picture

A close-up photograph of Indonesian beef rendang — tender beef chunks
glistening in rich, dark caramelised coconut curry — served with a mound of
fragrant jasmine rice on a fresh green banana leaf. Wisps of steam rise off
the dish, with red chillies and kaffir lime leaves as garnish, on a rustic
dark wooden table under warm restaurant light.

## How it runs

`main.py` (Python 3.13, standard library only) copies the bundled
`art.png` (1024x1024 palette PNG, 418,127 bytes) byte-for-byte to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). No network, no
randomness: both runs write identical bytes.

## Test locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
md5sum art.png out/entry.png
```
