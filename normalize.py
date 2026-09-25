import os
from pydub import AudioSegment, effects

# Dossiers
INPUT_FOLDER = "sounds/urban"   # Dossier contenant tes 91 sons
OUTPUT_FOLDER = "soundsnormalized/urban"   # Dossier où seront les sons normalisés

# Créer le dossier de sortie s'il n'existe pas
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def normalize_audio(input_path, output_path, target_dBFS=-14.0):
    # Charger le son
    audio = AudioSegment.from_file(input_path)
    
    # Normaliser
    change_in_dBFS = target_dBFS - audio.dBFS
    normalized_audio = audio.apply_gain(change_in_dBFS)
    
    # Exporter en mp3 (ou wav selon ton choix)
    normalized_audio.export(output_path, format="mp3")
    print(f"Normalisé : {os.path.basename(input_path)}")

# Traiter tous les fichiers du dossier
for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith((".mp3", ".wav", ".ogg")):
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)
        normalize_audio(input_path, output_path)

print("\n--- Tous les sons sont normalisés et prêts pour Senera ! ---")