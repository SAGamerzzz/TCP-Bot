import time
import os
import sys
import threading
import subprocess
import importlib

# ── কালার কোড ────────────────────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
MAGENTA = "\033[95m"
CYAN    = "\033[96m"
RED     = "\033[91m"
BLUE    = "\033[94m"
WHITE   = "\033[97m"
ORANGE  = "\033[38;5;214m"
DIM     = "\033[2m"

def clear():
    os.system("clear")

# ── মোটা ASCII আর্ট — AFRIDI ─────────────────────────────────
LETTERS = {
    'A': [
        "  █████╗  ",
        " ██╔══██╗ ",
        " ███████║ ",
        " ██╔══██║ ",
        " ██║  ██║ ",
        " ╚═╝  ╚═╝ ",
    ],
    'F': [
        " ███████╗ ",
        " ██╔════╝ ",
        " █████╗   ",
        " ██╔══╝   ",
        " ██║      ",
        " ╚═╝      ",
    ],
    'R': [
        " ██████╗  ",
        " ██╔══██╗ ",
        " ██████╔╝ ",
        " ██╔══██╗ ",
        " ██║  ██║ ",
        " ╚═╝  ╚═╝ ",
    ],
    'I': [
        " ██╗ ",
        " ██║ ",
        " ██║ ",
        " ██║ ",
        " ██║ ",
        " ╚═╝ ",
    ],
    'D': [
        " ██████╗  ",
        " ██╔══██╗ ",
        " ██║  ██║ ",
        " ██║  ██║ ",
        " ██████╔╝ ",
        " ╚═════╝  ",
    ],
    'I2': [
        " ██╗ ",
        " ██║ ",
        " ██║ ",
        " ██║ ",
        " ██║ ",
        " ╚═╝ ",
    ],
}

LETTER_ORDER  = ['A', 'F', 'R', 'I', 'D', 'I2']
LETTER_COLORS = [CYAN, RED, YELLOW, MAGENTA, GREEN, BLUE]
ROWS = 6

def get_lines(visible_count):
    lines = [""] * ROWS
    for i in range(visible_count):
        key   = LETTER_ORDER[i]
        color = LETTER_COLORS[i % len(LETTER_COLORS)]
        for row in range(ROWS):
            lines[row] += color + BOLD + LETTERS[key][row] + RESET
    return lines

def print_afridi_static():
    for line in get_lines(6):
        print(" " + line)

# ── আসল Free Fire লোগো ───────────────────────────────────────
FF_LOGO = [
    "            ⣀⣠⡤                        ",
    "   ⢀⣤⡶⠁⣠⣴⣾⠟⠋⠁                          ",
    "  ⢀⣴⣿⣿⣴⣿⠿⠋⣁⣀⣀⣀⣀⣀⡀                      ",
    "  ⣰⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⡀                ",
    "⣠⣾⣿⡿⠟⠋⠉⠀⣀⣀⣨⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣴⠂",
    "⠈⠉⠁⠀⣀⣴⣾⣿⣿⡿⠟⠛⠉⠉⠉⠉⠛⠻⠿⠿⠿⠿⠿⠿⠟⠋⠁          ",
    "   ⢀⣴⣿⣿⣿⡿⠁⢀⣀⣤⣤⣤⣤⣀⣀                      ",
    "   ⣾⣿⣿⣿⡿⠁⢀⣴⣿⠋⠉⠉⠉⠉⠛⣿⣿⣶⣤⣤⣤⣤⣶⠖            ",
    "  ⢸⣿⣿⣿⣿⡇⢀⣿⣿⣇⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⡿⠃              ",
    "  ⠸⣿⣿⣿⣿⡇⠈⢿⣿⣿⠇⠀⠀⠀⠀⢠⣿⣿⣿⠟⠋                ",
    "   ⢿⣿⣿⣿⣷⡀⠀⠉⠉⠀⠀⠀⢀⣾⣿⣿⡏                    ",
    "    ⠙⢿⣿⣿⣷⣄⡀⠀⠀⣀⣴⣿⣿⣿⣋⣠⡤⠄                  ",
    "       ⠈⠙⠛⠛⠿⠿⠿⠿⠿⠟⠛⠛⠛⠉⠁                   ",
]

