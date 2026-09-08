#!/usr/bin/env python3
"""Regenerates the six profile-README figures (sheet + board renditions).

Run from the repo root:  python tools/generate-figures.py
Edit geometry once here, never edit the SVGs by hand. GitHub XML-parses SVGs,
so escape < and & in any text you add, then re-validate before committing."""
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
os.makedirs(OUT, exist_ok=True)

SERIF = "'Libre Caslon Text',Georgia,'Times New Roman',serif"
SANS  = "'Atkinson Hyperlegible',-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"
MONO  = "'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

SHEET = dict(
    key="sheet",
    bg="#F4F5F0", grid="#C9D7E6", grid5="#ADC3D8", frame="#1A2434",
    ink="#141C2B", muted="#5C687A", ox="#7C242C", cobalt="#1B4F9C",
    hl="#F0E05C", hlop="0.55", hltext="#141C2B", boxfill="#FAFAF6", hatchop="0.55",
)
BOARD = dict(
    key="board",
    bg="#25342E", grid="#37493F", grid5="#465B50", frame="#C4D0C7",
    ink="#EFEFE4", muted="#9FAEA4", ox="#E58176", cobalt="#8FBBE0",
    hl="#E8CE63", hlop="0.28", hltext="#22302A", boxfill="#2C3D36", hatchop="0.7",
)

