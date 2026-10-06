import pandas as pd

# ----- edit this -----
inDir = "/Volumes/DOM_SEVEN/371DCE_260624_embryos-fix-Ect2-WTvWA/diseect_scope/frames1to134_single-cells copy/"
# ---------------------

# keep_default_na=False stops group names like "null"/"NA"/"None" being read as NaN
key   = pd.read_csv(inDir + "blind_key.csv", keep_default_na=False)
score = pd.read_csv(inDir + "furrow_scores.csv")

df = score.merge(key, on="blind_code", how="inner")
df = df[df["exclude"] != 1].copy()
df["difference"] = pd.to_numeric(df["difference"], errors="coerce")
df = df.dropna(subset=["difference"])

# per-cell unblinded table
df.to_csv(inDir + "furrow_unblinded.csv", index=False)

# per-group summary (the third CSV); dropna=False keeps any empty/edge-case group key
summary = (
    df.groupby("group", dropna=False)["difference"]
      .agg(n="count", mean="mean", median="median",
           sd="std", sem=lambda x: x.std(ddof=1) / (len(x) ** 0.5),
           min="min", max="max")
      .round(3)
      .reset_index()
)
summary.to_csv(inDir + "furrow_group_summary.csv", index=False)

print(summary.to_string(index=False))