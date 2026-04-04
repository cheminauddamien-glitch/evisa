#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Repair script to undo substring damage from erroneous replacements.
Reverses: "or"->"ou", "and"->"et", "for"->"pour", "first"->"d'abord",
"open a"->"ouvrez un", "Best option for"->"Meilleure option pour" etc.
inside English words where they should not have been changed.
"""
import os
import re
import glob

FR_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www", "fr")
PATTERN = os.path.join(FR_DIR, "expat-guide-*.html")

# Words corrupted by "or" -> "ou"
OR_FIXES = [
    # Fix longest first to avoid double-fixing
    ("foueigners", "foreigners"),
    ("Foueigners", "Foreigners"),
    ("foueigner", "foreigner"),
    ("Foueigner", "Foreigner"),
    ("foueign", "foreign"),
    ("Foueign", "Foreign"),
    ("FOUEIGN", "FOREIGN"),
    ("infoumat", "informat"),
    ("Infoumat", "Informat"),
    ("woukers", "workers"),
    ("wouker", "worker"),
    ("Wouker", "Worker"),
    ("wouking", "working"),
    ("wouk", "work"),
    ("Wouk", "Work"),
    ("WOUK", "WORK"),
    ("netwouk", "network"),
    ("Netwouk", "Network"),
    ("wouldwide", "worldwide"),
    ("Wouldwide", "Worldwide"),
    ("wouth", "worth"),
    ("Wouth", "Worth"),
    ("majou", "major"),
    ("Majou", "Major"),
    ("factou", "factor"),
    ("authouities", "authorities"),
    ("authouity", "authority"),
    ("Authouity", "Authority"),
    ("histouically", "historically"),
    ("histouical", "historical"),
    ("categouy", "category"),
    ("Categouy", "Category"),
    ("oudinary", "ordinary"),
    ("Oudinary", "Ordinary"),
    ("impoutant", "important"),
    ("Impoutant", "Important"),
    ("theouetically", "theoretically"),
    ("stouage", "storage"),
    ("mouning", "morning"),
    ("platfoums", "platforms"),
    ("platfoum", "platform"),
    ("Platfoum", "Platform"),
    ("Tempouary", "Temporary"),
    ("tempouary", "temporary"),
    ("neighbouhoods", "neighbourhoods"),
    ("neighbouhood", "neighbourhood"),
    ("territouial", "territorial"),
    ("Territouial", "Territorial"),
    ("foutement", "fortement"),
    ("Foutement", "Fortement"),
    ("moue ", "more "),
    ("Moue ", "More "),
    ("befou ", "before "),
    ("befoue", "before"),
    ("Befou ", "Before "),
    ("poutuguese", "portuguese"),
    ("Poutuguese", "Portuguese"),
    ("suppout", "support"),
    ("Suppout", "Support"),
    ("oppoutunit", "opportunit"),
    ("Oppoutunit", "Opportunit"),
    ("repout", "report"),
    ("Repout", "Report"),
    ("transfou", "transfor"),
    ("Transfou", "Transfor"),
    ("comfout", "comfort"),
    ("Comfout", "Comfort"),
    ("affoudable", "affordable"),
    ("favouable", "favorable"),
    ("favou", "favour"),
    ("Favou", "Favour"),
    ("commou", "common"),
    ("flou ", "floor "),
    ("Flou ", "Floor "),
    ("modou", "moderate"),
    ("doctous", "doctors"),
    ("doctou", "doctor"),
    ("Doctou", "Doctor"),
    ("regulatou", "regulator"),
    ("senatou", "senator"),
    ("investou", "investor"),
    ("administrat", "administrat"),
    ("colou", "colour"),
    ("Colou", "Colour"),
    # Fix remaining "ou" that should be "or" in English context
    (" ou ", " or "),  # standalone "or" -> "ou" -- only fix between spaces
    (" ou,", " or,"),
    (" ou.", " or."),
    (" ou)", " or)"),
    ("(ou ", "(or "),
    ("/ou ", "/or "),
    (" ou/", " or/"),
    # Fix "for" -> "fou" issues
    ("fou ", "for "),
    ("Fou ", "For "),
    (" fou,", " for,"),
    (" fou.", " for."),
    (" fou;", " for;"),
    (" fou:", " for:"),
]

# Words corrupted by "and" -> "et"
AND_FIXES = [
    ("Leting", "Landing"),
    ("leting", "landing"),
    ("Letguage", "Language"),
    ("letguage", "language"),
    ("underfunded et understaffed", "underfunded and understaffed"),
    ("understeted", "understaffed"),
    ("outstetig", "outstanding"),
    ("stetard", "standard"),
    ("Stetard", "Standard"),
    ("demetig", "demanding"),
    ("metigatory", "mandatory"),
    ("commeting", "commanding"),
    ("metet", "mandat"),
    ("Metet", "Mandat"),
    ("Geougia", "Georgia"),
    ("geougia", "georgia"),
    # "and" -> "et" inside words - harder to fix generically
    # Fix "Land" that became "Let" (but only at word boundaries)
]

def fix_or_damage(text):
    """Fix damage from 'or' -> 'ou' substring replacement."""
    result = text
    for wrong, right in OR_FIXES:
        if wrong in result:
            result = result.replace(wrong, right)
    return result

def fix_and_damage(text):
    """Fix damage from 'and' -> 'et' substring replacement."""
    result = text
    for wrong, right in AND_FIXES:
        if wrong in result:
            result = result.replace(wrong, right)
    # Fix "Land" -> "Let" (at word boundary)
    result = re.sub(r'\bLet Management\b', 'Land Management', result)
    result = re.sub(r'\bLet Department\b', 'Land Department', result)
    result = re.sub(r'\bLet Registry\b', 'Land Registry', result)
    result = re.sub(r'\blet registry\b', 'land registry', result)
    return result

def fix_first_damage(text):
    """Fix damage from 'first' -> 'd'abord' substring replacement."""
    result = text
    result = result.replace("the d'abord", "the first")
    result = result.replace("The d'abord", "The first")
    result = result.replace("d'abord 50m", "first 50m")
    result = result.replace("d'abord months", "first months")
    result = result.replace("d'abord year", "first year")
    result = result.replace("d'abord 50", "first 50")
    result = result.replace("d'abord months", "first months")
    # "within the first" patterns
    result = result.replace("within the d'abord", "within the first")
    return result

