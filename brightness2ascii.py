def brightness_to_ascii(brightness):
    # ascii charactesr ordered from darkest to lighest
    ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    ascii_index = int(brightness / 255 * (len(ascii_chars) - 1))
    return ascii_chars[ascii_index]
