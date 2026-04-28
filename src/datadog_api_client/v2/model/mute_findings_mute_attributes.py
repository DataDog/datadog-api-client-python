# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.mute_findings_reason import MuteFindingsReason


class MuteFindingsMuteAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mute_findings_reason import MuteFindingsReason

        return {
            "description": (str,),
            "expire_at": (int,),
            "is_muted": (bool,),
            "reason": (MuteFindingsReason,),
        }

    attribute_map = {
        "description": "description",
        "expire_at": "expire_at",
        "is_muted": "is_muted",
        "reason": "reason",
    }

    def __init__(
        self_,
        is_muted: bool,
        reason: MuteFindingsReason,
        description: Union[str, UnsetType] = unset,
        expire_at: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Mute properties to apply to the findings.

        :param description: Additional information about the reason why the findings are muted or unmuted. This field has a limit of 280 characters.
        :type description: str, optional

        :param expire_at: The expiration date of the mute action (Unix ms). It must be set to a value greater than the current timestamp. If this field is not provided, the findings remain muted indefinitely.
        :type expire_at: int, optional

        :param is_muted: Whether the findings should be muted or unmuted.
        :type is_muted: bool

        :param reason: The reason why the findings are muted or unmuted.
        :type reason: MuteFindingsReason
        """
        if description is not unset:
            kwargs["description"] = description
        if expire_at is not unset:
            kwargs["expire_at"] = expire_at
        super().__init__(kwargs)

        self_.is_muted = is_muted
        self_.reason = reason
