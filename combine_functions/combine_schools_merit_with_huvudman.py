import re
import pandas as pd

ELEVER_PATH  = "data_files/Grundskola - Antal elever per årskurs 2025 Skolnivå.csv"
MERITER_PATH = "data_files/skolor_meriter_complete.csv"
OUTPUT_PATH  = "data_files/skolor_meriter_complete.csv"

df_elever = pd.read_csv(
    ELEVER_PATH, sep=";", skiprows=5, encoding="utf-8-sig"
)
df_meriter = pd.read_csv(
    MERITER_PATH, sep=";", encoding="utf-8-sig"
)

sthlm = df_elever[df_elever["Skolkommun"] == "Stockholm"][
    ["Skola", "Typ av huvudman", "Elever, årskurs 1-9"]
].copy()
sthlm["Skola_upper"] = sthlm["Skola"].str.upper().str.strip()

typ_lookup   = dict(zip(sthlm["Skola_upper"], sthlm["Typ av huvudman"]))
antal_lookup = dict(zip(sthlm["Skola_upper"], sthlm["Elever, årskurs 1-9"]))

def rensa_namn(namn: str) -> str:
    """Tar bort skolstadiesuffix som ', F–9' eller ', 4–9' från slutet."""
    namn = re.sub(r",\s*(?:F|f)?[–\-]?\d+[–\-]\d+\s*$", "", str(namn)).strip()
    namn = re.sub(r",\s*F[–\-]\d+\s*$", "", namn).strip()
    return namn

df_meriter["_namn_upper"] = df_meriter["namn"].apply(rensa_namn).str.upper()

MANUAL_MAP = {
    "BROMMA ENSKILDA SKOLA":                  "BROMMA ENSKILDA SKOLA EK.FÖREN.",
    "INTERNATIONELLA ENGELSKA SKOLAN BROMMA": "INTERNATIONELLA ENGELSKA SKOLAN BROMMA",
    "INTERNATIONELLA ENGELSKA SKOLAN LILJEHOLMEN": "INTERNATIONELLA ENGELSKA SKOLAN LILJEHOLMEN",
    "INTERNATIONELLA ENGELSKA SKOLAN ÄLVSJÖ": "INTERNATIONELLA ENGELSKA SKOLAN ÄLVSJÖ",
    "KRISTOFFERSKOLAN":                       "KRISTOFFERSKOLAN, GR",
    "KUNSKAPSSKOLANS RESURSSKOLA HÄGERSTEN":  "KUNSKAPSSKOLANS RESURSSKOLA",
    "MAGELUNGENS GRUNDSKOLA LÅNGBROPARK":     "MAGELUNGENS GRUNDSKOLA LÅNGBROPARK",
    "MAGELUNGENS GRUNDSKOLA ÄLVSJÖ":          "MAGELUNGENS GRUNDSKOLA ÄLVSJÖ",
    "RAOUL WALLENBERGSKOLAN":                 "RAOUL WALLENBERGSKOLAN BROMMA",
    "SNITZ GRUNDSKOLA":                       "SNITZ GRUNDSKOLA",
    "THEA PRIVATA GRUNDSKOLA – BROMMA":       "TELLUSSKOLAN THEA BROMMA",
}

df_meriter["Typ av huvudman"]        = df_meriter["_namn_upper"].map(typ_lookup)
df_meriter["Antal_elever_skolverket"] = df_meriter["_namn_upper"].map(antal_lookup)

for meriter_key, elever_key in MANUAL_MAP.items():
    mask = (df_meriter["_namn_upper"] == meriter_key) & df_meriter["Typ av huvudman"].isna()
    if mask.any() and elever_key in typ_lookup:
        df_meriter.loc[mask, "Typ av huvudman"]        = typ_lookup[elever_key]
        df_meriter.loc[mask, "Antal_elever_skolverket"] = antal_lookup.get(elever_key)

df_meriter = df_meriter.drop(columns=["_namn_upper"])
df_meriter.to_csv(OUTPUT_PATH, sep=";", index=False)

grundskolor = df_meriter[df_meriter["kategori"] == "grundskolor"]
matchade    = grundskolor["Typ av huvudman"].notna().sum()
totalt      = len(grundskolor)

print(f"  Totalt rader : {len(df_meriter)}")
print(f"  Grundskolor  : {totalt}  |  matchade: {matchade}  |  omatchade: {totalt - matchade}")
print()
print("Förhandsgranskning grundskolor:")
print(
    grundskolor[["namn", "Typ av huvudman", "Elever, årskurs 1-9", "Antal_elever_skolverket"]]
    .head(10)
    .to_string(index=False)
)