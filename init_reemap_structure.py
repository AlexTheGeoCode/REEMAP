import os

# Hauptverzeichnisname (optional anpassen)
base_dir = "REEMAP"

# Strukturdefinition
folders = [
    "data/raw/geologie",
    "data/raw/märkte",
    "data/raw/historisch",
    "data/processed/json",
    "data/processed/geojson",
    "data/processed/csv",
    "data/exports",
    "notebooks/exploratory",
    "scripts/python",
    "qgis/projects",
    "qgis/layers",
    "docs",
    "prompts/fundstellen",
    "prompts/marktanalyse",
    "prompts/geopolitik",
    "prompts/recycling",
    "github/workflows",
    "literature/quellen_extrakte",
    "literature/analysen",
    "visualisierung/diagramme",
    "visualisierung/karten",
    "app/streamlit",
    "projektplanung"
]

# Wichtige leere Dateien mit Beispieldaten oder Platzhaltertext
files = {
    "README.md": "# REEMAP – Rare Earth Evidence Mapping Platform\n",
    "Projektlogbuch.md": "## Projektlogbuch\n\n- [ ] 27.07.2025 – Struktur erstellt\n",
    "projektplanung/projektplan.md": "# Projektplan\n",
    "projektplanung/roadmap.md": "# Roadmap\n",
    "projektplanung/usecases.md": "# Use Cases\n",
    "docs/MVP-Architektur.md": "# MVP Architektur\n",
    "data/processed/csv/fundstellen.csv": "site_id, name, land, lat, lon, minerale\n",
    "data/processed/json/bor_fluss.json": '{\n  "site_id": "TIM-BOR-001",\n  "historical_name": "Bor Flussseifen",\n  "modern_name": "Bor, Serbien",\n  "lat": 44.0,\n  "lon": 22.0,\n  "ree_indicators": ["Ilmenit"],\n  "zujovic_reference": "Žujović, 1893, S.42",\n  "confidence_score": 0.7\n}',
    "prompts/fundstellen/historisch_extraktion.md": "# Prompt: Historische Fundstellen extrahieren\n",
    "literature/quellen_extrakte/kreb1917.md": "# Quelle: Norbert Krebs 1917 – Extrakt\n",
    ".gitignore": "# Bytecode & Jupyter\n__pycache__/\n*.pyc\n.ipynb_checkpoints/",
    "LICENSE": "MIT License"
}

# Erstellung starten
print(f"Erstelle Projektstruktur in: {base_dir}")

for folder in folders:
    path = os.path.join(base_dir, folder)
    os.makedirs(path, exist_ok=True)
    print(f"📁 Ordner erstellt: {path}")

for file, content in files.items():
    path = os.path.join(base_dir, file)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"📄 Datei erstellt: {path}")

print("\n✅ Projektstruktur erfolgreich erstellt!")
