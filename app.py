import streamlit as st
import base64

import streamlit as st

st.markdown("""
<style>

/* Hide top toolbar (Share, GitHub, menu) */
[data-testid="stToolbar"] {
    display: none;
}

/* Hide main menu */
#MainMenu {
    visibility: hidden;
}

/* Hide footer (Hosted with Streamlit) */
footer {
    visibility: hidden;
}

/* Hide header */
header {
    visibility: hidden;
}

/* Remove top padding */
.block-container {
    padding-top: 1rem;
}

</style>
""", unsafe_allow_html=True)


# CONFIG

st.set_page_config(
    page_title="Karyar | Campus Freelancing",
    page_icon="🧩",
    layout="wide"
)


# LOGO -> base64

def img_to_base64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = img_to_base64("karyar_logo.png")


# GOOGLE FORM LINKS

FREELANCER_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfTKSFW8--8xgRFAB1C6pUNpzcoRAgPN7cqILa_PE_8fDc9Tw/viewform?usp=publish-editor"
USER_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSciohUmTNvbhliPvePCd4M_1unGne3JlsxSJ64oUPFOd60lEA/viewform?usp=publish-editor"

# COLORS
# Background stays near-black.
# Logo: Midnight green

DARK_GREEN = "#642F37"      # Puce Red
MOSS_GREEN = "#B6B0B8"      # Pastel Purple
BEIGE = "#F7C767"           # Orange-Yellow (Crayola)
ROSY_BROWN = "#F9904D"      # Royal Orange
MIDNIGHT_GREEN = "#C03A0F"  # Rust (logo color)

#background
BG = "#06060a"

# Soft beige UI tints
BEIGE_SOFT = "rgba(247,199,103,0.10)"
BEIGE_BORDER = "rgba(247,199,103,0.22)"

# Accent used where CORAL was used earlier (headline + button gradient)
ACCENT = MIDNIGHT_GREEN


# CSS

