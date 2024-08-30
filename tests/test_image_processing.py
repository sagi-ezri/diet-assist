
import unittest
from PIL import Image
from diet_assist_app.image_processing import transform_image

class TestImageProcessing(unittest.TestCase):
    
    def test_transform_image(self):
        image = Image.new('RGB', (256, 256), color = 'red')
        tensor = transform_image(image)
        self.assertEqual(tensor.shape, (1, 3, 224, 224))

if __name__ == '__main__':
    unittest.main()
