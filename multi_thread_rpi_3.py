import importlib
import sys
import time
import threading
import subprocess  # ✅ pour pouvoir lancer des commandes shell (pip install)

# --- Vérification des bibliothèques ---
required_libs = ["time", "threading", "requests"]  # 👈 tu peux ajouter ici d’autres libs externes

print("Vérification des bibliothèques nécessaires...")

for lib in required_libs:
    try:
        importlib.import_module(lib)
        print(f"✅ {lib} est disponible.")
    except ImportError:
        print(f"❌ {lib} n'est pas installé. Installation en cours...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", lib], check=True)
            print(f"✅ {lib} a été installé avec succès.")
        except subprocess.CalledProcessError:
            print(f"⚠️ Impossible d’installer automatiquement {lib}. Vérifie le nom du package.")

print("\n--- Démarrage des threads ---\n")

# --- Fonctions des threads ---
def say_hello():
    while True:
        print("hello")
        time.sleep(1)

def say_caca():
    while True:
        print("caca")
        time.sleep(0.5)

# --- Création des threads ---
thread1 = threading.Thread(target=say_hello, daemon=True)
thread2 = threading.Thread(target=say_caca, daemon=True)

# --- Lancement des threads ---
thread1.start()
thread2.start()

# --- Boucle principale (empêche le programme de se terminer) ---
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nArrêt manuel du programme.")
