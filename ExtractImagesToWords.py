import easyocr
import os
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

def extract_text_to_array(image_folder, output_file):
    print("Starting OCR...")
    reader = easyocr.Reader(['en'], gpu=False, verbose=False)
    print("Model loaded!")
    
    supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp')
    
    image_files = [f for f in os.listdir(image_folder) 
                   if f.lower().endswith(supported_formats)]
    
    print(f"Found {len(image_files)} images")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        #clear
        f.write("")
    
    for i, filename in enumerate(image_files, 1):
        print(f"Processing {filename} ({i}/{len(image_files)})")
        image_path = os.path.join(image_folder, filename)
        
        try:
            result = reader.readtext(image_path)
            
            # Append text to file immediately
            with open(output_file, 'a', encoding='utf-8') as f:
                for bbox, text, confidence in result:
                    if confidence > 0.5:
                        f.write(f"{text}\n")
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    
    print(f"All done! Text saved to {output_file}")

def save_array_to_file(text_array, output_file):
    """Save text array to file"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for text in text_array:
            f.write(f"{text}\n")

# Usage
if __name__ == "__main__":
    image_folder = input("Image folder path: ")
    output_file = input("Output file name: ")
    
    extract_text_to_array(image_folder, output_file)