st.markdown(
    f"""
<style>
html, body, [class*="css"] {{
  font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
}}

.stApp {{
  background:
    radial-gradient(1100px 650px at 50% -12%, rgba(192,58,15,0.16), transparent 58%),
    radial-gradient(900px 600px at 12% 22%, rgba(100,47,55,0.22), transparent 62%),
    linear-gradient(180deg, {BG} 0%, #07070a 55%, {BG} 100%);
  color: #f3f3f3;
}}

.block-container {{
  max-width: 1120px;
  padding-top: 0.9rem !important;
  padding-bottom: 2.1rem !important;
}}

/* HERO */
.hero {{
  text-align: center;
  padding: 6px 10px 8px 10px;
}}

.logo-img {{
  width: 46%;
  max-width: 620px;
  margin: 0 auto 2px auto;  /* VERY tight gap */
  display: block;
  filter: drop-shadow(0px 14px 34px rgba(0,0,0,0.55));
}}

.logo-tagline {{
  font-size: 22px;
  font-weight: 500;
  color: rgba(246,240,228,0.86);
  margin: 0px 0 14px 0;     /* RIGHT BELOW logo */
  line-height: 1.2;
}}

.hero-title {{
  font-size: 40px;
  line-height: 1.08;
  font-weight: 820;
  margin: 0 0 10px 0;
  color: {ROSY_BROWN};
}}

.hero-subtitle {{
  font-size: 16.5px;
  color: rgba(246,240,228,0.74);
  margin: 0 auto;
  max-width: 860px;
}}

/* Pills */
.pill-row {{
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  margin-top: 16px;
}}

.pill {{
  padding: 8px 12px;
  border-radius: 999px;
  border: 1px solid rgba(182,176,184,0.22);
  background: rgba(0,0,0,0.25);
  color: rgba(246,240,228,0.78);
  font-size: 13px;
}}

.soft-divider {{
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(182,176,184,0.16), transparent);
  margin: 20px 0 18px 0;
}}

/* Beige premium wrapper (SUBTLE, CLEAN) */
.beige-wrap {{
  margin-top: 8px;
  margin-bottom: 28px;  /* <-- ADDED SPACE BETWEEN BEIGE BOX AND FEATURE CARDS */
  padding: 22px 18px;
  border-radius: 18px;
  background:
    radial-gradient(700px 240px at 50% 0%, rgba(247,199,103,0.16), transparent 60%),
    {BEIGE_SOFT};
  border: 1px solid {BEIGE_BORDER};
  box-shadow: 0 18px 54px rgba(0,0,0,0.33);
}}

.section-title {{
  font-size: 22px;
  font-weight: 780;
  color: rgba(246,240,228,0.92);
  margin: 2px 0 6px 0;
}}

.section-note {{
  color: rgba(246,240,228,0.70);
  margin: 0 0 18px 0;
  font-size: 14.5px;
}}

/* Feature Cards */
.card {{
  background: rgba(100,47,55,0.20);
  border: 1px solid rgba(192,58,15,0.18);
  border-radius: 16px;
  padding: 18px 18px 16px 18px;
  box-shadow: 0 16px 46px rgba(0,0,0,0.35);
  backdrop-filter: blur(8px);
  transition: transform 0.18s ease, border-color 0.18s ease;
  height: 100%;
}}

.card:hover {{
  transform: translateY(-3px);
  border-color: rgba(247,199,103,0.34);
}}

.card-title {{
  font-size: 16px;
  font-weight: 760;
  color: rgba(246,240,228,0.92);
  margin-bottom: 6px;
}}

.card-text {{
  font-size: 14px;
  color: rgba(246,240,228,0.74);
  margin: 0;
}}

/* Adds vertical spacing between the 2 rows of cards */
.row-gap {{
  height: 32px;  /* increased from 18px */
}}

/* CTA panel */
.cta-wrap {{
  margin-top: 22px;
  padding: 22px 18px;
  border-radius: 18px;
  background:
    radial-gradient(760px 260px at 50% 0%, rgba(192,58,15,0.18), transparent 60%),
    rgba(100,47,55,0.26);
  border: 1px solid rgba(182,176,184,0.16);
  box-shadow: 0 18px 54px rgba(0,0,0,0.38);
  text-align: center;
}}

.cta-title {{
  font-size: 18px;
  font-weight: 820;
  color: rgba(246,240,228,0.92);
  margin-bottom: 6px;
}}

.cta-sub {{
  font-size: 14px;
  color: rgba(246,240,228,0.72);
  margin-bottom: 16px;
}}

.btn-row {{
  display: flex;
  gap: 14px;
  justify-content: center;
  flex-wrap: wrap;
}}

.btn-primary, .btn-secondary {{
  display: inline-block;
  text-decoration: none !important;
  padding: 12px 18px;
  border-radius: 12px;
  font-weight: 760;
  transition: transform 0.18s ease, box-shadow 0.18s ease, background 0.18s ease;
  min-width: 220px;
}}

.btn-primary {{
  color: #0b0f12 !important;
  background: linear-gradient(135deg, {ACCENT} 0%, {ROSY_BROWN} 55%, {BEIGE} 100%);
  box-shadow: 0 12px 30px rgba(192,58,15,0.22);
}}

.btn-primary:hover {{
  transform: translateY(-2px);
  box-shadow: 0 16px 44px rgba(192,58,15,0.34);
}}

.btn-secondary {{
  color: rgba(246,240,228,0.88) !important;
  background: rgba(0,0,0,0.28);
  border: 1px solid rgba(247,199,103,0.28);
}}

.btn-secondary:hover {{
  transform: translateY(-2px);
  background: rgba(100,47,55,0.22);
}}

/* Footer */
.footer {{
  margin-top: 26px;
  padding: 18px 0 6px 0;
  text-align: center;
  color: rgba(246,240,228,0.55);
  font-size: 13px;
}}
.footer strong {{
  color: rgba(246,240,228,0.80);
}}

/* Tiny premium beige accent line */
.beige-accent {{
  width: 90px;
  height: 3px;
  border-radius: 99px;
  margin: 10px auto 0 auto;
  background: linear-gradient(90deg, transparent, {BEIGE}, transparent);
  opacity: 0.85;
}}
</style>
""",
    unsafe_allow_html=True
)


