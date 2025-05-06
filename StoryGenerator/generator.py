import pathlib
import types

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client(api_key="AIzaSyCkkeM4-hW0GLcrbGALqni-UbS-2gOTc3Q")

prompt = """
        Generate a story about a cute dog a Crayon Shin-chan art style.
        For each scene, generate a image.
        The images should show the same dog in different scenes.
        """

contents = [
    types.Content(
        role="user",
        parts=[
            types.Part.from_bytes(
                data=pathlib.Path("dog.png").read_bytes(),
                mime_type="image/png"
            ),
            types.Part.from_text(text=prompt),
        ]
    )
]

response = client.models.generate_content(
    model="gemini-2.0-flash-exp",
    contents=contents,
    config=types.GenerateContentConfig(
        response_modalities=["Text", "Image"]
    ),
)

image_counter = 0
for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save(f"{image_counter}.png")
        image_counter += 1
