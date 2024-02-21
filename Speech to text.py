# Druhý krok

from openai import OpenAI
from tkinter import filedialog
# import os

api_key = "your API"  # nahraďte tímto svým API klíčem
client = OpenAI(api_key=api_key)

def otevri_soubor():
    global audio_file
    audio_file = filedialog.askopenfilename()
    if not audio_file:  # Pokud uživatel nevybral soubor
        return None
    # last_name = os.path.basename(audio_file)
    return audio_file

open_file = otevri_soubor()

if open_file:  # Pokud uživatel vybral soubor
    with open(f"{open_file}", "rb") as audio_file:
        transcript = client.audio.transcriptions.create(file=audio_file, model="whisper-1", response_format="srt", timestamp_granularities=["segment"])

    # Uložit hodnoty proměnné transcript do cílové složky
    output_file_path = filedialog.asksaveasfilename(defaultextension=".srt", filetypes=[("SRT files", "*.srt")])

    # Uložit obsah do vybraného souboru
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(str(transcript))

    print(f"Transkripce byla úspěšně uložena do souboru {output_file_path}.")
else:
    print("Uživatel nevybral soubor.")