def head(w, h, p, gridsize=16):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
<defs>
<pattern id="q1" width="{gridsize}" height="{gridsize}" patternUnits="userSpaceOnUse">
<path d="M{gridsize} 0H0V{gridsize}" fill="none" stroke="{p['grid']}" stroke-width="0.6"/>
</pattern>
<pattern id="q2" width="{gridsize*5}" height="{gridsize*5}" patternUnits="userSpaceOnUse">
<path d="M{gridsize*5} 0H0V{gridsize*5}" fill="none" stroke="{p['grid5']}" stroke-width="0.9"/>
</pattern>
<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M0 0 L10 5 L0 10 z" fill="{p['cobalt']}"/>
</marker>
</defs>
<rect width="{w}" height="{h}" fill="{p['bg']}"/>
<rect width="{w}" height="{h}" fill="url(#q1)"/>
<rect width="{w}" height="{h}" fill="url(#q2)"/>
'''

def frame(w, h, p):
    return (f'<rect x="28" y="28" width="{w-56}" height="{h-56}" fill="none" '
            f'stroke="{p["frame"]}" stroke-width="1.1"/>\n')

def hdr(w, p, num, right):
    return (f'<text x="56" y="62" font-family="{MONO}" font-size="11" letter-spacing="1.7" '
            f'fill="{p["muted"]}">FIG. {num}</text>\n'
            f'<text x="{w-56}" y="62" text-anchor="end" font-family="{MONO}" font-size="11" '
            f'fill="{p["muted"]}">{right}</text>\n'
            f'<path d="M56 76H{w-56}" stroke="{p["muted"]}" stroke-width="0.7" opacity="0.55"/>\n')

def txt(x, y, s, font, size, fill, anchor="start", style="normal", ls=None, weight=None):
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    st = f' font-style="italic"' if style == "italic" else ""
    l = f' letter-spacing="{ls}"' if ls else ""
    wt = f' font-weight="{weight}"' if weight else ""
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" fill="{fill}"'
            f'{a}{st}{l}{wt}>{s}</text>\n')

def hl(x, y, w, h, p):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{p["hl"]}" opacity="{p["hlop"]}"/>\n'


# ---------------------------------------------------------------- FIG 1
def fig1(p):
    W, H = 1280, 440
    s = head(W, H, p)
    s += frame(W, H, p)
    s += hdr(W, p, 1, "github.com/pyogi37")

    # left column
    s += txt(64, 162, "Priyanshu Yogi", SERIF, 54, p["ink"])
    s += f'<path d="M64 182H336" stroke="{p["ox"]}" stroke-width="2.2"/>\n'
    s += txt(64, 216, "Forward deployed engineer.", SERIF, 20, p["ink"], style="italic")
    s += txt(64, 244, "Applied AI, discovery through deployment.", SERIF, 20, p["muted"], style="italic")
    s += txt(64, 292, "Three years turning ambiguous customer problems", SANS, 13.5, p["ink"])
    s += hl(61, 300, 340, 20, p)
    s += txt(64, 315, "into systems that survive contact with reality.", SANS, 13.5, p["ink"])
    s += txt(64, 356, "Jaipur, India  ·  priyanshu.fyi  ·  open to remote", MONO, 12, p["muted"])
    s += txt(64, 394, "Fig. 1. One point per system understood before the next one could be built.",
             SERIF, 12.5, p["muted"], style="italic")

    # plot frame
    x0, x1, ytop, yb = 640, 1200, 110, 356
    s += f'<path d="M{x0} {ytop}V{yb}H{x1}" fill="none" stroke="{p["ink"]}" stroke-width="1.3"/>\n'
    for i in range(1, 9):
        tx = x0 + i * 62
        if tx < x1:
            s += f'<path d="M{tx} {yb}v-6" stroke="{p["ink"]}" stroke-width="0.9"/>\n'
    for i in range(1, 6):
        ty = yb - i * 41
        if ty > ytop:
            s += f'<path d="M{x0} {ty}h6" stroke="{p["ink"]}" stroke-width="0.9"/>\n'
    s += txt(920, 386, "x  systems understood", SERIF, 12.5, p["muted"], anchor="middle", style="italic")
    s += (f'<g transform="rotate(-90 612 233)">'
          + txt(612, 233, "y  systems built", SERIF, 12.5, p["muted"], anchor="middle", style="italic").strip()
          + '</g>\n')

    # curve
    s += (f'<path d="M646 332 C700 324, 748 306, 792 288 C852 266, 890 254, 944 236 '
          f'C1016 212, 1082 184, 1132 142" fill="none" stroke="{p["ox"]}" stroke-width="2.4" '
          f'stroke-linecap="round"/>\n')
    # projection
    s += (f'<path d="M1132 142 L1188 112" fill="none" stroke="{p["cobalt"]}" stroke-width="1.7" '
          f'stroke-dasharray="5 4" marker-end="url(#ah)"/>\n')

    pts = [(662, 322, "full stack, built from scratch"),
           (792, 288, "computer vision at the edge"),
           (944, 236, "enterprise deployment, 7 countries")]
    for (px, py, lab) in pts:
        s += f'<circle cx="{px}" cy="{py}" r="4.2" fill="{p["bg"]}" stroke="{p["ink"]}" stroke-width="1.5"/>\n'
        s += txt(px + 11, py + 18, lab, SANS, 11.5, p["muted"])

    # selected point
    s += f'<circle cx="1132" cy="142" r="11" fill="none" stroke="{p["ox"]}" stroke-width="1" stroke-dasharray="2 3"/>\n'
    s += f'<circle cx="1132" cy="142" r="5.6" fill="{p["ox"]}"/>\n'
    s += f'<path d="M1124 136 L1090 118 H1064" fill="none" stroke="{p["ox"]}" stroke-width="1"/>\n'
    s += hl(764, 106, 296, 22, p)
    s += txt(1056, 123, "now: agentic systems, shipped with evals", SERIF, 15, p["ox"],
             anchor="end", style="italic")
    s += '</svg>\n'
    return s


# ---------------------------------------------------------------- FIG 2
def fig2(p):
    W, H = 1280, 390
    s = head(W, H, p)
    s += frame(W, H, p)
    s += hdr(W, p, 2, "github.com/pyogi37/signalroom")

    s += txt(64, 110, "SignalRoom", SERIF, 26, p["ink"])
    s += txt(228, 110, "discovery transcript in, solution brief out, every claim traceable to a quote",
             SERIF, 15, p["muted"], style="italic")

    stages = [
        ("discover", ["no model, just", "speaker-attributed lines"]),
        ("extract",  ["every quote must be a", "verbatim substring"]),
        ("retrieve", ["SQLite full-text search,", "not a vector store"]),
        ("design",   ["brief assembled from", "cited claims only"]),
        ("critique", ["contradictions, gaps,", "open items"]),
        ("gate",     ["human interrupt,", "checkpointed, resumable"]),
    ]
    bx, bw, gap, by, bh = 63, 164, 34, 152, 54
    # bracket over extract..critique
    l = bx + 1 * (bw + gap)
    r = bx + 4 * (bw + gap) + bw
    s += f'<path d="M{l} 140v-7H{r}v7" fill="none" stroke="{p["muted"]}" stroke-width="0.9"/>\n'
    s += txt((l + r) / 2, 126, "CHECKED IN CODE", SANS, 10, p["muted"], anchor="middle", ls="1.6")

    for i, (name, ann) in enumerate(stages):
        x = bx + i * (bw + gap)
        last = (i == len(stages) - 1)
        if last:
            s += hl(x, by, bw, bh, p)
            s += f'<rect x="{x}" y="{by}" width="{bw}" height="{bh}" fill="none" stroke="{p["ox"]}" stroke-width="1.9"/>\n'
            col = p["ox"]
        else:
            s += f'<rect x="{x}" y="{by}" width="{bw}" height="{bh}" fill="{p["boxfill"]}" stroke="{p["ink"]}" stroke-width="1.1"/>\n'
            col = p["ink"]
        s += txt(x + bw / 2, by + 34, name, MONO, 15, col, anchor="middle")
        s += txt(x + bw / 2, 228, ann[0], SERIF, 11.5, p["muted"], anchor="middle", style="italic")
        s += txt(x + bw / 2, 243, ann[1], SERIF, 11.5, p["muted"], anchor="middle", style="italic")
        if not last:
            ax = x + bw + 7
            s += (f'<path d="M{ax} {by + bh/2}H{ax + gap - 15}" stroke="{p["cobalt"]}" '
                  f'stroke-width="1.5" marker-end="url(#ah)"/>\n')

    s += f'<path d="M63 274H1217" stroke="{p["muted"]}" stroke-width="0.7" opacity="0.55"/>\n'
    stats = [("recall", "0.948"), ("precision", "0.865"), ("quotes verbatim", "119 / 119"),
             ("quotes dropped", "0"), ("injections ignored", "4 / 4"), ("cost per room", "&lt; $0.002")]
    colw = (1217 - 63) / 6.0
    for i, (lab, val) in enumerate(stats):
        cx = 63 + colw * i + colw / 2
        s += txt(cx, 300, lab.upper(), SANS, 9.5, p["muted"], anchor="middle", ls="1.3")
        s += txt(cx, 326, val, MONO, 19, p["ink"], anchor="middle")

    s += txt(64, 352, "Fig. 2. Ten synthetic discovery calls with planted traps. Numbers from the committed "
                      "eval run, replayed by content hash so CI needs no API key.",
             SERIF, 12.5, p["muted"], style="italic")
    s += '</svg>\n'
    return s


# ---------------------------------------------------------------- FIG 3
def fig3(p):
    W, H = 1280, 420
    s = head(W, H, p)
    # hatch patterns
    hs = ''
    specs = [("hA", p["ox"], "M0 8 L8 0"), ("hB", p["cobalt"], "M0 0 L8 8"), ("hC", p["ink"], "M4 0 L4 8")]
    for pid, col, d in specs:
        hs += (f'<pattern id="{pid}" width="8" height="8" patternUnits="userSpaceOnUse">'
               f'<path d="{d}" stroke="{col}" stroke-width="1" opacity="{p["hatchop"]}"/></pattern>')
    s = s.replace('<marker id="ah"', hs + '\n<marker id="ah"')
    s += frame(W, H, p)
    s += hdr(W, p, 3, "priyanshu.fyi")

    sets = [(420, 180, "hA", p["ox"]), (560, 180, "hB", p["cobalt"]), (490, 272, "hC", p["ink"])]
    for (cx, cy, pid, col) in sets:
        s += f'<circle cx="{cx}" cy="{cy}" r="100" fill="url(#{pid})"/>\n'
    for (cx, cy, pid, col) in sets:
        s += f'<circle cx="{cx}" cy="{cy}" r="100" fill="none" stroke="{col}" stroke-width="1.4"/>\n'

    s += txt(366, 130, "Build", SERIF, 17, p["ink"], anchor="middle")
    s += txt(614, 130, "Deploy", SERIF, 17, p["ink"], anchor="middle")
    s += txt(490, 350, "Discover", SERIF, 17, p["ink"], anchor="middle")
    clips = ('<clipPath id="c1"><circle cx="420" cy="180" r="100"/></clipPath>'
             '<clipPath id="c2" clip-path="url(#c1)"><circle cx="560" cy="180" r="100"/></clipPath>'
             '<clipPath id="c3" clip-path="url(#c2)"><circle cx="490" cy="272" r="100"/></clipPath>')
    s = s.replace('<marker id="ah"', clips + '\n<marker id="ah"')
    s += (f'<rect x="380" y="140" width="220" height="180" fill="{p["hl"]}" '
          f'opacity="0.92" clip-path="url(#c3)"/>\n')
    s += txt(490, 212, "FDE", MONO, 13, p["hltext"], anchor="middle")

    rows = [(112, "hA", p["ox"], "Build",
             "TypeScript, Python, NestJS, FastAPI, React, Next.js,", "Postgres, Mongo, LangGraph, RAG, evals"),
            (182, "hB", p["cobalt"], "Deploy",
             "Docker, AWS, Azure, CI/CD, edge inference, RTSP", "pipelines, pilots that actually ran"),
            (252, "hC", p["ink"], "Discover",
             "50+ enterprise AI opportunities across 7 countries,", "RFPs, PoCs, pilot to scale")]
    for (y, pid, col, name, d1, d2) in rows:
        s += f'<rect x="720" y="{y-17}" width="24" height="24" fill="url(#{pid})" stroke="{col}" stroke-width="1"/>\n'
        s += txt(758, y, name, SANS, 14.5, p["ink"], weight="700")
        s += txt(758, y + 20, d1, SANS, 12, p["muted"])
        s += txt(758, y + 37, d2, SANS, 12, p["muted"])

    s += f'<path d="M720 300H1216" stroke="{p["muted"]}" stroke-width="0.7" opacity="0.55"/>\n'
    s += txt(720, 332, "The overlap is the job.", SERIF, 18, p["ink"], style="italic")
    s += txt(720, 356, "Most people pick one circle. The problems worth solving sit where all three meet.",
             SANS, 12, p["muted"])
    s += '</svg>\n'
    return s


for name, fn in [("fig-1-hero", fig1), ("fig-2-signalroom", fig2), ("fig-3-tracks", fig3)]:
    for pal in (SHEET, BOARD):
        suffix = "" if pal["key"] == "sheet" else "-dark"
        path = os.path.join(OUT, f"{name}{suffix}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(fn(pal))
        print(path)
