W, H = 800, 400
CX, CY = W / 2, H / 2
NUM_STARS = 200

svg_lines = []
def add(s):
    svg_lines.append(s)

add(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">')
add('<style>')

add(f'''
circle {{
  --i: sibling-index();
  --angle: calc(var(--i) * 137.508deg);
  --dist: calc(280px + mod(var(--i) * 97, 320) * 1px);
  r: calc(0.4px + mod(var(--i) * 0.618, 1) * 1.4px);
  fill: #ffffff;
  opacity: 0;
  animation: fly linear infinite;
  animation-duration: calc(2s + mod(var(--i) * 0.73, 4) * 1s);
  animation-delay: calc(mod(var(--i) * 1.37, 7) * -1s);
}}

@media (prefers-color-scheme: light) {{
  circle {{ fill: #1b1f24; }}
}}

@keyframes fly {{
  0% {{
    transform: translate({CX}px, {CY}px) rotate(var(--angle)) translateX(0px) scale(0.1);
    opacity: 0;
  }}
  10% {{ opacity: 0.3; }}
  50% {{ opacity: 0.8; }}
  85% {{ opacity: 1; }}
  100% {{
    transform: translate({CX}px, {CY}px) rotate(var(--angle)) translateX(var(--dist)) scale(1);
    opacity: 0;
  }}
}}
''')

add('</style>')

add('<g>')
for i in range(NUM_STARS):
    add('<circle/>')
add('</g>')

add('</svg>')

with open('starfield.svg', 'w') as f:
    f.write('\n'.join(svg_lines))

print(f"{len('\n'.join(svg_lines))} bytes")
