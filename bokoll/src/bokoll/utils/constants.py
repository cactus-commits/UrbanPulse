from pathlib import Path

BASE_PATH = Path(__file__).parents[1]
ASSETS_PATH = BASE_PATH / "assets"
COMPONENTS_PATH = BASE_PATH / "components"
IMAGE_PATH = ASSETS_PATH / "images"
STYLES_PATH = ASSETS_PATH / "styles"
MAKRDOWN_PATH = ASSETS_PATH / "markdown"
DATA_PATH = ASSETS_PATH / "data"

print(ASSETS_PATH)
