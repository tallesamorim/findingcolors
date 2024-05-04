from PIL import Image
import flet as ft

def main(page: ft.Page):
    def rgb_to_hex(rgb):
        return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

    # Open the image file
    img = Image.open('imagem.png')
    # Convert the image data to RGB
    rgb_im = img.convert('RGB')
    # Get image dimensions
    width, height = rgb_im.size

    containers = []  # Initialize an empty list to store containers

    i = 15
    while i < width:
        j = 15
        while j < height:
            rgb = rgb_im.getpixel((i, j))
            hex_color = rgb_to_hex(rgb)
            print(f'Hexadecimal: {hex_color} RGB: {rgb}')
            if hex_color != '#f1f1f1':
                container = ft.Container(
                    padding=20,
                    bgcolor=hex_color,
                    width=500,
                    height=80,
                    content=ft.Text(f'hexadecimal: {hex_color} RGB: {rgb}', selectable=True)
                    
                )
                containers.append(container)  # Add container to the list
            j += 40
        i += 40

    page.adaptive = True
    page.scroll = ft.ScrollMode.ALWAYS
    page.add(
        ft.Column(
            width=500,
            controls=containers  # Pass the list of containers to the ResponsiveRow
        )
    )
    page.update()

ft.app(target=main)