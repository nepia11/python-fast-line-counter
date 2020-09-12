# https://tech-blog.optim.co.jp/entry/2019/12/09/080000
# 結構早い

import sys

def wc_block_64k(name, blocksize=65536):
    def blocks(f):
        while True:
            b = f.read(blocksize)
            if b:
                yield b
            else:
                break

    with open(name, 'r') as f:
        return sum(bl.count('\n') for bl in blocks(f))
