# Terminal GitHub Profile — Charan Mavuduru

<p align="center">
  <img src="https://raw.githubusercontent.com/Sarma9273/terminal-github-profile/main/portrait.svg"
       alt="Charan Mavuduru — animated terminal dot-matrix portrait"
       width="620">
</p>

<p align="center">
  <strong>AI & Cybersecurity · SOC · Security Engineering · RAG · Incident Response · Research</strong>
</p>

---

This repository recreates the supplied **animated terminal-style dot-matrix portrait** as a reproducible GitHub asset.

The README above is the actual showcase: the generated `portrait.svg` is embedded directly, so opening the repository displays the portrait rather than merely showing a link to it.

## How it works

```text
portrait photo
      ↓
OpenCV subject segmentation
      ↓
contrast / luminance sampling
      ↓
dot radius + opacity mapping
      ↓
animated SVG generation
      ↓
portrait.svg
      ↓
README display
```

## Repository structure

- `1785407430921.png` — canonical source portrait
- `portrait.svg` — generated animated dot-matrix output
- `generate.py` — Python generator
- `requirements.txt` — Python dependencies
- `.github/workflows/generate-portrait.yml` — automatic regeneration workflow
- `LICENSE` — MIT license

## Generator

The implementation follows the reference architecture:

- Pillow for image loading, grayscale conversion and resizing
- OpenCV GrabCut for subject segmentation
- connected-component cleanup and morphology
- luminance-driven dot size and opacity
- native SVG `<circle>` elements
- SVG `<animate>` elements for the reveal/pulse cycle
- self-contained output with no JavaScript dependency

## Reproducible generation

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Generate the portrait:

```bash
python generate.py 1785407430921.png --output portrait.svg
```

GitHub Actions also regenerates the SVG when the generator, requirements, source portrait, or workflow changes.

## Reuse in another README

```html
<p align="center">
  <img src="https://raw.githubusercontent.com/Sarma9273/terminal-github-profile/main/portrait.svg"
       alt="Charan Mavuduru — animated terminal dot-matrix portrait"
       width="620">
</p>
```

## Featured profile areas

**RA-XSOC Security Copilot · SentinelOps-AI · SynthoQuest · GURUVERSE**

