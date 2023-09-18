import os
from datetime import datetime
from rembg import remove

class BackgroundRemover:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

    def processing_images(self):
        today = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        processed_folder = os.path.join(self.output_folder, today)
        os.makedirs(processed_folder, exist_ok=True)

        for file_name in os.listdir(self.input_folder):
            if file_name.endswith(('.png','.jpg','.jpeg')):
                input_path = os.path.join(self.input_folder, file_name)
                output_path = os.path.join(processed_folder, file_name)
                self._remove_background(input_path,  output_path)
                self._move_images_orig(input_path, processed_folder)


    def _remove_background(self, input_p, output_p):
        with open(input_p,'rb') as file_inp, open(output_p, 'wb') as file_outp:
            background_removed = remove(file_inp.read())
            file_outp.write(background_removed)


    def _move_images_orig(self, inp_path, dest_path):
        original_folder = os.path.join(dest_path, 'originals')
        os.makedirs(original_folder, exist_ok=True)
        
        filename = os.path.basename(inp_path)
        new_path = os.path.join(original_folder, filename)
        os.rename(inp_path, new_path)

if __name__ == "__main__":
    input_folder = "entrada"
    output_folder = "salida"

    removeb = BackgroundRemover(input_folder, output_folder)
    removeb.processing_images()