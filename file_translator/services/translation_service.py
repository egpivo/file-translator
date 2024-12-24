import httpx

from file_translator.config import TRANSLATION_API_URL
from file_translator.schemas import TranslationPayload


def get_translation_headers():
    return {"accept": "application/json", "Content-Type": "application/json"}


async def translate_text(
    text: str, source_lang: str = "FRENCH", target_lang: str = "English"
) -> str:
    payload = TranslationPayload(
        src_lang=source_lang,
        dst_lang=target_lang,
        text=text,
        llm_config={
            "llm_api_url": "http://vitruvian-llm-api-dev.llm-api.svc.cluster.local:8080/openai/v1",
            "llm_api_key": "TEMPTY",
            "llm_model_name": "gpt-4o",
            "llm_temperature": 0,
        },
    ).dict()

    async with httpx.AsyncClient(timeout=httpx.Timeout(40.0)) as client:
        response = await client.post(
            TRANSLATION_API_URL, headers=get_translation_headers(), json=payload
        )
        response.raise_for_status()
        return response.json().get("text", text)
