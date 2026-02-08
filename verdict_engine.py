def generate_verdict(margin, ltv, cac, elasticity):
    decisions = []

    if margin < 0.3:
        decisions.append("Increase price or reduce costs")

    if ltv > 3 * cac:
        decisions.append("Scale advertising")

    if elasticity < -1:
        decisions.append("Do not increase price")

    if margin > 0.5 and ltv > 3 * cac:
        decisions.append("Launch bundles or upsells")

    if not decisions:
        decisions.append("Maintain current strategy")

    return decisions
