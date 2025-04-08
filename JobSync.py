jobs = [
    # Tanks
    "PLD", "WAR", "DRK", "GNB",

    # Healers
    "WHM", "SCH", "AST", "SGE",

    # Melee DPS
    "MNK", "DRG", "NIN", "SAM", "RPR", "VPR",

    # Physical Ranged DPS
    "BRD", "MCH", "DNC",

    # Magical Ranged DPS
    "BLM", "SMN", "RDM", "PCT"
]

jobs_tali = {
    "PLD": 100, "WAR": 100, "DRK": 100, "GNB": 100,
    "WHM": 80, "SCH": 80, "AST": 100, "SGE": 100,
    "MNK": 72, "DRG": 60, "NIN": 100, "SAM": 70, "RPR": 74, "VPR": 80,
    "BRD": 60, "MCH": 100, "DNC": 100,
    "BLM": 100, "SMN": 80, "RDM": 75, "PCT": 80
}
jobs_koi = {
    "PLD": 100, "WAR": 100, "DRK": 91, "GNB": 86,
    "WHM": 100, "SCH": 100, "AST": 100, "SGE": 100,
    "MNK": 61, "DRG": 63, "NIN": 65, "SAM": 100, "RPR": 100, "VPR": 100,
    "BRD": 100, "MCH": 86, "DNC": 74,
    "BLM": 66, "SMN": 100, "RDM": 59, "PCT": 100
}

job_roles = {
    # Tanks
    "PLD": "Tank", "WAR": "Tank", "DRK": "Tank", "GNB": "Tank",

    # Healers
    "WHM": "Healer", "SCH": "Healer", "AST": "Healer", "SGE": "Healer",

    # Melee DPS
    "MNK": "Melee", "DRG": "Melee", "NIN": "Melee", "SAM": "Melee", "RPR": "Melee", "VPR": "Melee",

    # Physical Ranged DPS
    "BRD": "PhysRanged", "MCH": "PhysRanged", "DNC": "PhysRanged",

    # Magical Ranged DPS
    "BLM": "Caster", "SMN": "Caster", "RDM": "Caster", "PCT": "Caster"
}


def createPairs(jobs, jobsTali, jobsKoi, jobRoles, threshold=5):
    usedTali = set()
    usedKoi = set()
    allCombinations = []

    for jobKoi in jobs:
        levelKoi = jobsKoi.get(jobKoi, 0)
        if levelKoi == 100:
            continue
        roleKoi = jobRoles.get(jobKoi)

        for jobTali in jobs:
            levelTali = jobsTali.get(jobTali, 0)
            if levelTali == 100:
                continue
            roleTali = jobRoles.get(jobTali)

            # Skip same job
            if jobKoi == jobTali:
                continue

            # Determine pairing rank
            if (roleKoi == "Tank" and roleTali == "Healer") or (roleKoi == "Healer" and roleTali == "Tank"):
                rank = 1
            elif (roleKoi == "Melee" and roleTali in ["PhysRanged", "Caster"]) or \
                 (roleTali == "Melee" and roleKoi in ["PhysRanged", "Caster"]):
                rank = 2
            elif roleKoi == "Melee" and roleTali == "Melee":
                rank = 3
            else:
                continue  # Ignore other role combos

            delta = abs(levelKoi - levelTali)
            allCombinations.append((rank, delta, jobKoi, levelKoi, roleKoi, jobTali, levelTali, roleTali))

    # Sort by rank first, then delta
    allCombinations.sort(key=lambda x: (x[0], x[1]))  # Sort by rank, then by level difference

    # Choose best non-overlapping pairs
    finalPairs = []
    for rank, delta, koiJob, koiLvl, koiRole, taliJob, taliLvl, taliRole in allCombinations:
        if koiJob in usedKoi or taliJob in usedTali:
            continue
        usedKoi.add(koiJob)
        usedTali.add(taliJob)
        finalPairs.append((koiJob, koiLvl, koiRole, taliJob, taliLvl, taliRole, delta))

    # Output
    for koiJob, koiLvl, koiRole, taliJob, taliLvl, taliRole, delta in finalPairs:
        print(f"Koi {koiJob} {koiLvl} + Tali {taliJob} {taliLvl}; \nLevel difference of: {delta}\n")


createPairs(jobs, jobs_koi, jobs_tali, job_roles)
