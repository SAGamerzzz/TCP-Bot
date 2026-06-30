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
    b = bots[bid]
    bot_dir = os.path.join(CURRENT_DIR, f"Afridi_VIP_{bid}")
    
    if os.path.exists(bot_dir):
        b["logs"].append(f"🗑️ [SYS] Removing old clone for Server {bid}...")
        shutil.rmtree(bot_dir, ignore_errors=True)
    b["logs"].append(f"🚀 [SYS] Cloning fresh repo for Server {bid}...")
    subprocess.run(["git", "clone", "--depth", "1", GITHUB_REPO, bot_dir], capture_output=True)
    
    while b["status"] == "Running":
        try:
            with open(os.path.join(bot_dir, "AFRIDI.txt"), 'w') as f:
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
# 4. PREMIUM NEON GAMING UI
# ==========================================
HTML_PAGE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AFRIDI VIP PANEL</title>
    <style>
        body, html { 
            margin: 0; padding: 0; min-height: 100%; 
            background: radial-gradient(circle at center, #101528 0%, #070913 100%); 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #e2e8f0; 
        }
        .container { padding: 25px; max-width: 1400px; margin: 0 auto; }
        .header { 
            text-align: center; border: 1px solid rgba(0, 242, 254, 0.3); 
            background: rgba(13, 19, 41, 0.85); padding: 20px; border-radius: 16px;
            margin-bottom: 30px; box-shadow: 0 0 30px rgba(0, 242, 254, 0.15);
            backdrop-filter: blur(8px);
        }
        .header h1 { 
            margin: 0; font-size: 28px; font-weight: 800; letter-spacing: 4px;
            background: linear-gradient(45deg, #00f2fe, #4facfe, #f355da);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        #stats { margin-top: 10px; font-family: monospace; color: #a0aec0; font-size: 13px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 20px; }
        .card { 
            background: rgba(17, 24, 49, 0.9); border: 1px solid rgba(255, 255, 255, 0.08); 
            padding: 20px; border-radius: 14px; position: relative; 
            box-shadow: 0 10px 25px rgba(0,0,0,0.3); transition: all 0.3s ease;
        }
        .card:hover { border-color: rgba(0, 242, 254, 0.4); transform: translateY(-4px); }
        .status-badge { 
            float: right; font-size: 11px; font-weight: bold; font-family: monospace;
            padding: 3px 8px; border-radius: 20px; text-transform: uppercase;
        }
        .status-running { background: rgba(16, 185, 129, 0.15); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.3); }
        .status-stopped { background: rgba(239, 68, 68, 0.15); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.3); }
        
        input { 
            width: 100%; padding: 10px 12px; background: #090d1f; border: 1px solid rgba(255,255,255,0.1); 
            color: #fff; margin: 8px 0; box-sizing: border-box; border-radius: 8px; font-size: 13px;
            transition: all 0.2s;
        }
        input:focus { border-color: #00f2fe; outline: none; box-shadow: 0 0 10px rgba(0, 242, 254, 0.2); }
        
        .btn-action {
            width: 100%; padding: 11px; margin-top: 10px; border-radius: 8px; 
            font-weight: bold; cursor: pointer; border: none; font-size: 13px; letter-spacing: 1px;
            transition: all 0.2s;
        }
        .btn-start { background: linear-gradient(45deg, #00f2fe, #4facfe); color: #000; }
        .btn-start:hover { opacity: 0.9; box-shadow: 0 0 15px rgba(0, 242, 254, 0.4); }
        .btn-stop { background: #24141e; border: 1px solid #ef4444; color: #ef4444; margin-top: 6px; }
        .btn-stop:hover { background: #ef4444; color: #fff; }
        
        .terminal { 
            height: 200px; background: #050711; border: 1px solid rgba(255,255,255,0.05); 
            margin-top: 12px; padding: 10px; font-size: 11px; overflow-y: auto; 
            color: #718096; font-family: monospace; white-space: pre-wrap; border-radius: 8px;
        }
        .fab { 
            position: fixed; bottom: 25px; right: 25px; width: 56px; height: 56px; 
            border-radius: 50%; background: linear-gradient(45deg, #f355da, #7000ff); 
            border: none; color: white; font-size: 28px; cursor: pointer; z-index: 100; 
            box-shadow: 0 0 20px rgba(243, 85, 218, 0.4); transition: transform 0.2s;
        }
        .fab:hover { transform: scale(1.08); }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>AFRIDI VIP SYSTEM</h1>
            <div id="stats">CPU: 0% | RAM: 0% | ACTIVE SERVERS: 0</div>
        </div>
        <div class="grid" id="card-container">
            {% for bid, b in bots.items() %}
                {% if b.active %}
                <div class="card">
                    <span class="status-badge {{ 'status-running' if b.status=='Running' else 'status-stopped' }}" id="badge-{{bid}}">{{ b.status }}</span>
                    <h3 style="margin:0; font-size:16px; color:#4facfe;">SERVER SLOT #{{ bid }}</h3>
                    <input type="text" id="uid-{{bid}}" placeholder="UID" value="{{ b.uid }}">
                    <input type="text" id="pwd-{{bid}}" placeholder="PASS" value="{{ b.pwd }}">
                    <button class="btn-action btn-start" onclick="control('{{bid}}', 'start')">START ENGINE</button>
                    <button class="btn-action btn-stop" onclick="control('{{bid}}', 'stop')">STOP</button>
                    <div class="terminal" id="log-{{bid}}">Console waiting...</div>
                </div>
                {% endif %}
            {% endfor %}
        </div>
    </div>
    <button class="fab" onclick="addServer()">+</button>

    <script>
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
                else alert("MAX 5 SERVERS REACHED! (LIMIT 5)");
            });
        }

        setInterval(() => {
            fetch('/api/stats').then(r => r.json()).then(data => {
                document.getElementById('stats').innerText = `CPU: ${data.cpu} | RAM: ${data.ram} | ACTIVE SERVERS: ${data.active_count}`;
                for(let bid in data.bots) {
                    const l = document.getElementById('log-'+bid);
                    if(l) {
                        l.innerText = data.bots[bid].logs.join('\n');
                        l.scrollTop = l.scrollHeight;
                    }
                    const badge = document.getElementById('badge-'+bid);
                    if(badge) {
                        badge.innerText = data.bots[bid].status;
                        if(data.bots[bid].status === 'Running') {
                            badge.className = 'status-badge status-running';
                        } else {
                            badge.className = 'status-badge status-stopped';
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
