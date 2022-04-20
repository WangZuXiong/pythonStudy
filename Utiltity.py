def rgb_to_html_color(rgb_tuple):
    """
    convert an (R, G, B) tuple to #RRGGBB
    """

    hex_color = '#%02x%02x%02x' % rgb_tuple

    return hex_color


def html_color_to_rgb(color_str):
    """
    convert #RRGGBB to an (R, G, B) tuple
    """

    color_str = color_str.strip()

    if color_str[0] == '#':
        color_str = color_str[1:]

    if len(color_str) != 6:
        Logger.logger_error("input #%s is not in #RRGGBB format" % color_str)
        return 255, 255, 255

    r, g, b = color_str[:2], color_str[2:4], color_str[4:]
    r, g, b = [int(n, 16) for n in (r, g, b)]

    return r, g, b
