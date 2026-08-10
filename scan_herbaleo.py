import os
import easyocr
import glob

reader = easyocr.Reader(['id', 'en'], gpu=False)

search_dir = r"D:\Alan\OneDrive - PT. ERA CARING INDONESIA\MY_WORKSPACE\01_ACTIVE_PROJECT\Integration Telemed Omipos\GrabMart\prd_imgs\prd_imgs"
target = "herbaleo"

image_files = glob.glob(os.path.join(search_dir, "*.jpg"))
print(f"Scanning {len(image_files)} images for '{target}'...")

matches = []
for i, img_path in enumerate(image_files):
    filename = os.path.basename(img_path)
    try:
        results = reader.readtext(img_path, detail=0)
        text = " ".join(results).lower()
        if target.lower() in text:
            matches.append((filename, text))
            print(f"  [MATCH] {filename}")
        else:
            print(f"  [{i+1}/{len(image_files)}] {filename} - not found")
    except Exception as e:
        print(f"  [{i+1}/{len(image_files)}] {filename} - ERROR: {e}")

print(f"\n=== RESULTS ===")
if matches:
    print(f"Found {len(matches)} image(s) containing '{target}':")
    for filename, text in matches:
        print(f"  - {filename}")
else:
    print(f"No images found containing '{target}'.")
