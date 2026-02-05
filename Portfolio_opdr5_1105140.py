import pandas as pd

df = pd.read_csv("events.csv")

print(df.head())

print("VRAAG 1: Aantal rijen en kolommen")
print(df.shape)

print("\nVRAAG 2: Percentage lege waarden per kolom")
lege_percentages = df.isnull().mean() * 100
print(lege_percentages)

print("\nVRAAG 3: Aantal dubbele rijen")
print(df.duplicated().sum())

print("\nVRAAG 4: Aantal volledig lege rijen")
print(df.isnull().all(axis=1).sum())

print("\nVRAAG 5: Voorbeeld van datumwaarden")
for col in df.columns:
    if "date" in col.lower():
        print(col)
        print(df[col].head())

print("\nVRAAG 6: Kolomnamen")
print(df.columns)

print("\nVRAAG 7: Statistische samenvatting")
print(df.describe(include='all'))

print("\nVRAAG 8: Datatypes per kolom")
print(df.dtypes)

print("Aantal rijen voor opschonen:", len(df))
df = df.drop_duplicates()
print("Aantal rijen na opschonen:", len(df))

df["n_vis"] = df["n_vis"].str.replace(",", ".", regex=False)
df["n_vis"] = pd.to_numeric(df["n_vis"], errors="coerce")

df = df.drop(columns=["cnt_vis"])

df["datum_ID"] = pd.to_datetime(df["datum_ID"], errors="coerce")

weer_kolommen = ["temp", "tC", "r_mm", "wind_ms"]

for kolom in weer_kolommen:
    df[kolom] = df[kolom].astype(str).str.replace(",", ".", regex=False)
    df[kolom] = pd.to_numeric(df[kolom], errors="coerce")

print("\nControle na opschonen")
print(df.info())
print(df.head())

df.to_csv("events_cleaned.csv", index=False)
print("Opgeschoonde dataset opgeslagen als events_cleaned.csv")
