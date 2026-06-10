import streamlit as st
import pandas as pd

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="PBL Knowledge Hub", 
    page_icon="🧠",
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ==========================================
# DATA DICTIONARY (TURNER SYNDROME)
# ==========================================
# Translated directly from your React case file[span_2](start_span)[span_2](end_span)
turner_data = {
    "diagnosis": {
        "title": "Turner Syndrome (45,X) - The Diagnosis",
        "blocks": [
            {
                "type": "alert", 
                "label": "Primary Diagnosis", 
                "text": "Turner Syndrome: a chromosomal disorder in phenotypic females."
            },
            {
                "type": "heading", 
                "text": "How We Reached the Diagnosis"
            },
            {
                "type": "table",
                "headers": ["Clue from Case", "What It Suggests"],
                "rows": [
                    ["Never bled vaginally (primary amenorrhea)", "No estrogen -> no endometrial proliferation"],
                    ["Short stature (4.5 ft)", "GH insensitivity / early epiphyseal fusion"],
                    ["No breast development (Tanner I)", "Estrogen deficiency"],
                    ["Webbed neck", "Classic Turner feature (cystic hygroma remnant)"],
                    ["Widely spaced nipples, broad chest", "Lymphedema in fetal life shields chest growth"],
                    ["Puffed hands, small toes", "Lymphedema"],
                    ["Increased carrying angle (cubitus valgus)", "Classic Turner feature"],
                    ["Excessive nevi", "Common in Turner syndrome"],
                    ["Streaked ovaries on USS", "Gonadal dysgenesis -> no functional follicles"],
                    ["High FSH (68), High LH (35)", "No estrogen -> no negative feedback"],
                    ["Very low estradiol (6.8 pg/ml)", "Non-functional ovaries produce no estrogen"],
                    ["Barr body absent", "Only one X chromosome (no inactivated X)"],
                    ["Married 4 years, no conception", "Infertility due to gonadal dysgenesis"]
                ]
            },
            {
                "type": "box",
                "label": "Mnemonic: Turner's WEBBING",
                "text": "W - Webbed neck\nE - Estrogen deficiency (no puberty, amenorrhea)\nB - Bicuspid aortic valve\nB - Broad chest\nI - Infertility\nN - Nevi\nG - Gonadal dysgenesis (streak ovaries)"
            }
        ]
    },
    "clinical": {
        "title": "Clinical Features Explained",
        "blocks": [
            {"type": "heading", "text": "General Physical Findings"},
            {
                "type": "table",
                "headers": ["Feature", "Mechanism", "Embryological Basis"],
                "rows": [
                    ["Short stature", "SHOX gene haploinsufficiency on X chromosome", "SHOX regulates bone growth"],
                    ["Webbed neck (pterygium colli)", "Remnant of cystic hygroma (lymphatic obstruction)", "Fetal lymphatic failure"],
                    ["Broad/shield chest", "Lymphedema distorts thoracic cage in fetal dev.", "Structural adaptation"],
                    ["Cubitus valgus", "Bone dysplasia due to SHOX haploinsufficiency", "Abnormal endochondral ossification"],
                    ["Puffed hands & small toes", "Peripheral lymphedema", "Often present at birth, resolves/persists"],
                    ["No breast development", "No ovarian estrogen -> no thelarche", "Estrogen required for ductal growth"],
                    ["Excessive nevi", "Unknown; melanocyte proliferation", "More common in 45,X"],
                    ["Streak ovaries", "Oocytes degrade rapidly after birth", "Accelerated atresia due to missing X"]
                ]
            },
            {"type": "heading", "text": "Systemic Associations (Risks to Counsel About)"},
            {
                "type": "list",
                "items": [
                    "🫀 Cardiovascular: Bicuspid aortic valve, coarctation of aorta, aortic dissection",
                    "🩺 Renal: Horseshoe kidney, duplicated collecting system (USS of kidneys needed)",
                    "👂 Hearing: Sensorineural hearing loss",
                    "👁️ Ophthalmic: Strabismus, amblyopia, ptosis",
                    "🦋 Thyroid: Autoimmune hypothyroidism (Hashimoto's) - check TSH annually",
                    "🩸 Metabolic: Insulin resistance, type 2 DM risk",
                    "🦴 Bone: Osteoporosis (low estrogen -> low bone density) hence Calcium/Vit D needed",
                    "🧠 Psychosocial: Normal intelligence but may have visuospatial difficulties"
                ]
            }
        ]
    },
    "labs": {
        "title": "Lab Investigations Interpreted",
        "blocks": [
            {
                "type": "table",
                "headers": ["Test", "Result", "Normal Range", "Interpretation"],
                "rows": [
                    ["Hb", "12.3 g/dL", "12-16 g/dL (F)", "Normal - no anemia"],
                    ["Serum BHCG", "1.8 mIU/L", "<5 mIU/L", "Not pregnant (rules out ectopic)"],
                    ["Serum FSH", "68.28 mIU/L", "3-10 mIU/L", "Very HIGH - confirms ovarian failure"],
                    ["Serum LH", "35.50 mIU/L", "2-15 mIU/L", "HIGH - lack of negative feedback"],
                    ["Serum Estradiol", "6.8 pg/mL", "20-150 pg/mL", "Very LOW - no follicular activity"],
                    ["Serum TSH", "3.1 mIU/L", "0.4-4.0 mIU/L", "Normal (but Turner patients at risk)"],
                    ["Serum Vit D3", "19 ng/mL", "30-100 ng/mL", "Insufficient - needs supplement"],
                    ["Serum Calcium", "9.6 mg/dL", "8.5-10.5 mg/dL", "Normal"],
                    ["FBS", "90 mg/dL", "<100 mg/dL", "Normal (insulin resistance risk later)"],
                    ["Lipid Profile", "Normal", "-", "Good; monitor for cardiovascular risk"]
                ]
            },
            {
                "type": "alert",
                "label": "Key Pattern to Recognize",
                "text": "HIGH FSH + HIGH LH + VERY LOW Estradiol = Hypergonadotropic Hypogonadism"
            },
            {
                "type": "box",
                "label": "Ultrasound Findings",
                "text": "Streak ovaries: Fibrous tissue remnants -> no follicles, no estrogen."
            }
        ]
    },
    "pathophysiology": {
        "title": "Pathophysiology - Why It All Happens",
        "blocks": [
            {"type": "heading", "text": "The Core Problem: 45, X Karyotype"},
            {
                "type": "flow",
                "steps": [
                    "Monosomy X (45,X) -> usually due to non-disjunction in paternal meiosis",
                    "SHOX gene haploinsufficiency -> short stature, cubitus valgus",
                    "Two X chromosomes needed for oocyte survival -> accelerated oocyte atresia",
                    "By puberty: streak ovaries (only fibrous stroma remains) -> no estrogen",
                    "No estrogen -> No puberty (no thelarche, no menarche, Tanner I)",
                    "No estrogen -> No negative feedback on HPG axis -> FSH & LH rise markedly",
                    "High FSH + High LH + Low Estrogen = Hypergonadotropic Hypogonadism",
                    "No endometrial proliferation -> Primary amenorrhea (never bled)",
                    "No ovulation -> Infertility (4 years of failed conception)"
                ]
            },
            {"type": "heading", "text": "HPG Axis in Turner Syndrome vs Normal"},
            {
                "type": "table",
                "headers": ["Step", "Normal Female", "Turner Syndrome"],
                "rows": [
                    ["Hypothalamus", "GnRH pulsatile release", "GnRH pulsatile release (normal)"],
                    ["Pituitary", "FSH & LH release", "FSH & LH release (elevated -> no feedback)"],
                    ["Ovary", "Follicle development + Estradiol", "Streak ovary -> NO response"],
                    ["Feedback", "Estradiol negative feedback", "NO estradiol -> NO negative feedback"],
                    ["Uterus/Endometrium", "Proliferates under estrogen", "Atrophic (2mm thick)"],
                    ["Result", "Menarche, ovulation, fertility", "Primary amenorrhea, anovulation"]
                ]
            },
            {
                "type": "box",
                "label": "Why is the uterus present?",
                "text": "In normal male development, testes produce Müllerian Inhibiting Substance (AMH) to degenerate the uterus. In Turner's, there are no testes and no AMH, so the Müllerian ducts develop into a normal (though hypoplastic due to lack of estrogen) uterus and vagina."
            }
        ]
    },
    "barr": {
        "title": "Barr Body Genetics & Significance",
        "blocks": [
            {"type": "heading", "text": "What is a Barr Body?"},
            {"type": "alert", "label": "Definition", "text": "A Barr body (sex chromatin body) is the inactivated, condensed X chromosome visible at the periphery of the nucleus."},
            {"type": "heading", "text": "Lyon Hypothesis (X-Inactivation)"},
            {
                "type": "list",
                "items": [
                    "In every cell with more than one X chromosome, all extra X chromosomes are inactivated.",
                    "Inactivation is random (either maternal or paternal X).",
                    "Inactivation occurs early in embryonic development (~16-cell stage).",
                    "Formula: Number of Barr bodies = Number of X chromosomes - 1."
                ]
            },
            {
                "type": "table",
                "headers": ["Karyotype", "Barr Bodies", "Example"],
                "rows": [
                    ["46, XX", "1", "Normal Female"],
                    ["46, XY", "0", "Normal Male"],
                    ["45, X", "0", "Turner Syndrome (ABSENT)"],
                    ["47, XXY", "1", "Klinefelter Syndrome"],
                    ["47, XXX", "2", "Triple X Syndrome"]
                ]
            },
            {"type": "box", "label": "How the Test is Done", "text": "1. Scrape buccal mucosa (inner cheek)\n2. Smear on glass slide\n3. Stain and observe under microscope."}
        ]
    },
    "hrt": {
        "title": "HRT Rationale & Treatment Explained",
        "blocks": [
            {"type": "heading", "text": "Goals of HRT in Turner Syndrome"},
            {
                "type": "list",
                "items": [
                    "Induce puberty & secondary sexual characteristics (breast development).",
                    "Establish withdrawal bleeds (menstrual cycles) for psychological well-being.",
                    "Protect bone density (prevent osteoporosis).",
                    "Cardiovascular protection.",
                    "NOT for fertility (streak ovaries cannot produce eggs - must be counselled)."
                ]
            },
            {"type": "heading", "text": "Prescribed Regimen Explained"},
            {
                "type": "table",
                "headers": ["Drug", "Dose/Route", "Role", "Why This Dose/Timing"],
                "rows": [
                    ["Ethinyl Estradiol", "0.3mg/day oral", "Estrogen replacement", "Start LOW dose to mimic natural puberty onset."],
                    ["Medroxyprogesterone", "10mg (days 13-21)", "Protects endometrium", "Unopposed estrogen causes endometrial hyperplasia/cancer risk."],
                    ["Calcium + Vitamin D", "Oral supplements", "Bone protection", "Estrogen deficiency + Vit D deficiency = High fracture risk."]
                ]
            },
            {
                "type": "alert",
                "label": "Why Sequential and Not Continuous?",
                "text": "Sequential HRT (Estrogen every day + Progestogen only for part of the month) induces cyclical shedding of the endometrium, mimicking a normal menstrual period. Continuous would cause amenorrhea or unpredictable spotting."
            }
        ]
    },
    "ethics": {
        "title": "Medical Ethics, Confidentiality & Counselling",
        "blocks": [
            {"type": "heading", "text": "Issue 1: Confidentiality"},
            {"type": "alert", "label": "Patient's Request", "text": "\"She requested not to reveal her problem to anyone.\""},
            {
                "type": "list",
                "items": [
                    "Confidentiality is a cornerstone of the doctor-patient relationship.",
                    "The patient has the full right to control her own health information.",
                    "Ethical tension: Patient confidentiality vs. spouse's right to know regarding infertility.",
                    "Resolution: Do not breach confidentiality. Discuss with the patient WHY disclosure to the husband is important and encourage/support her to tell him."
                ]
            },
            {"type": "heading", "text": "Issue 2: Counselling Points"},
            {
                "type": "list",
                "items": [
                    "Infertility: Explain clearly that streak ovaries cannot produce eggs.",
                    "Options: Adoption, surrogacy with donor egg (depending on religious/legal context).",
                    "Psychosocial: Acknowledge stigma of infertility in cultural context.",
                    "HRT: Manage expectations—will restore periods and puberty, but NOT fertility."
                ]
            },
            {
                "type": "box",
                "label": "Rural & Sociocultural Context (CHS Angle)",
                "text": "The case is set in rural Sindh. Dais (traditional birth attendants) often lack scientific medical knowledge and may blame the woman or use harmful remedies. The social pressure for a male heir exacerbates marital distress."
            }
        ]
    },
    "viva": {
        "title": "Viva Q&A Exam Preparation",
        "blocks": [
            {"type": "heading", "text": "High-Yield Viva Questions"},
            {
                "type": "qa",
                "items": [
                    {"q": "What is the diagnosis in this case? Give reasons.", "a": "Turner Syndrome (45,X). Evidence: Primary amenorrhea, short stature, webbed neck, elevated FSH/LH, very low estrogen, absent Barr body."},
                    {"q": "Why are FSH and LH elevated?", "a": "Due to streak ovaries producing no estrogen, resulting in a loss of negative feedback on the hypothalamus and anterior pituitary."},
                    {"q": "What is a Barr body?", "a": "An inactivated, condensed X chromosome. Normal females have 1, Turner females (45,X) have 0."},
                    {"q": "Why is the uterus present?", "a": "Uterus is a Müllerian structure. It regresses only if Anti-Müllerian Hormone (AMH) is present. AMH is produced by testes, which are absent in Turner syndrome."},
                    {"q": "Why is progesterone added to the HRT?", "a": "To prevent endometrial hyperplasia and carcinoma caused by unopposed estrogen therapy."},
                    {"q": "What are the cardiovascular risks in Turner syndrome?", "a": "Bicuspid aortic valve (most common) and coarctation of the aorta."}
                ]
            }
        ]
    }
}


