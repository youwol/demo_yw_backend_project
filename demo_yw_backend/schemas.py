"""
Module gathering the schemas of bodies and responses of the end points.
"""

from typing import Literal

from pydantic import BaseModel


class CowSayBody(BaseModel):
    """
    Body to the endpoint `/cow-say`.
    """

    message: str
    """
    Message to display.
    """
    character: Literal[
        "beavis",
        "cheese",
        "cow",
        "daemon",
        "dragon",
        "fox",
        "kitty",
        "meow",
        "miki",
        "milk",
        "octopus",
        "pig",
        "stegosaurus",
        "stimpy",
        "trex",
        "turkey",
        "turtle",
        "tux",
    ]
    """
    Character to use.
    """


class AsyncTaskResult(BaseModel):
    """
    Represents a result send via wb-socket when calling the endpoint `/async-job`
    """

    result: str
    """
    The result.
    """


class CustomAssetBody(BaseModel):
    """
    Body specification of the endpoint `/create-asset`.
    """

    name: str = "foo"
    """
    Name of the asset.
    """
    id: str = "demo_yw_backend-custom-foo-id"
    """
    Asset ID.
    """
    tags: list[str] = ["demo_yw_backend", "create-asset"]
    """
    Tags associated to the assets.
    """
    description: str = "A foo asset."
    """
    Asset's description.
    """
