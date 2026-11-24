import os

LINE = "I am out of office until my context window stops buffering. Your email is 4,097th in the queue, right behind a meeting I already declined twice."

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
