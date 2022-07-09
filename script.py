from cloudinary import CloudinaryImage
import cloudinary
import cloudinary.uploader as uploader


def init_cloudinary():
    cloudinary.config(
        cloud_name="imageeditor",
        api_key="629772786785988",
        api_secret="4_TCOKBCQfGZ44LJCBUFiBXVS-g"
    )


def extract_url(image):
    return image[10:len(image) - 3]



def add_text(text, gravity='center', width=1050, height=1200, crop='fit', color="#000", font_size=40, font="Arial", x=0, y=0):
    return [
        {
            'overlay':
                {
                    'font_family': font,
                    'font_size': font_size,
                    'text': text
                },
            'color': color,
            'crop': crop,
            'width': width,
            'height': height,

            'gravity': gravity,
            'x': x,
            'y': y
        }
    ]


def add_image_transformations(image_url, gravity, width, height, opacity, x=0.0, y=0.0):
    transformations = [{
        "overlay": {'url': image_url},
        "width": width,
        "height": height,
        "opacity": opacity,
        "gravity": gravity,
        "x": x,
        "y": y
    }]

    return transformations


def generate_image():
    init_cloudinary()

    # Add text with formatting
    testimonial_transformations = [{ "width": ${background_width},
        "crop": "scale"}]
    testimonial_transformations.extend(
        add_image_transformations(image_url="${image_url}",
        gravity="north_west",x = ${image_x}, y = ${image_y}, width=${image_width}, height =${image_height}, opacity=100))
    testimonial_transformations.extend(
        add_text("${text}", "north_west", x=${text_x}, y=${text_y}))

    # Decide the background image
    image = CloudinaryImage("${background}").image(
        sign_url=True, transformation=testimonial_transformations)

    return extract_url(image)


print(generate_image())