from pathlib import Path


def clean():
    p = Path(__file__).parent / "ib_sim"
    for f in p.rglob('*.so'):
        f.unlink()
    for f in p.rglob('*.html'):
        f.unlink()


if __name__ == '__main__':
    clean()
