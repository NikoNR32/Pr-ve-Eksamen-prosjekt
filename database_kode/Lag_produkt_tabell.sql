CREATE TABLE IF NOT EXISTS produkter (
    produkt_id INTEGER PRIMARY KEY AUTOINCREMENT,
    navn TEXT NOT NULL,
    beskrivelse TEXT,
    pris REAL NOT NULL,
    kategori TEXT NOT NULL,
    storrelse TEXT,
    farge TEXT,
    lager_antall INTEGER NOT NULL DEFAULT 0,
    bilde_filnavn TEXT,
    opprettet_dato TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);