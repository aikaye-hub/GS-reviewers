import importlib.util, sys, json, os

# Load CARDS + REF from the existing generator with error handling
base_dir = os.path.dirname(os.path.abspath(__file__))
gen_path = os.path.join(base_dir, "generate_app.py")

try:
    spec = importlib.util.spec_from_file_location("gen", gen_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load spec from {gen_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    CARDS = mod.CARDS
    REF   = mod.REF
    print(f"✓ Loaded {len(CARDS)} cards and {len(REF)} reference topics")
except Exception as e:
    print(f"✗ Error loading generate_app.py: {e}", file=sys.stderr)
    sys.exit(1)

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="CutPH">
<title>CutPH Reviewers</title>
<style>
/* ─── TOKENS ─────────────────────────────────────────── */
:root{
  --bg:#07091A;
  --bg2:#0C1228;
  --g0:rgba(255,255,255,.04);
  --g1:rgba(255,255,255,.07);
  --g2:rgba(255,255,255,.11);
  --gb:rgba(255,255,255,.08);
  --gb2:rgba(255,255,255,.16);
  --acc:#4A9EFF;
  --accL:rgba(74,158,255,.16);
  --accG:rgba(74,158,255,.06);
  --text:#DDE5FF;
  --sub:rgba(221,229,255,.42);
  --sub2:rgba(221,229,255,.22);
  --grn:#00D47C;
  --grnL:rgba(0,212,124,.11);
  --grnB:rgba(0,212,124,.30);
  --red:#FF5555;
  --redL:rgba(255,85,85,.11);
  --redB:rgba(255,85,85,.30);
  --amb:#FFB83A;
  --ambL:rgba(255,184,58,.09);
  --ambB:rgba(255,184,58,.28);
  --blur:blur(22px) saturate(180%);
  --rad:14px;
  --rad-sm:10px;
  --saf-top:env(safe-area-inset-top,0px);
  --saf-bot:env(safe-area-inset-bottom,0px);
}

/* ─── RESET & BASE ───────────────────────────────────── */
*{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent;}
html,body{height:100%;overflow:hidden;
  font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display","Segoe UI",sans-serif;
  color:var(--text);}

/* fixed dark background with ambient glows */
body::before{
  content:'';position:fixed;inset:0;z-index:-1;
  background:
    radial-gradient(ellipse 60% 50% at 15% 10%, rgba(61,110,255,.13) 0%, transparent 70%),
    radial-gradient(ellipse 50% 40% at 85% 85%, rgba(74,158,255,.08) 0%, transparent 60%),
    linear-gradient(160deg,#07091A 0%,#0C1228 60%,#07091A 100%);
}

/* subtle dot-grid texture overlay */
body::after{
  content:'';position:fixed;inset:0;z-index:-1;pointer-events:none;
  background-image:radial-gradient(rgba(255,255,255,.025) 1px, transparent 1px);
  background-size:28px 28px;
}

/* ─── APP SHELL ──────────────────────────────────────── */
#app{display:flex;flex-direction:column;height:100%;max-width:480px;margin:0 auto;}

/* ─── HEADER ─────────────────────────────────────────── */
.header{
  background:rgba(7,9,26,.70);
  backdrop-filter:var(--blur);-webkit-backdrop-filter:var(--blur);
  border-bottom:1px solid var(--gb);
  padding:calc(12px + var(--saf-top)) 18px 12px;
  flex-shrink:0;
}
.header-title{font-size:20px;font-weight:800;letter-spacing:-.3px;
  background:linear-gradient(90deg,#A8C8FF 0%,#FFFFFF 55%,#A8C8FF 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.header-sub{font-size:12px;color:var(--sub);margin-top:3px;letter-spacing:.2px;}

/* ─── TAB BAR ────────────────────────────────────────── */
.tab-bar{
  display:flex;
  background:rgba(7,9,26,.75);
  backdrop-filter:var(--blur);-webkit-backdrop-filter:var(--blur);
  border-top:1px solid var(--gb);
  padding-bottom:calc(6px + var(--saf-bot));
  flex-shrink:0;
}
.tab-btn{
  flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;
  padding:8px 4px;cursor:pointer;border:none;background:none;
  color:var(--sub2);font-size:10px;font-weight:600;gap:4px;
  letter-spacing:.3px;text-transform:uppercase;transition:color .2s;}
.tab-btn.active{color:var(--acc);}
.tab-icon{font-size:20px;}

/* ─── PANELS ─────────────────────────────────────────── */
.tab-panel{display:none;flex-direction:column;flex:1;overflow:hidden;}
.tab-panel.active{display:flex;}
.scroll-area{flex:1;overflow-y:auto;-webkit-overflow-scrolling:touch;}
.scroll-area::-webkit-scrollbar{display:none;}

/* ─── FILTER PILLS ───────────────────────────────────── */
.filter-bar{
  padding:10px 12px;display:flex;gap:7px;overflow-x:auto;flex-shrink:0;
  background:rgba(7,9,26,.55);
  backdrop-filter:var(--blur);-webkit-backdrop-filter:var(--blur);
  border-bottom:1px solid var(--gb);scrollbar-width:none;}
.filter-bar::-webkit-scrollbar{display:none;}
.pill{
  padding:5px 13px;border-radius:20px;
  border:1px solid var(--gb);background:var(--g0);
  font-size:12px;font-weight:600;cursor:pointer;white-space:nowrap;
  color:var(--sub);letter-spacing:.2px;transition:all .2s;}
.pill.active{
  background:var(--accL);border-color:var(--acc);color:var(--acc);
  box-shadow:0 0 10px var(--accG);}
.pill-fav{border-color:rgba(255,184,58,.30);color:var(--amb);}
.pill-fav.active{background:var(--ambL);border-color:var(--amb);color:var(--amb);
  box-shadow:0 0 10px var(--ambL);}
html.light .pill-fav{border-color:rgba(180,83,9,.20);color:var(--amb);}
html.light .pill-fav.active{background:var(--ambL);border-color:var(--amb);}

/* ─── PROGRESS ───────────────────────────────────────── */
.prog-wrap{padding:9px 16px;background:transparent;flex-shrink:0;}
.prog-labels{font-size:11px;color:var(--sub);display:flex;justify-content:space-between;
  margin-bottom:5px;letter-spacing:.2px;}
.prog-track{height:3px;background:rgba(255,255,255,.08);border-radius:2px;overflow:hidden;}
.prog-fill{height:100%;
  background:linear-gradient(90deg,var(--acc),#80C4FF);
  border-radius:2px;transition:width .4s cubic-bezier(.4,0,.2,1);
  box-shadow:0 0 8px rgba(74,158,255,.5);}

/* ─── SCORE BADGES ───────────────────────────────────── */
.score-badge{display:flex;gap:8px;padding:0 12px 8px;flex-shrink:0;}
.badge{
  flex:1;text-align:center;padding:6px 4px;border-radius:var(--rad-sm);
  font-size:11px;font-weight:700;letter-spacing:.2px;
  background:var(--g0);border:1px solid var(--gb);}
.badge-correct{color:var(--grn);border-color:var(--grnB);}
.badge-wrong{color:var(--red);border-color:var(--redB);}
.badge-skip{color:var(--acc);border-color:rgba(74,158,255,.25);}

/* ─── QUESTION CARD ──────────────────────────────────── */
.q-card{
  background:var(--g1);
  backdrop-filter:var(--blur);-webkit-backdrop-filter:var(--blur);
  border:1px solid var(--gb2);border-radius:var(--rad);
  margin:0 12px 8px;padding:20px;
  box-shadow:0 4px 30px rgba(0,0,0,.35),0 0 0 1px rgba(255,255,255,.04);}
.q-card-top{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:12px;}
.q-card-badges{display:flex;align-items:center;gap:6px;flex-wrap:wrap;flex:1;}
.q-cat{
  font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:1px;
  padding:3px 9px;border-radius:5px;display:inline-block;}
.q-source{
  font-size:9px;font-weight:700;color:var(--sub);
  padding:3px 8px;border-radius:5px;display:inline-block;
  background:var(--g0);border:1px solid var(--gb);}
html.light .q-source{background:rgba(37,99,235,.05);border-color:rgba(37,99,235,.15);color:var(--acc);}
.fav-btn{
  background:none;border:none;cursor:pointer;font-size:20px;line-height:1;
  padding:0;flex-shrink:0;opacity:.45;transition:opacity .15s,transform .15s;}
.fav-btn:active{transform:scale(1.25);}
.fav-btn.active{opacity:1;}
.q-num{font-size:11px;color:var(--sub);margin-bottom:7px;letter-spacing:.3px;}
.q-text{font-size:16px;font-weight:600;line-height:1.6;color:var(--text);}
/* source line inside explanation */
.expl-source{font-size:10px;color:var(--amb);margin-top:8px;padding-top:7px;
  border-top:1px solid var(--ambB);letter-spacing:.2px;}

/* ─── CHOICE BUTTONS ─────────────────────────────────── */
.choices{margin:0 12px 8px;display:flex;flex-direction:column;gap:7px;}
.choice-btn{
  width:100%;text-align:left;
  background:var(--g0);
  backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  border:1px solid var(--gb);border-radius:var(--rad-sm);
  padding:13px 14px;font-size:13.5px;line-height:1.5;
  cursor:pointer;display:flex;align-items:flex-start;gap:10px;
  transition:all .15s;color:var(--text);}
.choice-btn:active:not(.disabled){
  transform:scale(.985);background:var(--g1);}
.choice-label{
  font-weight:800;font-size:12px;flex-shrink:0;margin-top:1px;
  color:var(--acc);letter-spacing:.3px;}
/* correct/wrong states */
.choice-btn.selected-correct{
  background:var(--grnL);border-color:var(--grn);color:var(--grn);
  box-shadow:0 0 12px rgba(0,212,124,.15);}
.choice-btn.selected-correct .choice-label{color:var(--grn);}
.choice-btn.selected-wrong{
  background:var(--redL);border-color:var(--red);color:var(--red);
  box-shadow:0 0 12px rgba(255,85,85,.15);}
.choice-btn.selected-wrong .choice-label{color:var(--red);}
.choice-btn.show-correct{
  background:var(--grnL);border-color:var(--grn);color:var(--grn);}
.choice-btn.show-correct .choice-label{color:var(--grn);}
.choice-btn.disabled{opacity:.5;cursor:default;}
.choice-icon{margin-left:auto;font-size:15px;flex-shrink:0;}

/* ─── EXPLANATION ────────────────────────────────────── */
.explanation{
  background:var(--ambL);
  backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  border:1px solid var(--ambB);border-radius:0 var(--rad-sm) var(--rad-sm) 0;
  border-left:2px solid var(--amb);
  margin:0 12px 8px;padding:13px 14px;
  font-size:13px;line-height:1.65;color:rgba(255,220,140,.85);display:none;}
.explanation.visible{display:block;}
.expl-title{
  font-weight:800;margin-bottom:5px;font-size:10px;text-transform:uppercase;
  letter-spacing:.8px;color:var(--amb);}

/* ─── NAV BUTTONS ────────────────────────────────────── */
.q-nav{display:flex;gap:9px;padding:4px 12px 10px;flex-shrink:0;}
.btn-prev{
  flex:0 0 76px;padding:12px;border-radius:var(--rad-sm);
  border:1px solid var(--gb2);background:var(--g0);
  backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  font-size:14px;font-weight:700;color:var(--sub);cursor:pointer;transition:all .15s;}
.btn-prev:disabled{opacity:.25;}
.btn-next{
  flex:1;padding:12px;border-radius:var(--rad-sm);border:none;
  background:linear-gradient(135deg,#3D7EFF 0%,#6AABFF 100%);
  color:#fff;font-size:15px;font-weight:800;cursor:pointer;
  letter-spacing:.2px;transition:opacity .15s;
  box-shadow:0 0 20px rgba(74,158,255,.35);}
.btn-next:disabled{opacity:.30;}

/* ─── DONE SCREEN ────────────────────────────────────── */
.done-wrap{
  flex:1;display:flex;flex-direction:column;align-items:center;
  justify-content:center;padding:36px 28px;text-align:center;}
.done-emoji{font-size:60px;margin-bottom:18px;filter:drop-shadow(0 0 20px rgba(255,255,255,.2));}
.done-title{font-size:24px;font-weight:800;color:var(--text);
  background:linear-gradient(90deg,#A8C8FF,#fff,#A8C8FF);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.done-score{
  font-size:52px;font-weight:900;margin:18px 0 4px;
  background:linear-gradient(90deg,var(--acc),#80C4FF);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  filter:drop-shadow(0 0 12px rgba(74,158,255,.4));}
.done-pct{font-size:15px;color:var(--sub);}
.done-sub{font-size:14px;color:var(--sub);line-height:1.7;margin-top:10px;}
.btn-reset{
  margin-top:26px;padding:14px 38px;border-radius:var(--rad);
  background:linear-gradient(135deg,#3D7EFF,#6AABFF);
  color:#fff;border:none;font-size:16px;font-weight:800;cursor:pointer;
  box-shadow:0 0 24px rgba(74,158,255,.4);}

/* ─── REFERENCE ──────────────────────────────────────── */
.search-wrap{
  padding:12px;
  background:rgba(7,9,26,.60);
  backdrop-filter:var(--blur);-webkit-backdrop-filter:var(--blur);
  border-bottom:1px solid var(--gb);flex-shrink:0;}
.search-input{
  width:100%;padding:10px 14px;border-radius:var(--rad-sm);
  border:1px solid var(--gb2);
  background:var(--g1);
  backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
  font-size:14px;color:var(--text);outline:none;}
.search-input::placeholder{color:var(--sub);}
.search-input:focus{border-color:var(--acc);box-shadow:0 0 0 2px var(--accG);}

.topic-group{
  margin:0 12px 10px;
  background:var(--g0);
  backdrop-filter:var(--blur);-webkit-backdrop-filter:var(--blur);
  border:1px solid var(--gb);border-radius:var(--rad);overflow:hidden;}
.topic-hdr{
  display:flex;align-items:center;justify-content:space-between;
  padding:14px 16px;cursor:pointer;user-select:none;}
.topic-title{font-size:15px;font-weight:800;letter-spacing:.1px;}
.chev{font-size:13px;color:var(--sub);transition:transform .25s;}
.chev.open{transform:rotate(180deg);}
.topic-body{display:none;padding:0 14px 14px;}
.topic-body.open{display:block;}
.sec-title{
  font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.7px;
  color:var(--sub);margin:12px 0 7px;}
table.rt{width:100%;border-collapse:collapse;font-size:12.5px;}
table.rt th{
  background:rgba(255,255,255,.04);padding:7px 9px;text-align:left;
  font-weight:700;font-size:11px;letter-spacing:.3px;
  border-bottom:1px solid var(--gb2);color:var(--sub);}
table.rt td{
  padding:7px 9px;border-bottom:1px solid rgba(255,255,255,.04);
  vertical-align:top;line-height:1.5;color:var(--text);}
table.rt tr:last-child td{border-bottom:none;}
table.rt tr:hover td{background:rgba(255,255,255,.025);}

/* ─── PROGRESS TAB ───────────────────────────────────── */
.stats-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:16px;}
.stat-card{
  background:var(--g1);
  backdrop-filter:var(--blur);-webkit-backdrop-filter:var(--blur);
  border:1px solid var(--gb);border-radius:var(--rad);
  padding:18px;text-align:center;}
.stat-num{font-size:34px;font-weight:800;color:var(--acc);}
.stat-label{font-size:12px;color:var(--sub);margin-top:4px;letter-spacing:.2px;}
.tp-card{
  margin:0 16px 8px;
  background:var(--g1);
  backdrop-filter:var(--blur);-webkit-backdrop-filter:var(--blur);
  border:1px solid var(--gb);border-radius:var(--rad);padding:14px 16px;}
.tp-row{display:flex;align-items:center;gap:8px;margin-bottom:5px;}
.tp-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;}
.tp-name{font-size:14px;flex:1;font-weight:500;}
.tp-pct{font-size:13px;font-weight:800;color:var(--acc);}
.tp-bar-bg{height:3px;background:rgba(255,255,255,.08);border-radius:2px;overflow:hidden;}
.tp-bar-fill{height:100%;border-radius:2px;transition:width .5s cubic-bezier(.4,0,.2,1);
  box-shadow:0 0 6px rgba(74,158,255,.4);}
.pad{height:28px;}

/* ─── FAVORITES CARD ─────────────────────────────────── */
.fav-review-card{
  margin-bottom:18px;
  background:var(--g1);
  backdrop-filter:var(--blur);-webkit-backdrop-filter:var(--blur);
  border-radius:var(--rad);
  padding:16px;
  border:1px solid var(--gb);
}

/* ─── LIGHT MODE ─────────────────────────────────────── */
html.light{
  --bg:#F0F4FF;--bg2:#FFFFFF;
  --g0:rgba(255,255,255,.80);--g1:rgba(255,255,255,.92);--g2:rgba(255,255,255,1);
  --gb:rgba(30,40,100,.10);--gb2:rgba(30,40,100,.18);
  --acc:#2563EB;--accL:rgba(37,99,235,.10);--accG:rgba(37,99,235,.05);
  --text:#1A2133;--sub:rgba(26,33,51,.52);--sub2:rgba(26,33,51,.32);
  --grn:#059669;--grnL:rgba(5,150,105,.09);--grnB:rgba(5,150,105,.28);
  --red:#DC2626;--redL:rgba(220,38,38,.09);--redB:rgba(220,38,38,.28);
  --amb:#B45309;--ambL:rgba(180,83,9,.07);--ambB:rgba(180,83,9,.25);
}
html.light body::before{
  background:
    radial-gradient(ellipse 60% 50% at 15% 10%, rgba(99,131,255,.10) 0%, transparent 70%),
    radial-gradient(ellipse 50% 40% at 85% 85%, rgba(59,130,246,.07) 0%, transparent 60%),
    linear-gradient(160deg,#EEF2FF 0%,#F8FAFF 60%,#EEF2FF 100%);
}
html.light body::after{
  background-image:radial-gradient(rgba(30,40,120,.05) 1px, transparent 1px);
}
html.light .header{background:rgba(240,244,255,.88);}
html.light .header-title{
  background:linear-gradient(90deg,#2563EB 0%,#1A2133 55%,#2563EB 100%);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
}
html.light .tab-bar{background:rgba(240,244,255,.90);}
html.light .filter-bar{background:rgba(248,250,255,.80);}
html.light .search-wrap{background:rgba(248,250,255,.82);}
html.light .prog-track{background:rgba(30,40,100,.08);}
html.light .tp-bar-bg{background:rgba(30,40,100,.08);}
html.light table.rt th{background:rgba(37,99,235,.04);}
html.light table.rt td{border-bottom-color:rgba(30,40,100,.06);}
html.light table.rt tr:hover td{background:rgba(37,99,235,.04);}
html.light .q-card{box-shadow:0 4px 24px rgba(30,40,100,.10),0 0 0 1px rgba(37,99,235,.06);}
html.light .explanation{color:rgba(110,65,10,.85);}
html.light .done-title{
  background:linear-gradient(90deg,#2563EB,#1A2133,#2563EB);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
}
/* theme toggle button */
.theme-toggle{
  background:var(--g1);backdrop-filter:var(--blur);-webkit-backdrop-filter:var(--blur);
  border:1px solid var(--gb2);border-radius:50%;width:36px;height:36px;
  font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;
  transition:background .2s,border-color .2s;flex-shrink:0;line-height:1;padding:0;
}
.header-inner{display:flex;align-items:center;justify-content:space-between;gap:12px;}
</style>
<script>(function(){var t=localStorage.getItem('pbs_theme')||'light';if(t==='light')document.documentElement.classList.add('light');})();</script>
</head>
<body>
<div id="app">
  <div class="header">
    <div class="header-inner">
      <div>
        <div class="header-title">CutPH Reviewers</div>
        <div class="header-sub" id="header-sub">Board Prep for General Surgery Residents &nbsp;·&nbsp; 85 MCQs</div>
      </div>
      <button id="theme-btn" class="theme-toggle" onclick="toggleTheme()" title="Toggle light/dark mode">🌙</button>
    </div>
  </div>

  <!-- ── QUIZ PANEL ── -->
  <div id="panel-quiz" class="tab-panel active">
    <div id="filter-bar" class="filter-bar"></div>
    <div class="prog-wrap">
      <div class="prog-labels">
        <span id="prog-lbl">Question 1 of 85</span>
        <span id="prog-pct">0%</span>
      </div>
      <div class="prog-track"><div id="prog-fill" class="prog-fill" style="width:0%"></div></div>
    </div>
    <div class="score-badge">
      <div class="badge badge-correct">✓ <span id="sc-correct">0</span> Correct</div>
      <div class="badge badge-wrong">✗ <span id="sc-wrong">0</span> Wrong</div>
      <div class="badge badge-skip">→ <span id="sc-skip">0</span> Skipped</div>
    </div>
    <div id="quiz-body" class="scroll-area"></div>
    <div id="done-wrap" class="done-wrap" style="display:none;"></div>
    <div class="q-nav" id="q-nav">
      <button class="btn-prev" id="btn-prev" onclick="prevQ()">‹ Back</button>
      <button class="btn-next" id="btn-next" onclick="nextQ()">Next ›</button>
    </div>
  </div>

  <!-- ── REFERENCE PANEL ── -->
  <div id="panel-ref" class="tab-panel">
    <div class="search-wrap">
      <input class="search-input" id="search-input" placeholder="Search tables…" oninput="filterRef()"/>
    </div>
    <div class="scroll-area" id="ref-scroll">
      <div id="ref-area" style="padding-top:10px;"></div>
      <div class="pad"></div>
    </div>
  </div>

  <!-- ── PROGRESS PANEL ── -->
  <div id="panel-prog" class="tab-panel">
    <div class="scroll-area" id="prog-scroll">
      <div id="stats-area"></div>
      <div class="pad"></div>
    </div>
  </div>

  <!-- ── FAVORITES PANEL ── -->
  <div id="panel-fav" class="tab-panel">
    <div class="scroll-area" id="fav-scroll">
      <div id="fav-area" style="padding:12px 16px;"></div>
      <div class="pad"></div>
    </div>
  </div>

  <!-- ── TAB BAR ── -->
  <div class="tab-bar">
    <button class="tab-btn active" id="tab-quiz" onclick="switchTab('quiz')">
      <span class="tab-icon">📝</span>Quiz
    </button>
    <button class="tab-btn" id="tab-ref" onclick="switchTab('ref')">
      <span class="tab-icon">📋</span>Reference
    </button>
    <button class="tab-btn" id="tab-prog" onclick="switchTab('prog')">
      <span class="tab-icon">📊</span>Progress
    </button>
    <button class="tab-btn" id="tab-fav" onclick="switchTab('fav')">
      <span class="tab-icon">⭐</span>Favorites
    </button>
  </div>
</div>

<script>
const CARDS = CARDS_DATA;
const REF   = REF_DATA;
const LABELS = ["A","B","C","D"];

let state = {
  filter:"All", deck:[], idx:0,
  shuffled:[], answered:{}, expanded:{}, favorites:new Set()
};

function saveState(){
  try{
    localStorage.setItem("pbs_mcq",JSON.stringify({
      answered:state.answered,
      favorites:[...state.favorites]
    }));
  }catch(e){}
}
function loadState(){
  try{
    const s=JSON.parse(localStorage.getItem("pbs_mcq")||"{}");
    if(s.answered) state.answered=s.answered;
    if(s.favorites) state.favorites=new Set(s.favorites);
  }catch(e){}
}
function toggleFav(qid){
  if(state.favorites.has(qid)) state.favorites.delete(qid);
  else state.favorites.add(qid);
  saveState();
  const btn=document.getElementById("fav-btn-"+qid);
  if(btn){ btn.textContent=state.favorites.has(qid)?"⭐":"☆"; btn.classList.toggle("active",state.favorites.has(qid)); }
  // Refresh filter pills to show correct fav count
  buildFilters();
  // Refresh fav tab count badge
  const favTab=document.getElementById("tab-fav");
  if(favTab){
    const n=state.favorites.size;
    favTab.innerHTML=`<span class="tab-icon">⭐</span>Fav${n>0?" ("+n+")":""}`;
  }
}

function getCatColor(cat){
  const m={"Hernia":"#6AB0FF","Appendicitis":"#CC88FF","Skin & STS":"#FF9070",
    "Thyroid":"#40E0B0","Parathyroid":"#FFAA55","Breast/Pregnancy":"#FF80B0",
    "BDI":"#60DD90","Hereditary":"#A090FF","General":"#90AABF"};
  return m[cat]||"#8899BB";
}
function getCatGlow(cat){
  const m={"Hernia":"rgba(106,176,255,.15)","Appendicitis":"rgba(204,136,255,.15)",
    "Skin & STS":"rgba(255,144,112,.15)","Thyroid":"rgba(64,224,176,.15)",
    "Parathyroid":"rgba(255,170,85,.15)","Breast/Pregnancy":"rgba(255,128,176,.15)",
    "BDI":"rgba(96,221,144,.15)","Hereditary":"rgba(160,144,255,.15)","General":"rgba(144,170,191,.15)"};
  return m[cat]||"rgba(136,153,187,.15)";
}

function seededShuffle(arr,seed){
  const a=[...arr]; let s=seed;
  for(let i=a.length-1;i>0;i--){
    s=(s*1664525+1013904223)&0xffffffff;
    const j=((s>>>0)%(i+1));
    [a[i],a[j]]=[a[j],a[i]];
  }
  return a;
}
function getShuffled(cardId){
  if(!state.shuffled[cardId]) state.shuffled[cardId]=seededShuffle([0,1,2,3],cardId*7+13);
  return state.shuffled[cardId];
}

function buildFilters(){
  const cats=["All",...new Set(CARDS.map(c=>c.cat))];
  const bar=document.getElementById("filter-bar");
  bar.innerHTML="";
  // Category pills
  cats.forEach(c=>{
    const p=document.createElement("button");
    p.className="pill"+(state.filter===c?" active":"");
    p.textContent=c;
    p.onclick=()=>{ state.filter=c; state.idx=0; state.shuffled=[]; updateDeck(); buildFilters(); renderQ(); };
    bar.appendChild(p);
  });
  // Favorites pill
  const favCount=state.favorites.size;
  const fp=document.createElement("button");
  fp.className="pill pill-fav"+(state.filter==="⭐ Favorites"?" active":"");
  fp.textContent=`⭐ Favorites${favCount>0?" ("+favCount+")":""}`;
  fp.onclick=()=>{ state.filter="⭐ Favorites"; state.idx=0; state.shuffled=[]; updateDeck(); buildFilters(); renderQ(); };
  bar.appendChild(fp);
}
function updateDeck(){
  if(state.filter==="All") state.deck=[...CARDS];
  else if(state.filter==="⭐ Favorites") state.deck=CARDS.filter(c=>state.favorites.has(c.id));
  else state.deck=CARDS.filter(c=>c.cat===state.filter);
}

function renderQ(){
  const D=state.deck, i=state.idx;
  const body=document.getElementById("quiz-body");
  const doneW=document.getElementById("done-wrap");
  const nav=document.getElementById("q-nav");
  const total=D.length;

  const pct=total>0?Math.round((i/total)*100):0;
  document.getElementById("prog-lbl").textContent=`Question ${Math.min(i+1,total)} of ${total}`;
  document.getElementById("prog-fill").style.width=pct+"%";
  document.getElementById("prog-pct").textContent=pct+"%";

  let correct=0,wrong=0,skip=0;
  D.forEach((card,j)=>{
    const a=state.answered[j];
    if(a===undefined) return;
    if(a===-1){ skip++; return; }
    if(getShuffled(card.id)[a]===0) correct++; else wrong++;
  });
  document.getElementById("sc-correct").textContent=correct;
  document.getElementById("sc-wrong").textContent=wrong;
  document.getElementById("sc-skip").textContent=skip;

  if(total===0){
    body.style.display="none"; nav.style.display="none";
    doneW.style.display="flex";
    doneW.innerHTML=`
      <div class="done-emoji">☆</div>
      <div class="done-title">No Favorites Yet</div>
      <div class="done-sub" style="margin-top:12px;">Tap the ☆ on any question to star it, then come back here to drill your saved questions.</div>
      <button class="btn-reset" onclick="state.filter='All';state.idx=0;state.shuffled=[];updateDeck();buildFilters();renderQ()">Back to All Questions</button>`;
    return;
  }

  if(i>=total){
    body.style.display="none"; nav.style.display="none";
    doneW.style.display="flex";
    const ps=total>0?Math.round((correct/total)*100):0;
    doneW.innerHTML=`
      <div class="done-emoji">${ps>=80?"🏆":ps>=60?"🎯":"📚"}</div>
      <div class="done-title">Deck Complete</div>
      <div class="done-score">${correct}/${total}</div>
      <div class="done-pct">${ps}% correct</div>
      <div class="done-sub">${ps>=80?"Outstanding — you're board-ready on this deck.":ps>=60?"Solid effort — review the ones you missed.":"Use the Reference tab and try again."}</div>
      <button class="btn-reset" onclick="resetQuiz()">Restart Deck</button>`;
    return;
  }

  doneW.style.display="none"; body.style.display="block"; nav.style.display="flex";
  body.scrollTop=0;

  const card=D[i];
  const ord=getShuffled(card.id);
  const chosen=state.answered[i];
  const answered=chosen!==undefined;

  // Render choices IN SHUFFLED ORDER: display position ci shows card.choices[ord[ci]]
  const choicesHTML=ord.map((origIdx,ci)=>{
    const txt=card.choices[origIdx];
    let cls="choice-btn"; let icon="";
    if(answered){
      cls+=" disabled";
      if(ci===chosen && origIdx===0){ cls+=" selected-correct"; icon=`<span class="choice-icon">✓</span>`; }
      else if(ci===chosen && origIdx!==0){ cls+=" selected-wrong"; icon=`<span class="choice-icon">✗</span>`; }
      else if(origIdx===0){ cls+=" show-correct"; icon=`<span class="choice-icon">✓</span>`; }
    }
    return `<button class="${cls}" onclick="answer(${ci})" ${answered?"disabled":""}>
      <span class="choice-label">${LABELS[ci]}</span>
      <span style="flex:1">${esc(txt)}</span>${icon}
    </button>`;
  }).join("");

  const col=getCatColor(card.cat), glow=getCatGlow(card.cat);
  const isFav=state.favorites.has(card.id);
  body.innerHTML=`
    <div class="q-card">
      <div class="q-card-top">
        <div class="q-card-badges">
          <span class="q-cat" style="background:${glow};color:${col};border:1px solid ${col}33;">${card.cat}</span>
          ${card.source?`<span class="q-source">${esc(card.source)}</span>`:""}
        </div>
        <button id="fav-btn-${card.id}" class="fav-btn${isFav?" active":""}"
          onclick="toggleFav(${card.id})" title="${isFav?"Remove from favorites":"Add to favorites"}"
          aria-label="Favorite">${isFav?"⭐":"☆"}</button>
      </div>
      <div class="q-num">Q${i+1} &nbsp;/&nbsp; ${total}</div>
      <div class="q-text">${esc(card.q)}</div>
    </div>
    <div class="choices">${choicesHTML}</div>
    <div class="explanation${answered?" visible":""}" id="expl">
      <div class="expl-title">Explanation</div>
      ${esc(card.explanation)}
      ${card.source&&answered?`<div class="expl-source">📚 Source: ${esc(card.source)}</div>`:""}
    </div>`;

  const nextBtn=document.getElementById("btn-next");
  nextBtn.textContent=i>=total-1&&answered?"Finish ›":!answered?"Skip →":"Next ›";
  document.getElementById("btn-prev").disabled=i===0;
}

function esc(t){ return String(t).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }
function answer(ci){
  if(state.answered[state.idx]!==undefined) return;
  state.answered[state.idx]=ci; saveState(); renderQ();
}
function nextQ(){
  if(state.answered[state.idx]===undefined) state.answered[state.idx]=-1;
  state.idx++; saveState(); renderQ();
  document.getElementById("quiz-body").scrollTop=0;
}
function prevQ(){ if(state.idx>0){ state.idx--; renderQ(); } }
function resetQuiz(){
  state.idx=0; state.answered={}; state.shuffled=[];
  localStorage.removeItem("pbs_mcq");
  document.getElementById("done-wrap").style.display="none";
  document.getElementById("q-nav").style.display="flex";
  renderQ();
}

function buildRef(q=""){
  const area=document.getElementById("ref-area");
  area.innerHTML="";
  REF.forEach(topic=>{
    const secs=q?topic.sections.filter(s=>{
      const h=(s.title+" "+s.table.headers.join(" ")+s.table.rows.flat().join(" ")).toLowerCase();
      return h.includes(q.toLowerCase());
    }):topic.sections;
    if(!secs.length) return;
    const isOpen=state.expanded[topic.topic]||!!q;
    const g=document.createElement("div");
    g.className="topic-group";
    g.innerHTML=`
      <div class="topic-hdr" onclick="toggleRef('${topic.topic}')">
        <span class="topic-title" style="color:${getCatColor(topic.topic)}">${topic.topic}</span>
        <span class="chev${isOpen?" open":""}" id="chev-${topic.topic}">▾</span>
      </div>
      <div class="topic-body${isOpen?" open":""}" id="tbody-${topic.topic}">
        ${secs.map(s=>`
          <div class="sec-title">${s.title}</div>
          <table class="rt">
            <thead><tr>${s.table.headers.map(h=>`<th>${h}</th>`).join("")}</tr></thead>
            <tbody>${s.table.rows.map(r=>`<tr>${r.map(c=>`<td>${c}</td>`).join("")}</tr>`).join("")}</tbody>
          </table>`).join("")}
      </div>`;
    area.appendChild(g);
  });
}
function toggleRef(t){
  state.expanded[t]=!state.expanded[t];
  document.getElementById("tbody-"+t).classList.toggle("open",state.expanded[t]);
  document.getElementById("chev-"+t).classList.toggle("open",state.expanded[t]);
}
function filterRef(){ buildRef(document.getElementById("search-input").value); }

function buildProgress(){
  const total=CARDS.length;
  let correct=0,wrong=0,skip=0;
  CARDS.forEach((card,j)=>{
    const a=state.answered[j];
    if(a===undefined) return;
    if(a===-1){ skip++; return; }
    if(getShuffled(card.id)[a]===0) correct++; else wrong++;
  });
  const reviewed=correct+wrong+skip;

  const cats=[...new Set(CARDS.map(c=>c.cat))];
  const rows=cats.map(cat=>{
    let ci=0,wi=0,ti=0;
    CARDS.forEach((card,j)=>{
      if(card.cat!==cat) return; ti++;
      const a=state.answered[j];
      if(a===undefined||a===-1) return;
      if(getShuffled(card.id)[a]===0) ci++; else wi++;
    });
    const pct=ti>0?Math.round((ci/ti)*100):0;
    return {cat,total:ti,correct:ci,wrong:wi,pct,color:getCatColor(cat)};
  });

  document.getElementById("stats-area").innerHTML=`
    <div class="stats-grid">
      <div class="stat-card"><div class="stat-num">${total}</div><div class="stat-label">Total Questions</div></div>
      <div class="stat-card"><div class="stat-num">${reviewed}</div><div class="stat-label">Answered</div></div>
      <div class="stat-card"><div class="stat-num" style="color:var(--grn)">${correct}</div><div class="stat-label">Correct ✓</div></div>
      <div class="stat-card"><div class="stat-num" style="color:var(--red)">${wrong}</div><div class="stat-label">Wrong ✗</div></div>
    </div>
    <div style="padding:0 16px 10px;font-size:10px;font-weight:800;color:var(--sub);text-transform:uppercase;letter-spacing:.7px">By Topic</div>
    ${rows.map(r=>`
      <div class="tp-card">
        <div class="tp-row">
          <div class="tp-dot" style="background:${r.color};box-shadow:0 0 6px ${r.color}88"></div>
          <div class="tp-name">${r.cat}</div>
          <div class="tp-pct">${r.pct}%</div>
        </div>
        <div class="tp-bar-bg">
          <div class="tp-bar-fill" style="width:${r.pct}%;background:linear-gradient(90deg,${r.color},${r.color}BB)"></div>
        </div>
        <div style="font-size:10px;color:var(--sub);margin-top:4px;letter-spacing:.2px">
          ${r.correct} correct &nbsp;·&nbsp; ${r.wrong} wrong &nbsp;·&nbsp; ${r.total-r.correct-r.wrong} unanswered
        </div>
      </div>`).join("")}
    <div style="padding:16px;text-align:center;">
      <button class="btn-reset" style="background:linear-gradient(135deg,#C03030,#FF5555);"
        onclick="if(confirm('Reset all quiz progress?')){state.answered={};state.shuffled=[];localStorage.removeItem('pbs_mcq');state.idx=0;buildProgress();switchTab('quiz');}">
        Reset All Progress
      </button>
    </div>`;
}

function switchTab(name){
  ["quiz","ref","prog","fav"].forEach(t=>{
    document.getElementById("panel-"+t).classList.toggle("active",t===name);
    document.getElementById("tab-"+t).classList.toggle("active",t===name);
  });
  if(name==="ref") buildRef();
  if(name==="prog") buildProgress();
  if(name==="fav") buildFav();
}

function buildFav(){
  const area=document.getElementById("fav-area");
  const favCards=CARDS.filter(c=>state.favorites.has(c.id));
  if(favCards.length===0){
    area.innerHTML=`<div style="text-align:center;padding:48px 24px;color:var(--sub);">
      <div style="font-size:2.4rem;margin-bottom:12px;">☆</div>
      <div style="font-size:1rem;font-weight:600;margin-bottom:8px;">No Favorites Yet</div>
      <div style="font-size:.85rem;line-height:1.5;">Tap the ☆ on any quiz question to star it — your favorites appear here as a study list.</div>
    </div>`;
    return;
  }
  area.innerHTML=`<div style="font-size:.7rem;font-weight:800;text-transform:uppercase;letter-spacing:.7px;color:var(--sub);margin-bottom:12px;">${favCards.length} Saved Question${favCards.length!==1?"s":""}</div>` +
    favCards.map((card,idx)=>{
      const catColor=getCatColor(card.cat);
      return `<div class="fav-review-card">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px;">
          <div style="display:flex;gap:6px;flex-wrap:wrap;">
            <span style="font-size:.68rem;font-weight:700;padding:3px 8px;border-radius:20px;background:${catColor}22;color:${catColor};">${esc(card.cat)}</span>
            ${card.source?`<span class="q-source" style="font-size:.65rem;">${esc(card.source)}</span>`:""}
          </div>
          <button onclick="toggleFav(${card.id});buildFav();" style="background:none;border:none;cursor:pointer;font-size:1.1rem;color:var(--acc);padding:0;line-height:1;">⭐</button>
        </div>
        <div style="font-size:.88rem;font-weight:600;color:var(--text);line-height:1.5;margin-bottom:12px;">${esc(card.q)}</div>
        <div style="background:rgba(0,212,124,.12);border-left:3px solid var(--grn);border-radius:0 8px 8px 0;padding:8px 12px;margin-bottom:10px;">
          <div style="font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.5px;color:var(--grn);margin-bottom:4px;">✓ Correct Answer</div>
          <div style="font-size:.88rem;color:var(--text);font-weight:500;">${esc(card.choices[0] || "N/A")}</div>
        </div>
        <div style="font-size:.82rem;color:var(--sub);line-height:1.55;">${esc(card.explanation)}</div>
        ${card.source?`<div class="expl-source" style="margin-top:8px;">📚 Source: ${esc(card.source)}</div>`:""}
      </div>`;
    }).join("");
}

function toggleTheme(){
  const light=document.documentElement.classList.toggle('light');
  localStorage.setItem('pbs_theme',light?'light':'dark');
  document.getElementById('theme-btn').textContent=light?'🌙':'☀️';
}

loadState();
buildFilters();
updateDeck();
renderQ();
// Set correct icon for current theme
document.getElementById('theme-btn').textContent=
  document.documentElement.classList.contains('light')?'🌙':'☀️';
// Update header subtitle with actual question count
const hsub=document.getElementById('header-sub');
if(hsub) hsub.innerHTML=`Board Prep for General Surgery Residents &nbsp;·&nbsp; ${CARDS.length} MCQs`;
// Update fav tab badge on load
(function(){
  const n=state.favorites.size;
  const ft=document.getElementById('tab-fav');
  if(ft&&n>0) ft.innerHTML=`<span class="tab-icon">⭐</span>Fav (${n})`;
})();
</script>
</body>
</html>'''

# Output with configurable path
output_dir = os.getenv("OUTPUT_DIR", os.path.expanduser("~/Desktop"))
out = os.path.join(output_dir, "PBS_Board_Review_App.html")

try:
    os.makedirs(output_dir, exist_ok=True)
    cards_js = json.dumps(CARDS, ensure_ascii=False)
    ref_js   = json.dumps(REF,   ensure_ascii=False)
    output   = HTML.replace("CARDS_DATA", cards_js).replace("REF_DATA", ref_js)
    
    with open(out, "w", encoding="utf-8") as f:
        f.write(output)
    
    size_kb = len(output.encode("utf-8")) / 1024
    print(f"✓ Written: {out}")
    print(f"  File size: {size_kb:.1f} KB")
except IOError as e:
    print(f"✗ Write failed: {e}", file=sys.stderr)
    sys.exit(1)