FLASH_COLORS = [RED, ORANGE, YELLOW, WHITE, ORANGE, RED, YELLOW,
                ORANGE, WHITE, RED, YELLOW, ORANGE, RED]

def print_ff_logo(color_offset=0, dim_mode=False):
    for row, line in enumerate(FF_LOGO):
        c = FLASH_COLORS[(row + color_offset) % len(FLASH_COLORS)]
        if dim_mode and row % 2 != 0:
            print(RED + DIM + line + RESET)
        else:
            print(c + BOLD + line + RESET)

# ──  ধাপ ১: AFRIDI দ্রুত ভেসে উঠবে ──────────────────────────
for i in range(1, 7):
    for flash in range(3):
        clear()
        print("\n")
        lines = get_lines(i) if flash % 2 == 0 else get_lines(i - 1)
        for line in lines:
            print(" " + line)
        print()
        time.sleep(0.06)
    clear()
    print("\n")
    for line in get_lines(i):
        print(" " + line)
    print()
    time.sleep(0.12)

time.sleep(0.4)

# ──  ধাপ ২: Free Fire লোগো লাইٹنگ ────────────────────────────
for flash_round in range(10):
    clear()
    print("\n")
    print_afridi_static()
    print()
    if flash_round % 3 == 0:
        for row, line in enumerate(FF_LOGO):
            c = [WHITE, YELLOW, ORANGE, RED][flash_round % 4]
            print(c + BOLD + line + RESET)
    elif flash_round % 3 == 1:
        print_ff_logo(color_offset=flash_round)
    else:
        print_ff_logo(dim_mode=True)
    print()
    time.sleep(0.16)

clear()
print("\n")
print_afridi_static()
print()
print_ff_logo(color_offset=2)
print()
time.sleep(0.8)

# ──  ধাপ ৩: মডিউল ইনস্টলার ───────────────────────────────────
MODULES = [
    ("requests",            "requests",            "pip"),
    ("psutil",              "psutil",              "pkg"),   
    ("PyJWT",               "jwt",                 "pip"),
    ("urllib3",             "urllib3",             "pip"),
    ("aiohttp",             "aiohttp",             "pip"),
    ("flask",               "flask",               "pip"),
    ("pycryptodome",        "Crypto",              "pip"),
    ("protobuf",            "google.protobuf",     "pip"),
    ("google-play-scraper", "google_play_scraper", "pip"),
    ("pytz",                "pytz",                "pip"),
    ("python-cfonts",       "cfonts",              "pip"),  # 👈 এই লাইনটি নতুন যুক্ত করা হয়েছে
]


PKG_NAMES = {
    "psutil": "python-psutil",
}

clear()
print()
print(CYAN + BOLD + "  ╔══════════════════════════════════════════════╗" + RESET)
print(CYAN + BOLD + "  ║       📦  মডিউল চেক করা হচ্ছে...           ║" + RESET)
print(CYAN + BOLD + "  ╚══════════════════════════════════════════════╝" + RESET)
print()
time.sleep(0.4)

BAR_LEN = 25

def run_progress_bar(stop_flag, label):
    spin    = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    bcolors = [RED, ORANGE, YELLOW, GREEN, CYAN, MAGENTA]
    filled  = 0
    idx     = 0
    while not stop_flag.is_set():
        bc  = bcolors[filled % len(bcolors)]
        bar = bc + BOLD + "█" * filled + DIM + "░" * (BAR_LEN - filled) + RESET
        sp  = spin[idx % len(spin)]
        sys.stdout.write(f"\r  {YELLOW}↓{RESET}  {WHITE}{BOLD}{label:<24}{RESET}  [{bar}]  {CYAN}{sp}{RESET}  ")
        sys.stdout.flush()
        filled = min(filled + 1, BAR_LEN)
        idx   += 1
        time.sleep(0.07)

