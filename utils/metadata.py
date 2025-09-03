import os
import ffmpeg
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

def extract_info(filepath):
    data = {}

    filename = os.path.basename(filepath)
    name, ext = os.path.splitext(filename)

    data["filename"] = filename
    data["ext"] = ext.replace(".", "")

    parser = createParser(filepath)
    if parser:
        metadata = extractMetadata(parser)
        if metadata:
            if metadata.has("duration"):
                data["duration"] = str(metadata.get("duration"))
            if metadata.has("width"):
                data["width"] = metadata.get("width")
            if metadata.has("height"):
                data["height"] = metadata.get("height")

    try:
        probe = ffmpeg.probe(filepath)
        if "streams" in probe:
            for stream in probe["streams"]:
                if stream.get("codec_type") == "video":
                    data["resolution"] = f"{stream.get('width')}x{stream.get('height')}"
                if stream.get("codec_type") == "audio":
                    data["artist"] = stream.get("tags", {}).get("artist")
                    data["title"] = stream.get("tags", {}).get("title")
    except:
        pass

    return data
