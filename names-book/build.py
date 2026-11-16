import sys, os, subprocess, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
import original

def build(parts, out_html, out_pdf):
    body = "\n".join(parts)
    open(out_html, "w", encoding="utf-8").write(page(body))
    subprocess.run(["node", os.path.join(os.path.dirname(os.path.abspath(__file__)), "render_pdf.cjs"), out_html, out_pdf], check=True)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/test"
    build([original.name1(), original.name2(), original.together12(), original.name3()], out + ".html", out + ".pdf")
