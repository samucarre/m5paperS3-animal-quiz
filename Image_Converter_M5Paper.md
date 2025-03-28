🖼️ Image Converter for M5Paper

This tool uses ImageMagick to convert images into a format compatible with M5Paper e-ink display.

🔧 Command
mogrify -resize 200x200 -colorspace Gray -colors 16 -format png -path ./converted *.png

📄 What it does:
	•	Resizes images to 200x200 pixels
	•	Converts to grayscale (16 levels)
	•	Converts format to PNG
	•	Saves the converted files into the ./converted folder

✅ Requirements
	•	ImageMagick
