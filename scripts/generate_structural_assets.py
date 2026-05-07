"""Generate local binary deliverables that are intentionally not committed.

This repository avoids tracking binary files. Run this script after cloning if you
need structural placeholder PNGs and a PDF generated from the Markdown report
before executing the notebook with the real CICIDS2017 dataset.

The notebook will regenerate the real analysis figures when the dataset is
provided.
"""
from __future__ import annotations

from pathlib import Path
import re
import struct
import textwrap
import zlib

ROOT = Path(__file__).resolve().parents[1]
FIGURES_DIR = ROOT / "figures"
REPORT_MD = ROOT / "informe_cicids2017_aws_trafico_red.md"
REPORT_PDF = ROOT / "informe_cicids2017_aws_trafico_red.pdf"

FIGURE_FILES = [
    "01_distribucion_labels.png",
    "02_benigno_vs_malicioso.png",
    "03_attack_category.png",
    "04_top_destination_ports.png",
    "05_hist_flow_duration.png",
    "06_boxplot_flow_duration_attack.png",
    "07_hist_flow_bytes.png",
    "08_boxplot_flow_packets_attack.png",
    "09_service_context.png",
    "10_heatmap_attack_service.png",
    "11_scatter_flowbytes_flowpackets.png",
    "12_promedio_duration_attack.png",
]


def _png_chunk(kind: bytes, data: bytes) -> bytes:
    return (
        struct.pack(">I", len(data))
        + kind
        + data
        + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
    )


def write_placeholder_png(path: Path, width: int = 1000, height: int = 580) -> None:
    """Write a minimal valid PNG placeholder using only the Python stdlib."""
    color = (245, 247, 250)
    raw = b"".join(b"\x00" + bytes(color) * width for _ in range(height))
    data = (
        b"\x89PNG\r\n\x1a\n"
        + _png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
        + _png_chunk(b"IDAT", zlib.compress(raw, 9))
        + _png_chunk(b"IEND", b"")
    )
    path.write_bytes(data)


def _escape_pdf_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def write_simple_pdf(markdown_path: Path, output_path: Path) -> None:
    """Create a lightweight PDF representation of the Markdown report."""
    markdown = markdown_path.read_text(encoding="utf-8")
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "[Figura incluida en carpeta figures/]", markdown)
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.S)
    text = text.replace("\\newpage", "\n")
    text = re.sub(r"[#*_`>|]+", " ", text)

    lines: list[str] = []
    for paragraph in text.splitlines():
        paragraph = paragraph.strip()
        lines.extend([""] if not paragraph else textwrap.wrap(paragraph, width=88))

    pages = [lines[index : index + 46] for index in range(0, len(lines), 46)] or [["Informe"]]
    font_id = 3 + 2 * len(pages)
    objects: list[tuple[int, bytes]] = [(1, b"<< /Type /Catalog /Pages 2 0 R >>")]
    kids: list[int] = []

    for index, page_lines in enumerate(pages):
        page_id = 3 + 2 * index
        content_id = page_id + 1
        kids.append(page_id)
        stream = ["BT", "/F1 10 Tf", "50 790 Td", "14 TL"]
        for line in page_lines:
            stream += [f"({_escape_pdf_text(line[:110])}) Tj", "T*"]
        stream.append("ET")
        data = "\n".join(stream).encode("latin-1", "replace")
        objects += [
            (
                page_id,
                (
                    f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] "
                    f"/Resources << /Font << /F1 {font_id} 0 R >> >> "
                    f"/Contents {content_id} 0 R >>"
                ).encode(),
            ),
            (content_id, b"<< /Length " + str(len(data)).encode() + b" >>\nstream\n" + data + b"\nendstream"),
        ]

    pages_object = (
        "<< /Type /Pages /Kids ["
        + " ".join(f"{kid} 0 R" for kid in kids)
        + f"] /Count {len(kids)} >>"
    ).encode()
    objects += [
        (2, pages_object),
        (font_id, b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"),
    ]
    objects = sorted(objects)

    output = bytearray(b"%PDF-1.4\n")
    offsets: dict[int, int] = {}
    for number, data in objects:
        offsets[number] = len(output)
        output += f"{number} 0 obj\n".encode() + data + b"\nendobj\n"

    xref = len(output)
    max_object = max(offsets)
    output += f"xref\n0 {max_object + 1}\n".encode() + b"0000000000 65535 f \n"
    for index in range(1, max_object + 1):
        output += f"{offsets.get(index, 0):010d} 00000 n \n".encode()
    output += f"trailer\n<< /Size {max_object + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    output_path.write_bytes(output)


def main() -> None:
    FIGURES_DIR.mkdir(exist_ok=True)
    for figure in FIGURE_FILES:
        write_placeholder_png(FIGURES_DIR / figure)
    write_simple_pdf(REPORT_MD, REPORT_PDF)
    print("Generated local placeholder figures and PDF deliverable.")


if __name__ == "__main__":
    main()
