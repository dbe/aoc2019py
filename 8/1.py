def run(lines):
    pixels = lines[0]
    per_page = 6 * 25
    pages = len(pixels) // per_page

    min_layer = None
    min_zeros = float('inf')

    for i in range(pages):
        start = i * per_page
        layer = pixels[start:start + per_page]
        zeros = num_pixels(layer, '0')
        if(zeros < min_zeros):
            min_layer = layer
            min_zeros = zeros

    return num_pixels(min_layer, '1') * num_pixels(min_layer, '2')

def num_pixels(layer, pixel):
    count = 0

    for p in layer:
        if p == pixel:
            count += 1

    return count
