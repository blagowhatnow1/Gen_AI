import requests
import pickle

image_urls = [
    "https://example.com/path/to/image1.png",  # Replace with actual URLs
    "https://example.com/path/to/image2.png"
]

# Dictionary to store images and config for pickling
pickle_data = {
    "config": config,
    "images": {}
}

# Loop to download images and store them in the dictionary
for idx, image_url in enumerate(image_urls):
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        image_filename = f"image_{idx + 1}.png"
        pickle_data['images'][image_filename] = image_response.content
        print(f"Downloaded and stored {image_filename}")
    else:
        print(f"Failed to download image from {image_url}")

# Pickle the configuration and images
pickle_filename = "images_data.pkl"
with open(pickle_filename, "wb") as pickle_file:
    pickle.dump(pickle_data, pickle_file)
    print(f"Data pickled to {pickle_filename}")

# Unpickling the data
with open(pickle_filename, "rb") as pickle_file:
    unpickled_data = pickle.load(pickle_file)

# Accessing the unpickled data
unpickled_config = unpickled_data["config"]
unpickled_images = unpickled_data["images"]

print("Unpickled configuration:", unpickled_config)
for image_name, image_content in unpickled_images.items():
    # Optionally, save the unpickled image to a file
    with open(f"unpickled_{image_name}", "wb") as image_file:
        image_file.write(image_content)
    print(f"Unpickled and saved {image_name}")
