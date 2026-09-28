# Terminal GitHub Profile — Charan Mavuduru

A GitHub-ready **animated dot-matrix portrait system** based on the supplied reference project.

## What this repository produces

A centered portrait is converted into thousands of luminous green dots and exported as an animated SVG. The SVG is self-contained and can be embedded directly in a GitHub profile README.

### Pipeline

```text
profile photo
     ↓
OpenCV subject segmentation
     ↓
contrast / luminance sampling
     ↓
dot radius + opacity mapping
     ↓
native SVG animation
     ↓
portrait.svg
```

## Files

- `generate.py` — OpenCV/Pillow generator
- `requirements.txt` — Python dependencies
- `assets/profile.png` — source portrait
- `portrait.svg` — generated animated output
- `.github/workflows/generate-portrait.yml` — reproducible GitHub Actions build

## Automatic generation

The GitHub Action generates `portrait.svg` whenever the generator or source portrait changes.

If `assets/profile.png` is absent, the workflow uses the public GitHub avatar for **Sarma9273** as the fallback source. To use the higher-quality portrait supplied for this project, replace `assets/profile.png` with that image and push it.

## Embed

```html
<p align="center">
  <img src="https://raw.githubusercontent.com/Sarma9273/terminal-github-profile/main/portrait.svg"
       alt="Charan Mavuduru — animated dot portrait"
       width="620">
</p>
```

## Profile focus

**AI & Cybersecurity · SOC · Security Engineering · RAG · Incident Response · Research**

Featured work includes RA-XSOC Security Copilot, SentinelOps-AI, SynthoQuest and GURUVERSE.

## Local generation

```bash
python -m pip install -r requirements.txt
python generate.py assets/profile.png --output portrait.svg
```

MIT License.
