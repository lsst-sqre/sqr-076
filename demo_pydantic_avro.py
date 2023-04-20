"""Demo Pydantic models based on Squarebot schemas."""

from __future__ import annotations

import json
from enum import Enum
from pathlib import Path
from typing import Optional

from pydantic import Field
from pydantic_avro.base import AvroBase


class SlackMessageType(str, Enum):
    app_mention = "app_mention"
    message = "message"


class SlackChannelType(str, Enum):
    channel = "channel"  # public channel
    group = "group"  # private channel
    im = "im"  # direct message
    mpim = "mpim"  # multi-persion direct message


class SquarebotMessage(AvroBase):
    """Model for a Slack message produced by Squarebot."""

    type: SlackMessageType = Field(description="The Slack message type.")

    channel: str = Field(
        description=(
            "ID of the channel where the message was sent "
            "(e.g., C0LAN2Q65)."
        )
    )

    channel_type: SlackChannelType = Field(
        description="The type of channel (public, direct im, etc..)"
    )

    user: Optional[str] = Field(
        None,
        description="The ID of the user that sent the message (eg U061F7AUR).",
    )

    text: str = Field(description="Content of the message.")

    ts: str = Field(description="Timestamp of the message.")

    event_ts: str = Field(description="When the event was dispatched.")


if __name__ == "__main__":
    avro_schema = SquarebotMessage.avro_schema()
    p = Path("squarebot_message.pydantic-avro.avsc")
    p.write_text(json.dumps(avro_schema, indent=2, sort_keys=True))
