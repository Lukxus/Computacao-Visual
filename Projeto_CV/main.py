# # from PIL import Image
# # import numpy as np
# # import matplotlib.pyplot as plt
# # from matplotlib.animation import FuncAnimation

# # def generate_fade_images(image_path, num_steps=40):  # Aumento para 40 passos
# #     img = Image.open(image_path).convert("RGBA")
# #     images = []

# #     for step in range(num_steps):
# #         factor = step / num_steps
# #         img_array = np.array(img)
        
# #         # Calcula o fator de transparência variando linearmente ao longo do eixo y
# #         fade = np.linspace(1, 0, img.height)[:, np.newaxis]
# #         fade = np.repeat(fade, img.width, axis=1)
# #         fade = np.repeat(fade[:, :, np.newaxis], 4, axis=2)  # Repete o fade para todas as canais de cor
# #         fade[..., 3] = 1  # Assegura que o canal alpha não seja modificado pelo fade

# #         faded_img_array = img_array * (1 - factor * fade)  # Aplica o fade variável
# #         faded_img_array = faded_img_array.astype(np.uint8)
        
# #         images.append(Image.fromarray(faded_img_array))
    
# #     return images

# # def update(frame):
# #     ax.imshow(np.array(fade_images[frame]))
# #     ax.set_title(f"Step: {frame + 1}")

# # # Caminho para a sua imagem
# # image_path = "kodim23.png"
# # fade_images = generate_fade_images(image_path, num_steps=40)  # Aumentando o número de passos para 40

# # fig, ax = plt.subplots()
# # ani = FuncAnimation(fig, update, frames=len(fade_images), repeat=False, interval=25)  # Reduzindo o intervalo para 25ms
# # ax.axis('off')
# # plt.show()

# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# def generate_fade_images(image_path, num_steps=20):
#     # Carrega a imagem
#     img = Image.open(image_path).convert("RGBA")
#     width, height = img.size
#     images = []

#     # Gera imagens com diferentes níveis de opacidade
#     for step in range(num_steps):
#         # Cria uma nova imagem com fundo transparente
#         new_image = Image.new("RGBA", (width, height))
#         factor = step / num_steps

#         # Aplica o efeito de fade
#         for y in range(height):
#             for x in range(width):
#                 pixel = img.getpixel((x, y))
#                 opacity = int(255 * (1 - factor * (y / max(height - 1, 1))))
#                 new_pixel = (pixel[0], pixel[1], pixel[2], opacity)
#                 new_image.putpixel((x, y), new_pixel)
        
#         images.append(new_image)

#     return images

# def update(frame, images, ax):
#     ax.imshow(np.array(images[frame]), interpolation='nearest')
#     ax.axis('off')

# # Caminho para a sua imagem - Substitua por um caminho de arquivo válido ou faça upload de uma imagem
# image_path = "Projeto_CV/kodim23.png"
# fade_images = generate_fade_images(image_path, num_steps=20)

# fig, ax = plt.subplots()
# ani = FuncAnimation(fig, update, frames=len(fade_images), fargs=(fade_images, ax), repeat=False)

# plt.show()


# Primeiro, instale a biblioteca Pillow, se ainda não estiver instalada
from PIL import Image

def generate_fade_images(image_path, num_steps=20):
    # Carrega a imagem
    img = Image.open(image_path).convert("RGBA")
    width, height = img.size
    images = []

    # Prepara uma imagem de fundo preto (ou qualquer outra cor) para o fade
    black_background = Image.new('RGBA', img.size, (0, 0, 0, 255))
    
    # Gera imagens com diferentes níveis de opacidade para a camada preta
    for step in range(num_steps):
        # Cria uma cópia da imagem original
        faded_image = img.copy()
        # Calcula a opacidade para a camada preta
        alpha = int(255 * (step / num_steps))
        # Cria uma camada sólida preta com a opacidade atual
        fade_layer = Image.new('RGBA', img.size, (0, 0, 0, alpha))
        # Combina a camada de fade com a imagem original
        faded_image = Image.alpha_composite(faded_image, fade_layer)
        images.append(faded_image)

    return images

# Define o caminho para sua imagem
image_path = "Projeto_CV/kodim23.png"

# Gera as imagens com efeito de fade
fade_images = generate_fade_images(image_path, num_steps=1000)

# Salva as imagens como um arquivo GIF
fade_images[0].save('fade_effect.gif',
                    save_all=True,
                    append_images=fade_images[1:],
                    duration=0,  # Ajuste o tempo em ms entre os frames conforme desejado
                    loop=0,
                    optimize=False)

print("GIF criado com sucesso e salvo como 'fade_effect.gif'")
