from collections import defaultdict
from typing import List, Dict


def parse_css(text: str) -> dict:
    styles = defaultdict(defaultdict)
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        # print(lines[i])
        if lines[i] == '' or lines[i] == '\n':
            i += 1
            continue
        else:
            assert lines[i][0] == '.'
            blocks = lines[i].split(' ')
            style_keys = []
            for b in blocks:
                if b != '' and '{' not in b:
                    assert b[0] == '.'
                    if ',' in b:
                        assert b[-1] == ','
                        style_keys.append(b[1:-1])
                    else:
                        style_keys.append(b[1:])
            # print(style_keys)
            i += 1
            parsed_dict = {}
            while '}' not in lines[i]:
                # print(lines[i])
                key, value = lines[i].split(':')
                key = key.strip()
                value = value[1:-1]
                if value == 'none':
                    value = None
                parsed_dict[key] = value
                i += 1
            i += 1
            # print(parsed_dict)
            for sk in style_keys:
                if ':' in sk:
                    sk1, sk2 = sk.split(':')
                    styles[sk1][sk2] = parsed_dict
                else:
                    styles[sk].update(parsed_dict)
    styles = {k: dict(v) for k, v in styles.items()}
    return dict(styles)


def add_styles(components: List, styles: Dict):
    for component in components:
        style_name = component['properties']['className']
        component['properties']['style'] = styles[style_name]
    return components