for pip_name, import_name, method in MODULES:
    try:
        importlib.import_module(import_name.split(".")[0])
        already = True
    except ImportError:
        already = False

    if already:
        bar = GREEN + BOLD + "█" * BAR_LEN + RESET
        print(f"  {GREEN}✔{RESET}  {WHITE}{BOLD}{pip_name:<24}{RESET}  [{bar}]  {GREEN}{BOLD}ALREADY INSTALLED ✓{RESET}")
        time.sleep(0.15)
        continue

    stop_flag = threading.Event()
    t = threading.Thread(target=run_progress_bar, args=(stop_flag, pip_name))
    t.start()

    if method == "pkg":
        pkg_pkg_name = PKG_NAMES.get(pip_name, pip_name)
        result = subprocess.run(
            ["pkg", "install", pkg_pkg_name, "-y"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    else:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", pip_name, "-q"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    stop_flag.set()
    t.join()

    try:
        importlib.import_module(import_name.split(".")[0])
        success = True
    except ImportError:
        success = False

    if success:
        tag = "PKG INSTALLED ✓" if method == "pkg" else "INSTALLED ✓"
        bar = GREEN + BOLD + "█" * BAR_LEN + RESET
        sys.stdout.write(f"\r  {GREEN}✔{RESET}  {WHITE}{BOLD}{pip_name:<24}{RESET}  [{bar}]  {GREEN}{BOLD}{tag}{RESET}          \n")
    else:
        bar = RED + BOLD + "█" * BAR_LEN + RESET
        sys.stdout.write(f"\r  {RED}✘{RESET}  {WHITE}{BOLD}{pip_name:<24}{RESET}  [{bar}]  {RED}{BOLD}FAILED ✘{RESET}             \n")
    sys.stdout.flush()
    time.sleep(0.1)

print()
print(GREEN + BOLD + "  ✅  সব মডিউল প্রস্তুত! মূল প্রোগ্রাম শুরু হচ্ছে..." + RESET)
print()
time.sleep(1)
clear()

# ════════════════════════════════════════════════════════════
# ✅ মূল সিস্টেম কোড (৫টি বোট সাপোর্ট এবং নিউ গেমিং থিম সহ)
# ════════════════════════════════════════════════════════════
import json, socket, shutil, re, logging, random
from flask import Flask, render_template_string, jsonify, request
import psutil
from cfonts import render

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(CURRENT_DIR, "afridi_vip_pro.json")
GITHUB_REPO = "https://github.com/Ariyan20267/Ariyan_bot.git"

# ৫টি বোট কনফিগারেশন সাপোর্ট
bots = {
    "1": {"active": True, "uid": "", "pwd": "", "status": "Stopped", "process": None, "logs": [], "start_time": 0},
    "2": {"active": False, "uid": "", "pwd": "", "status": "Stopped", "process": None, "logs": [], "start_time": 0},
    "3": {"active": False, "uid": "", "pwd": "", "status": "Stopped", "process": None, "logs": [], "start_time": 0},
    "4": {"active": False, "uid": "", "pwd": "", "status": "Stopped", "process": None, "logs": [], "start_time": 0},
    "5": {"active": False, "uid": "", "pwd": "", "status": "Stopped", "process": None, "logs": [], "start_time": 0}
}

app = Flask(__name__)
logging.getLogger('werkzeug').setLevel(logging.ERROR)

def save_config():
    data = {k: {"uid": v["uid"], "pwd": v["pwd"], "active": v["active"]} for k, v in bots.items()}
    with open(CONFIG_FILE, 'w') as f: json.dump(data, f, indent=4)

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                saved = json.load(f)
                for k in saved:
                    if k in bots: bots[k].update(saved[k])
        except: pass

def run_bot_engine(bid):
def run_bot_engine(bid):
    b = bots[bid]
    bot_dir = os.path.join(CURRENT_DIR, f"Afridi_VIP_{bid}")
    
    if os.path.exists(bot_dir):
        b["logs"].append(f"🗑️ [SYS] Removing old clone for Server {bid}...")
        shutil.rmtree(bot_dir, ignore_errors=True)
    b["logs"].append(f"🚀 [SYS] Cloning fresh repo for Server {bid}...")
    subprocess.run(["git", "clone", "--depth", "1", GITHUB_REPO, bot_dir], capture_output=True)
    
    while b["status"] == "Running":
        try:
            # 💡 এখানে আগে AFRIDI.txt ছিল, সেটিকে পরিবর্তন করে ARIYAN.txt করা হলো
            with open(os.path.join(bot_dir, "ARIYAN.txt"), 'w') as f:
                json.dump({b["uid"]: b["pwd"]}, f, indent=4)

            b["process"] = subprocess.Popen(
                [sys.executable, "-u", "main.py"],
                cwd=bot_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1
            )
            b["start_time"] = time.time()

            for line in iter(b["process"].stdout.readline, ''):
                if b["status"] != "Running": break
                if line.strip():
                    b["logs"].append(line.strip())
                    if len(b["logs"]) > 100: b["logs"].pop(0)
            
            b["process"].wait()
            if b["status"] == "Running":
                b["logs"].append("🔄 [SYS] Restarting in 5s...")
                time.sleep(5)
        except Exception as e:
            b["logs"].append(f"⚠️ [ERROR] {str(e)}")
            time.sleep(10)

def restart_scheduler():
    while True:
        time.sleep(60)
        for bid, b in bots.items():
            if b["status"] == "Running" and b["start_time"] > 0:
                if (time.time() - b["start_time"]) > 7200:
                    b["logs"].append("⚡ [SYSTEM] 2 Hours Limit! Auto-refreshing...")
                    if b["process"]: b["process"].kill()

threading.Thread(target=restart_scheduler, daemon=True).start()

# ==========================================
# 4. WORKING ORIGINAL CYBERPUNK PANEL UI
# ==========================================
HTML_PAGE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AFRIDI VOID://TERMINAL</title>
<style>
  :root{
    --bg:#06080a;
    --panel:#0b0f12;
    --line:#1c2b27;
    --accent:#39ff8f;
    --accent-dim:#1f7a4d;
    --danger:#ff3b5c;
    --text:#cdeede;
    --muted:#5d8d77;
    --mono: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
  }
  *{box-sizing:border-box;}
  body,html{margin:0;padding:0;height:100%;background:var(--bg);font-family:var(--mono);color:var(--text);overflow-x:hidden;}
  canvas#rain{position:fixed;top:0;left:0;z-index:0;opacity:.35;}
  .scan{position:fixed;inset:0;z-index:1;pointer-events:none;
    background:repeating-linear-gradient(to bottom, rgba(57,255,143,0.025) 0px, rgba(57,255,143,0.025) 1px, transparent 1px, transparent 3px);
    mix-blend-mode:overlay;}
  .wrap{position:relative;z-index:2;max-width:1180px;margin:0 auto;padding:28px 20px 80px;}

  .topbar{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid var(--line);padding-bottom:14px;margin-bottom:26px;}
  .topbar .brand{font-size:13px;letter-spacing:.32em;color:var(--accent);text-transform:uppercase;}
  .topbar .brand span{color:var(--muted);}
  .topbar .meta{font-size:11px;color:var(--muted);letter-spacing:.1em;text-align:right;}
  .topbar .meta b{color:var(--accent);}

  .stats{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);border:1px solid var(--line);margin-bottom:28px;}
  .stat{background:var(--panel);padding:16px 18px;}
  .stat .label{font-size:10px;letter-spacing:.18em;color:var(--muted);text-transform:uppercase;margin-bottom:8px;}
  .stat .value{font-size:22px;color:var(--accent);font-weight:600;}
  .stat .value.warn{color:var(--danger);}

  .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px;}
  .card{background:var(--panel);border:1px solid var(--line);position:relative;animation:rise .45s ease-out both;}
  @keyframes rise{from{opacity:0;transform:translateY(14px);}to{opacity:1;transform:translateY(0);}}
  .card-head{display:flex;justify-content:space-between;align-items:center;padding:12px 16px;border-bottom:1px solid var(--line);}
  .card-head .id{font-size:12px;letter-spacing:.1em;color:var(--text);}
  .card-head .id b{color:var(--accent);}
  .pill{font-size:10px;letter-spacing:.08em;padding:2px 8px;border:1px solid currentColor;text-transform:uppercase;}
  .pill.on{color:var(--accent); background: rgba(57,255,143,0.05);}
  .pill.off{color:var(--danger); background: rgba(255,59,92,0.05);}
  .card-body{padding:16px;}

  label{display:block;font-size:10px;letter-spacing:.14em;color:var(--muted);text-transform:uppercase;margin-bottom:5px;margin-top:12px;}
  label:first-child{margin-top:0;}
  input[type=text]{
    width:100%;padding:9px 10px;background:#020403;border:1px solid var(--line);color:var(--text);
    font-family:var(--mono);font-size:13px;outline:none;transition:border-color .15s;
  }
  input[type=text]:focus{border-color:var(--accent);}

  .btn-row{display:flex;gap:8px;margin-top:14px;}
  button{
    font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;
    padding:9px 12px;cursor:pointer;border:1px solid var(--accent-dim);background:transparent;color:var(--accent);
    transition:all .15s; flex:1;
  }
  button:hover{background:var(--accent);color:#031b10;box-shadow:0 0 14px rgba(57,255,143,.35);}
  button.stop{border-color:#5a2030;color:var(--danger);}
  button.stop:hover{background:var(--danger);color:#1a0509;box-shadow:0 0 14px rgba(255,59,92,.35);}

  .console-wrapper {
    position: relative;
    margin-top: 14px;
  }
  .console{
    height:210px;background:#020403;border:1px solid var(--line);
    padding:10px;font-size:11px;line-height:1.6;color:var(--accent);overflow-y:auto;white-space:pre-wrap;
  }
  .console::-webkit-scrollbar{width:6px;}
  .console::-webkit-scrollbar-thumb{background:var(--accent-dim);}

  .copy-btn{
    position:absolute;top:8px;right:8px;font-size:9px;letter-spacing:.1em;padding:4px 8px;
    border:1px solid var(--line);background:rgba(0,0,0,.7);color:var(--muted);text-transform:uppercase;
    cursor:pointer;z-index:10;transition:all 0.15s;
  }
  .copy-btn:hover{color:var(--accent);border-color:var(--accent-dim);background:rgba(0,0,0,.9);}
  .copy-btn.copied{color:#031b10;background:var(--accent);border-color:var(--accent);}

  .fab{
    position:fixed;bottom:24px;right:24px;width:52px;height:52px;border-radius:50%;
    background:var(--panel);border:1px solid var(--accent-dim);color:var(--accent);font-size:26px;
    display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:50;
    box-shadow:0 0 18px rgba(57,255,143,.25);
  }
  .fab:hover{background:var(--accent);color:#031b10;}

  .banner{
    text-align:center;font-size:10px;letter-spacing:.2em;color:var(--muted);text-transform:uppercase;
    border-top:1px solid var(--line);margin-top:40px;padding-top:16px;
  }
  .banner b{color:var(--accent-dim);}

  @media (max-width:640px){
    .stats{grid-template-columns:repeat(2,1fr);}
    .topbar{flex-direction:column;gap:6px;align-items:flex-start;}
    .topbar .meta{text-align:left;}
  }
</style>
</head>
<body>
<canvas id="rain"></canvas>
<div class="scan"></div>

<div class="wrap">
  <div class="topbar">
    <div class="brand">AFRIDI<span>://</span>VOID-PANEL</div>
    <div class="meta">PRODUCTION NODE ENGINE <b>ONLINE</b><br>PORT: <b>5000</b></div>
  </div>

  <div class="stats">
    <div class="stat"><div class="label">Core Load</div><div class="value" id="s-cpu">0%</div></div>
    <div class="stat"><div class="label">Memory</div><div class="value" id="s-ram">0%</div></div>
    <div class="stat"><div class="label">Nodes Active</div><div class="value" id="s-active">0</div></div>
    <div class="stat"><div class="label">Max Slots</div><div class="value" style="color:#00f2fe;">5</div></div>
  </div>

  <div class="grid" id="card-container">
    {% for bid, b in bots.items() %}
        {% if b.active %}
        <div class="card" id="card-{{bid}}">
          <div class="card-head">
            <div class="id">SERVER SLOT <b>#{{bid}}</b></div>
            <div class="pill {{ 'on' if b.status=='Running' else 'off' }}" id="pill-{{bid}}">
                {{ 'ONLINE' if b.status=='Running' else 'OFFLINE' }}
            </div>
          </div>
          <div class="card-body">
            <label>User ID (UID)</label>
            <input type="text" id="uid-{{bid}}" placeholder="Enter Game UID" value="{{ b.uid }}">
            <label>Access Password</label>
            <input type="text" id="pwd-{{bid}}" placeholder="Enter Token/Password" value="{{ b.pwd }}">
            <div class="btn-row">
              <button onclick="control('{{bid}}', 'start')">Start Engine</button>
              <button class="stop" onclick="control('{{bid}}', 'stop')">Stop</button>
            </div>
            <div class="console-wrapper">
              <button class="copy-btn" id="copybtn-{{bid}}" onclick="copyLog('{{bid}}')">Copy</button>
              <div class="console" id="log-{{bid}}">Connecting to terminal streams...</div>
            </div>
          </div>
        </div>
        {% endif %}
    {% endfor %}
  </div>
</div>

<button class="fab" id="addBtn" onclick="addServer()" title="Spin up node">+</button>

<div class="banner">POWERED BY AFRIDI CORE ENGINE V5 · <b>WORKING ORIGINAL SYSTEM</b></div>

<script>
/* ---------- Matrix rain background ---------- */
const canvas = document.getElementById('rain');
const ctx = canvas.getContext('2d');
function resize(){ canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
resize(); window.addEventListener('resize', resize);
const glyphs = "0101010101010101";
const fontSize = 14;
let columns = Math.floor(canvas.width / fontSize);
let drops = Array(columns).fill(1);
function drawRain(){
  if (columns !== Math.floor(canvas.width / fontSize)) { columns = Math.floor(canvas.width / fontSize); drops = Array(columns).fill(1); }
  ctx.fillStyle = "rgba(6,8,10,0.08)";
  ctx.fillRect(0,0,canvas.width,canvas.height);
  ctx.fillStyle = "#39ff8f";
  ctx.font = fontSize + "px monospace";
  for (let i=0;i<drops.length;i++){
    const text = glyphs.charAt(Math.floor(Math.random()*glyphs.length));
    ctx.fillText(text, i*fontSize, drops[i]*fontSize);
    if (drops[i]*fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
    drops[i]++;
  }
}
setInterval(drawRain, 60);

/* ---------- Core Server Controller Function Flow ---------- */
function control(bid, action) {
    const uid = document.getElementById('uid-'+bid).value;
    const pwd = document.getElementById('pwd-'+bid).value;
    fetch('/api/control', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({bid, action, uid, pwd})
    });
}

function addServer() {
    fetch('/api/add_server').then(r => r.json()).then(data => {
        if(data.success) location.reload();
        else {
            const btn = document.getElementById('addBtn');
            btn.style.borderColor = 'var(--danger)'; btn.style.color = 'var(--danger)';
            setTimeout(()=>{ btn.style.borderColor=''; btn.style.color=''; }, 600);
            alert("MAX 5 SERVERS REACHED! (SLOT LIMIT IS 5)");
        }
    });
}

/* ---------- 1-Click Clipboard Logger Copy Engine ---------- */
function copyLog(bid) {
    const logBox = document.getElementById('log-'+bid);
    if (!logBox) return;
    
    // কনসোলের ভেতরের পুরো টেক্সট এক্সট্রাক্ট করা হচ্ছে
    const textToCopy = logBox.innerText;
    
    navigator.clipboard.writeText(textToCopy).then(() => {
        const btn = document.getElementById('copybtn-'+bid);
        btn.textContent = 'Copied!'; 
        btn.classList.add('copied');
        setTimeout(() => { 
            btn.textContent = 'Copy'; 
            btn.classList.remove('copied'); 
        }, 1500);
    }).catch(err => {
        alert("কপি করা যায়নি, ব্রাউজার পারমিশন চেক করুন।");
    });
}

/* ---------- Live I/O Polling Data Stream ---------- */
setInterval(() => {
    fetch('/api/stats').then(r => r.json()).then(data => {
        document.getElementById('s-cpu').innerText = data.cpu;
        document.getElementById('s-ram').innerText = data.ram;
        document.getElementById('s-active').innerText = data.active_count;
        
        for(let bid in data.bots) {
            const l = document.getElementById('log-'+bid);
            if(l) {
                l.innerText = data.bots[bid].logs.join('\n');
                // অটো স্ক্রোল যদি ইউজার নিচে থাকে
                l.scrollTop = l.scrollHeight;
            }
            const pill = document.getElementById('pill-'+bid);
            if(pill) {
                if(data.bots[bid].status === 'Running') {
                    pill.innerText = 'ONLINE';
                    pill.className = 'pill on';
                } else {
                    pill.innerText = 'OFFLINE';
                    pill.className = 'pill off';
                }
            }
        }
    });
}, 2000);
</script>
</body>
</html>
"""


# ==========================================
# 5. FLASK API ROUTES (UPDATED FOR 5 LIMIT)
# ==========================================
@app.route('/')
def index():
    load_config()
    active_count = sum(1 for b in bots.values() if b["active"])
    return render_template_string(HTML_PAGE, bots=bots, active_count=active_count)

@app.route('/api/add_server')
def add_server():
    active_count = sum(1 for b in bots.values() if b["active"])
    if active_count < 5: 
        for bid in ["1", "2", "3", "4", "5"]:
            if not bots[bid]["active"]:
                bots[bid]["active"] = True
                save_config()
                return jsonify({"success": True})
    return jsonify({"success": False})

@app.route('/api/control', methods=['POST'])
def control():
    data = request.json
    bid, action = data.get('bid'), data.get('action')
    if bid in bots:
        bots[bid]["uid"], bots[bid]["pwd"] = data.get("uid", ""), data.get("pwd", "")
        save_config()
        if action == 'start' and bots[bid]["status"] != "Running":
            bots[bid]["status"] = "Running"
            threading.Thread(target=run_bot_engine, args=(bid,), daemon=True).start()
        elif action == 'stop':
            bots[bid]["status"] = "Stopped"
            if bots[bid]["process"]: 
                bots[bid]["process"].terminate() 
    return jsonify({"status": "ok"})

@app.route('/api/stats')
def stats():
    try: cpu = f"{psutil.cpu_percent()}%"
    except: cpu = "N/A"
    active_count = sum(1 for b in bots.values() if b["active"])
    return jsonify({
        "cpu": cpu, "ram": f"{psutil.virtual_memory().percent}%",
        "active_count": active_count,
        "bots": {bid: {"status": b["status"], "logs": b["logs"][-100:]} for bid, b in bots.items() if b["active"]}
    })

if __name__ == '__main__':
    load_config()
    os.system('clear' if os.name == 'posix' else 'cls')
    print(render('AFRIDI', colors=['cyan', 'yellow'], align='center'))
    PORT = 5000
    print(f"\033[1;32m[+] PREMIUM NEON PANEL LIVE: http://localhost:{PORT}\033[0m")
    app.run(host='0.0.0.0', port=PORT, debug=False, use_reloader=False)