# ==========================================
# DYNAMIC RENDERING ENGINE
# ==========================================
def render_blocks(blocks):
    """Parses the JSON-like block array and renders Streamlit components."""
    for block in blocks:
        if block["type"] == "heading":
            st.markdown(f"#### {block['text']}")
            st.divider()
            
        elif block["type"] == "alert":
            st.error(f"**{block['label']}**\n\n{block['text']}")
            
        elif block["type"] == "box":
            st.info(f"**{block['label']}**\n\n{block['text']}")
            
        elif block["type"] == "list":
            for item in block["items"]:
                st.markdown(f"- {item}")
            st.markdown("<br>", unsafe_allow_html=True)
            
        elif block["type"] == "table":
            df = pd.DataFrame(block["rows"], columns=block["headers"])
            st.table(df)
            
        elif block["type"] == "flow":
            st.markdown("##### Disease Progression Flow")
            for i, step in enumerate(block["steps"]):
                st.markdown(f"**{i+1}.** {step}")
                if i < len(block["steps"]) - 1:
                    st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;⬇")
            st.markdown("<br>", unsafe_allow_html=True)
            
        elif block["type"] == "qa":
            for item in block["items"]:
                with st.expander(f"🗣️ **Q:** {item['q']}"):
                    st.success(f"**A:** {item['a']}")

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2966/2966327.png", width=60) # Placeholder medical logo
st.sidebar.title("📚 PBL Modules")
st.sidebar.caption("Ziauddin University | MBBS Knowledge Hub")

