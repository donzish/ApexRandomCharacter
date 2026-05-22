"""Lightweight CSS for the Streamlit app."""


APP_CSS = """
<style>
    .app-hero {
        padding: 1.4rem 0 1rem;
    }

    .app-kicker {
        color: #38bdf8;
        font-size: .78rem;
        font-weight: 700;
        letter-spacing: .13em;
        text-transform: uppercase;
    }

    .app-hero h1 {
        font-size: 2.7rem;
        line-height: 1.05;
        margin: .35rem 0 .55rem;
    }

    .app-hero p {
        color: #cbd5e1;
        font-size: 1.02rem;
        max-width: 46rem;
    }

    .result-card {
        background: linear-gradient(145deg, #101827 0%, #172033 100%);
        border: 1px solid rgba(148, 163, 184, .24);
        border-radius: 8px;
        padding: 1rem;
        min-height: 8.8rem;
        box-shadow: 0 16px 36px rgba(2, 6, 23, .22);
    }

    .result-card__top {
        align-items: center;
        color: #94a3b8;
        display: flex;
        font-size: .76rem;
        font-weight: 700;
        justify-content: space-between;
        letter-spacing: .09em;
        text-transform: uppercase;
    }

    .result-card__badge {
        background: rgba(15, 23, 42, .82);
        border: 1px solid rgba(148, 163, 184, .24);
        border-radius: 6px;
        color: #e2e8f0;
        font-size: .68rem;
        padding: .2rem .45rem;
    }

    .result-card__value {
        color: #f8fafc;
        font-size: 2rem;
        font-weight: 800;
        line-height: 1.15;
        margin-top: 1rem;
        min-height: 2.5rem;
        overflow-wrap: anywhere;
    }

    .result-card__empty {
        color: #64748b;
        font-weight: 600;
    }

    .weapon-card .result-card__value {
        color: #facc15;
        font-size: 3.2rem;
    }

    .mission-card {
        margin-top: .35rem;
        min-height: 10.5rem;
    }

    .mission-card .result-card__value {
        color: #e2e8f0;
        font-size: 1.08rem;
        line-height: 1.45;
    }

    .section-label {
        color: #cbd5e1;
        font-weight: 700;
        letter-spacing: .02em;
        margin: 1.35rem 0 .45rem;
    }
</style>
"""