# HERO

st.markdown(
    f"""
<div class="hero">
  <img class="logo-img" src="data:image/png;base64,{logo_base64}" />
  <div class="logo-tagline">Be Among the First</div>
  <div class="beige-accent"></div>

  <div class="hero-title">Campus Freelancing, Reinvented.</div>
  <div class="hero-subtitle">
    Karyar connects skilled students with real campus opportunities which are fast, fair,
    and built for your ecosystem.
  </div>

  <div class="pill-row">
    <span class="pill">Micro-gigs</span>
    <span class="pill">Student pricing</span>
    <span class="pill">Quick delivery</span>
    <span class="pill">Profiles & skills</span>
    <span class="pill">Trust-first</span>
  </div>
</div>
""",
    unsafe_allow_html=True
)

st.markdown('<div class="soft-divider"></div>', unsafe_allow_html=True)


# FEATURES (beige premium wrap)

st.markdown(
    """
<div class="beige-wrap">
  <div class="section-title">What Karyar will offer</div>
  <div class="section-note">A simple,powerful experience designed for campus life.</div>
</div>
""",
    unsafe_allow_html=True
)

# Cards - Row 1
c1, c2, c3 = st.columns(3, gap="large")  # gap adds horizontal spacing
with c1:
    st.markdown(
        """
<div class="card">
  <div class="card-title">Post gigs in seconds</div>
  <p class="card-text">Create micro-tasks like posters, PPTs, edits, coding help — and get offers quickly.</p>
</div>
""",
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
<div class="card">
  <div class="card-title"> Skill-first discovery</div>
  <p class="card-text">Find freelancers by skills, reviews, and delivery speed — not noise.</p>
</div>
""",
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
<div class="card">
  <div class="card-title"> Student-friendly pricing</div>
  <p class="card-text">Transparent pricing built for campus budgets — with smart suggestions later.</p>
</div>
""",
        unsafe_allow_html=True
    )

# Vertical spacing between rows
st.markdown('<div class="row-gap"></div>', unsafe_allow_html=True)

# Cards - Row 2
c4, c5, c6 = st.columns(3, gap="large")
with c4:
    st.markdown(
        """
<div class="card">
  <div class="card-title">Clear order tracking</div>
  <p class="card-text">Milestones, delivery, revisions — everything stays organized.</p>
</div>
""",
        unsafe_allow_html=True
    )

with c5:
    st.markdown(
        """
<div class="card">
  <div class="card-title">Trust & safety (soon)</div>
  <p class="card-text">Verification + fair dispute handling — designed for student communities.</p>
</div>
""",
        unsafe_allow_html=True
    )

with c6:
    st.markdown(
        """
<div class="card">
  <div class="card-title">Built with feedback</div>
  <p class="card-text">Pre-registering tells us what to build first. Early users shape Karyar.</p>
</div>
""",
        unsafe_allow_html=True
    )


# CTA

st.markdown(
    f"""
<div class="cta-wrap">
  <div class="cta-title">Pre-register for early access</div>
  <div class="cta-sub">Pick your side — offer skills as a freelancer or post gigs as a user.</div>

  <div class="btn-row">
    <a class="btn-primary" href="{FREELANCER_FORM}" target="_blank">Join as Freelancer</a>
    <a class="btn-secondary" href="{USER_FORM}" target="_blank">Register as User</a>
  </div>
</div>
""",
    unsafe_allow_html=True
)


# FOOTER

st.markdown(
    """
<div class="footer">
  <strong>For students.</strong> Made with love by students. 💛
</div>
""",
    unsafe_allow_html=True
)