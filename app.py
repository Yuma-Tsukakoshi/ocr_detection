import io
import os


# # Imports the Google Cloud client library
# from google.cloud import vision

# # Instantiates a client
# client = vision.ImageAnnotatorClient()

# # The name of the image file to annotate
# file_name = os.path.abspath('data/receipt.png')

# # Loads the image into memory
# with io.open(file_name, 'rb') as image_file:
#     content = image_file.read()

# image = vision.Image(content=content)

# # Performs label detection on the image file
# response =  client.document_text_detection(
#         image=image,
#         image_context={'language_hints': ['ja']}
#     )

# # レスポンスからテキストデータを抽出
# output_text = ''
# for page in response.full_text_annotation.pages:
#     for block in page.blocks:
#         for paragraph in block.paragraphs:
#             for word in paragraph.words:
#                 output_text += ''.join([
#                     symbol.text for symbol in word.symbols
#                 ])
#             output_text += '\n'

# print(output_text)

def detect_text_uri():
    """Detects text in the file located in Google Cloud Storage or on the Web."""
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()
    file_name = os.path.abspath('data/receipt.png')
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
      content = image_file.read()
    
    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")

    for text in texts:
        print(f'\n"{text.description}"')

        vertices = [
            f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
        ]

        print("bounds: {}".format(",".join(vertices)))

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

detect_text_uri()
