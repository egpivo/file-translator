import os

SIZE_THRESHOLD = 5 * 1024 * 1024
CACHE_DIR = os.path.join(os.getcwd(), "cache")

TRANSLATION_API_URL = (
    "https://vitruvian-translation-worker-dev.presight.ai/api/v1/translate"
)
EXCEL_MEDIA_TYPE = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
