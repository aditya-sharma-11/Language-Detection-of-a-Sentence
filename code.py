from langdetect import detect

# Function to detect the language of a sentence
def detect_language(text):
    return detect(text)

# Dictionary of some famous Languages and their respective codes
codes = {
    'ar': 'Arabic', 'et': 'Armenian', 'art': 'Artificial Language',
    'sq': 'Albanian', 'bn': 'Bangla', 'bh': 'Bhojpuri',
    'bul': 'Bulgarian', 'cai': 'Central American Indian Language',
    'cze': 'Czech', 'da': 'Danish', 'de': 'German', 'eg': 'Egyptian', 'en': 'English',
    'fr': 'French', 'gon': 'Gondi', 'el': 'Greek', 'gsw': 'Swiss German', 'hi': 'Hindi',
    'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese', 'kn': 'Kannada',
    'ks': 'Kashmiri', 'ka': 'Georgian', 'ko': 'Korean', 'la': 'Latin',
    'mr': 'Marathi', 'mni': 'Manipuri', 'mul': 'Multiple Languages', 'nl': 'Dutch',
    'te': 'Telugu', 'ta': 'Tamil', 'cy': 'Welsh'
}

# Taking input from the user
text = input("Enter the sentence: ")

try:
    # Detecting language
    detected_code = detect_language(text)
    # Retrieving language name from the dictionary
    language_name = codes.get(detected_code, "Unknown Language")
    print("The language of the text is:", language_name)
except Exception as e:
    print("An error occurred:", e)