module = st.sidebar.selectbox("Select Module", ["Musculoskeletal (MSK)", "Urinary", "Reproductive"])
st.sidebar.divider()

# ==========================================
# MAIN APPLICATION ROUTING
# ==========================================

# --- MSK MODULE ---
if module == "Musculoskeletal (MSK)":
    st.title("🦴 Musculoskeletal Module")
    msk_cases = [f"MSK PBL {i}: Case Title" for i in range(1, 9)]
    selected_pbl = st.sidebar.radio("Select MSK Case:", msk_cases)
    
    st.subheader(selected_pbl)
    st.warning("Data for this case is pending upload. Use the `turner_data` dictionary structure to map this case.")

# --- URINARY MODULE ---
elif module == "Urinary":
    st.title("💧 Urinary Module")
    uro_cases = [f"Urinary PBL {i}: Case Title" for i in range(1, 5)]
    selected_pbl = st.sidebar.radio("Select Urinary Case:", uro_cases)
    
    st.subheader(selected_pbl)
    st.warning("Data for this case is pending upload. Use the `turner_data` dictionary structure to map this case.")

# --- REPRODUCTIVE MODULE ---
elif module == "Reproductive":
    st.title("🧬 Reproductive Module")
    repro_cases = ["PBL 1: Turner Syndrome", "PBL 2: AUB + Endometriosis"]
    selected_pbl = st.sidebar.radio("Select Reproductive Case:", repro_cases)
    
    # -------------------------------------
    # PBL 1: TURNER SYNDROME (FULLY MAPPED)
    # -------------------------------------
    if selected_pbl == "PBL 1: Turner Syndrome":
        st.caption("PBL-1 | Disturbed Married Life")
        st.subheader("Turner Syndrome (45,X) - Complete Study Guide")
        
        # Create Navigation Tabs matching the React architecture
        tabs = st.tabs([
            "🩺 Diagnosis", 
            "📋 Clinical", 
            "🧪 Labs", 
            "⚙️ Pathophys", 
            "🧬 Barr Body", 
            "💊 HRT", 
            "⚖️ Ethics", 
            "🗣️ Viva"
        ])
        
        # Map Tabs to Data Dictionaries
        with tabs[0]: render_blocks(turner_data["diagnosis"]["blocks"])
        with tabs[1]: render_blocks(turner_data["clinical"]["blocks"])
        with tabs[2]: render_blocks(turner_data["labs"]["blocks"])
        with tabs[3]: render_blocks(turner_data["pathophysiology"]["blocks"])
        with tabs[4]: render_blocks(turner_data["barr"]["blocks"])
        with tabs[5]: render_blocks(turner_data["hrt"]["blocks"])
        with tabs[6]: render_blocks(turner_data["ethics"]["blocks"])
        with tabs[7]: render_blocks(turner_data["viva"]["blocks"])

    # -------------------------------------
    # PBL 2: AUB & ENDOMETRIOSIS
    # -------------------------------------
    elif selected_pbl == "PBL 2: AUB + Endometriosis":
        st.caption("PBL-2 | Pelvic Pain and Bleeding")
        st.subheader("Abnormal Uterine Bleeding & Endometriosis")
        st.warning("Data for this case is pending upload. Build out the `aub_data` dictionary and pass it to the `render_blocks` function here.")
