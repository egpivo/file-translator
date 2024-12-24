import pytest
import respx
from httpx import Response

from file_translator.config import TRANSLATION_API_URL
from file_translator.services.translation_service import translate_text


@pytest.mark.asyncio
@respx.mock
async def test_translate_text():
    # Mock response
    mock_response_data = {"text": "Hello"}
    respx.post(TRANSLATION_API_URL).mock(
        return_value=Response(200, json=mock_response_data)
    )

    input_text = "Bonjour"
    source_lang = "FRENCH"
    target_lang = "English"

    translated_text = await translate_text(input_text, source_lang, target_lang)

    assert translated_text == "Hello"
    assert respx.calls.call_count == 1