def fix_open_a_damage(text):
    """Fix damage from 'open a' -> 'ouvrez un' substring replacement inside words."""
    result = text
    # "ouvrez unn" from "open an"
    result = result.replace("ouvrez unn ", "open an ")
    result = result.replace("Ouvrez unn ", "Open an ")
    return result

def process_file(filepath):
    fname = os.path.basename(filepath)
    print(f"Repairing: {fname}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    content = fix_or_damage(content)
    content = fix_and_damage(content)
    content = fix_first_damage(content)
    content = fix_open_a_damage(content)

    # Additional specific fixes
    # "recommet" from recommend -> "et" replacing "and"
    content = content.replace("recommeted", "recommended")
    content = content.replace("Recommeted", "Recommended")
    content = content.replace("recommetée", "recommandée")
    content = content.replace("recommetation", "recommendation")

    changes = 0
    if content != original:
        changes = sum(1 for a, b in zip(content, original) if a != b)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    print(f"  -> {'Fixed' if changes > 0 else 'No changes needed'}")
    return 1 if changes > 0 else 0

def main():
    files = sorted(glob.glob(PATTERN))
    print(f"Repairing {len(files)} files...")
    total = 0
    for f in files:
        total += process_file(f)
    print(f"\nDone. {total} files repaired.")

if __name__ == '__main__':
    main()
