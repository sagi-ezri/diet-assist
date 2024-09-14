# 🍽️ Diet Assist App

The **Diet Assist App** is an AI-powered tool designed to help users make informed dietary decisions. The app allows users to upload an image of food, detects whether it contains a specific type of food, and provides a health recommendation based on the user’s dietary goals. The app also includes text-to-speech functionality to audibly deliver the recommendation.

## Features

- **Image Upload**: Users can upload images in JPEG or PNG formats.
- **Food Detection**: The app detects whether the uploaded image contains food.
- **Food Classification**: Identifies the specific type of food in the image.
- **Health Recommendations**: Offers advice on whether to eat the detected food based on health goals.
- **Text-to-Speech**: Converts the recommendation to speech and plays the audio within the app.

## Installation

### Prerequisites

- Python 3.10 or higher
- Poetry (for dependency management)

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/sagi-ezri/diet-assist.git
cd diet-assist
```

### Install Dependencies

Use Poetry to install the required dependencies:

```bash
poetry install
```

This will install all the dependencies specified in the `pyproject.toml` file.

## Usage

To run the application, use the following command:

```bash
poetry run streamlit run app.py
```

This will start a local Streamlit server, and you can access the app in your web browser at `http://localhost:8501`.

### Steps to Use the App

1. **Upload an Image**: Click on "Choose an image..." to upload a JPEG or PNG file.
2. **View the Image**: The uploaded image will be displayed within the app.
3. **Detection and Classification**: The app will analyze the image to detect and classify any food present.
4. **Health Recommendation**: If food is detected, the app will generate a recommendation on whether you should eat the food.
5. **Listen to the Recommendation**: The recommendation will be converted to speech and played back within the app.

## Testing

To run the tests, use the following command:

```bash
poetry run pytest tests/
```

This command will execute the test cases located in the `tests/` directory.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- The app uses the `gTTS` library for text-to-speech functionality.
- The food detection model is powered by PyTorch.
- The health recommendation feature is supported by the OpenAI API.

---

Thank you for using the Diet Assist App! If you have any questions or feedback, please feel free to contact us.
