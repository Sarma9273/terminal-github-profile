# Terminal GitHub Profile — Charan Mavuduru

A GitHub-ready animated terminal dot portrait generator and profile asset system.

## Intended output

The final asset is an animated, high-resolution dot-matrix portrait rendered as a self-contained SVG. It is designed for your GitHub profile README, project READMEs and your personal site.

## Architecture

- Source: one portrait photo
- Processing: OpenCV + Pillow
- Subject isolation: GrabCut + morphological cleanup
- Rendering: luminance-driven dot radius and opacity
- Animation: native SVG animation
- Output: one portable SVG with no browser runtime dependency
- GitHub: committed SVG can be rendered directly in a README

## Generate

Requires Python 3.10+.

1. Put your portrait at assets/profile.png.
2. Install dependencies: python -m pip install -r requirements.txt
3. Run: python generate.py assets/profile.png --output portrait.svg
4. Commit portrait.svg.

For the best result, use a centered portrait with reasonable contrast and a simple background.

## Profile identity

Charan Mavuduru — AI & Cybersecurity, SOC / Security Engineering, RAG security copilots, RA-XSOC, SentinelOps-AI, SynthoQuest and GURUVERSE.

## Embed in your GitHub profile README

Use the raw SVG from this repository with an HTML image element pointing to:
https://raw.githubusercontent.com/Sarma9273/terminal-github-profile/main/portrait.svg

## Important

The reference ZIP supplied for this project contains an example portrait. It is not used as your identity image. The personalized portrait must be generated from your own photo.

## License

MIT
