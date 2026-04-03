import random

# uncomment if you want the same field every time
#random.seed(1337)

W, H = 800, 400
CX, CY = W / 2, H / 2
NUM_STARS = 200

svg_lines = []
def add(s):
    svg_lines.append(s)

add(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">')
add('<style>')

add('''
circle { fill: #ffffff; }

@media (prefers-color-scheme: light) {
  circle { fill: #1b1f24; }
}

@keyframes fly {
  0% {
    transform: translate(var(--cx), var(--cy)) rotate(var(--angle)) translateX(0px) scale(0.1);
    opacity: 0;
  }
  10% { opacity: 0.3; }
  50% { opacity: 0.8; }
  85% { opacity: 1; }
  100% {
    transform: translate(var(--cx), var(--cy)) rotate(var(--angle)) translateX(var(--dist)) scale(1);
    opacity: 0;
  }
}
''')

for i in range(NUM_STARS):
    angle_deg = random.uniform(0, 360)
    max_dist = random.uniform(280, 600)
    duration = random.uniform(2.0, 6.0)
    delay = random.uniform(0, 7.0)

    add(f'.s{i} {{')
    add(f'  --angle: {angle_deg:.1f}deg;')
    add(f'  --cx: {CX}px;')
    add(f'  --cy: {CY}px;')
    add(f'  --dist: {max_dist:.0f}px;')
    add(f'  animation: fly {duration:.1f}s {delay:.1f}s linear infinite;')
    add(f'}}')

add('</style>')

for i in range(NUM_STARS):
    r = random.uniform(0.4, 1.8)
    add(f'<circle class="s{i}" cx="0" cy="0" r="{r:.1f}" opacity="0"/>')

add('</svg>')

with open('starfield.svg', 'w') as f:
    f.write('\n'.join(svg_lines))

print(f"{len('\n'.join(svg_lines))} bytes")
