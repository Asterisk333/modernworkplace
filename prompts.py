# Prompt 10 topics, calendar week
def prompt_weekly(kalenderwoche: int, quellen: str) -> str:
    return (
        f"Fasse mir die 10 wichtigsten Nachrichten der letzten Woche "
        f"(Kalenderwoche: {kalenderwoche}) aus der Schweiz zusammen. "
        f"Verwende ausschliesslich die Rubriken Schweiz, Politik und Wirtschaft auf {quellen}. "
        f"Filtere alle Klatsch-, Promi-, Sport-, Gossip- oder Lifestyle-Themen konsequent heraus. "
        f"Struktur: Antworte ausschliesslich mit einem JSON-Array von 10 Objekten. "
        f"Jedes Objekt muss exakt folgende Felder enthalten: – \"title\" : 1 Satz, die Überschrift des Themas "
        f"– \"summary\" : 2–4 Sätze prägnante, sachliche Zusammenfassung (nur Fakten, keine Wertungen) "
        f"– \"source\" : URL zur Quelle "
        f"Wichtig: Gib nur valides JSON zurück, keine Einleitung, keine Meta-Kommentare, keine Erklärungen, keine Abschlussbemerkungen."
    )


# Prompt 5 topics, yesterday
def prompt_daily(datum: str, quellen: str) -> str:
    return (
        f"Fasse mir die 5 wichtigsten Nachrichten vom {datum} aus der Schweiz zusammen. "
        f"Verwende ausschliesslich die Rubriken Schweiz, Politik und Wirtschaft auf {quellen}. "
        f"Filtere alle Klatsch-, Promi-, Sport-, Gossip- oder Lifestyle-Themen konsequent heraus. "
        f"Struktur: Antworte ausschliesslich mit einem JSON-Array von 5 Objekten. "
        f"Jedes Objekt muss exakt folgende Felder enthalten: – \"title\" : 1 Satz, die Überschrift des Themas "
        f"– \"summary\" : 2–4 Sätze prägnante, sachliche Zusammenfassung (nur Fakten, keine Wertungen) "
        f"– \"source\" : URL zur Quelle "
        f"Wichtig: Gib nur valides JSON zurück, keine Einleitung, keine Meta-Kommentare, keine Erklärungen, keine Abschlussbemerkungen."
    )
