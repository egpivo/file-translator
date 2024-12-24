from pydantic import BaseModel


class TranslationPayload(BaseModel):
    src_lang: str
    dst_lang: str
    text: str
    llm_config: dict
