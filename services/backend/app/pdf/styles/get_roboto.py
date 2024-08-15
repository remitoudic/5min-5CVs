import gdown
import os

# Create a fonts directory if it doesn't exist
if not os.path.exists('fonts'):
    os.makedirs('fonts')

# URLs for the font files
urls = {
    'Roboto-Regular.ttf': 'https://github.com/openmaptiles/fonts/blob/master/roboto/Roboto-Regular.ttf',
    'Roboto-Bold.ttf': 'https://github.com/openmaptiles/fonts/blob/master/roboto/Roboto-Bold.ttf'
}

# Download each font file
for filename, url in urls.items():
    output_path = os.path.join('fonts', filename)
    gdown.download(url, output_path, quiet=False)

print("Font files downloaded successfully.")