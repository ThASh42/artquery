from typing import Annotated

from pydantic import Field

hexstr = Annotated[str, Field(pattern=r'^[0-9a-f]+$')]


class hexstr64(hexstr):  # type: ignore
    min_length = 64
    max_length = 64


class hexstr128(hexstr):  # type: ignore
    min_length = 128
    max_length = 128


class AccountNumber(hexstr64):
    pass


class SigningKey(hexstr64):
    pass


class Signature(hexstr128):
    pass
