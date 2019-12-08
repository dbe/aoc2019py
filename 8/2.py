def run(lines):
    pixels = lines[0]
    per_layer = 6 * 25
    layers = len(pixels) // per_layer

    final = ['2'] * per_layer

    for i in range(layers):
        start = i * per_layer
        layer = pixels[start:start + per_layer]

        for i, p in enumerate(layer):
            if(p != '2' and final[i] == '2'):
                final[i] = p

    for y in range(6):
        for x in range(25):
            i = 25 * y + x
            if(final[i] == '1'):
                print("\u25A0", end='')
            else:
                print(' ', end='')
        print()
