import pytest
from morse_encoder_decoder import encode,morse_code_dict,decode,decode_morse_code_dict

def test_encode():
    assert encode(morse_code_dict,"Hello") == ".... . .-.. .-.. ---"
    assert encode(morse_code_dict,"Hello my name is Megan Morse") == ".... . .-.. .-.. --- | -- -.-- | -. .- -- . | .. ... | -- . --. .- -. | -- --- .-. ... ."

def test_encode_empty_message():
    assert encode(morse_code_dict, "") == ""

def test_encode_invalid_character():
    with pytest.raises(KeyError):
        assert encode(morse_code_dict,"HELLO#")
    with pytest.raises(KeyError):
        assert encode(morse_code_dict,"HELLO|")

def test_decode():
    assert decode(decode_morse_code_dict,".... . .-.. .-.. ---") == "H e l l o"
    assert decode(decode_morse_code_dict,"... ..- .--. . .-. | ... . -.-. .-. . - | .. -. - . .-.. |") == "S u p e r   s e c r e t   i n t e l  "

def test_decode_invalid_character():
    with pytest.raises(KeyError):
        assert decode(decode_morse_code_dict,"==")