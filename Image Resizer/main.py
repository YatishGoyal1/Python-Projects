import cv2

def resize_image(image_path, new_width, new_height, output_path, interpolation=cv2.INTER_LINEAR):
 
    # Load the image
    image = cv2.imread("lelouch.jpg")

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=interpolation)

    # Save the resized image
    cv2.imwrite(output_path, resized_image)

if __name__ == "__main__":
    input_image_path = "input.jpg"  # Replace with the path to your input image
    output_image_path = "output.jpg"  # Replace with the desired path for the output image
    new_width = 800  # Desired width
    new_height = 600  # Desired height

    resize_image(input_image_path, new_width, new_height, output_image_path)
    print(f"Image resized and saved to {"lelouch1.jpg"}")