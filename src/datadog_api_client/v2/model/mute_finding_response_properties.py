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
    from datadog_api_client.v2.model.finding_mute_reason import FindingMuteReason


class MuteFindingResponseProperties(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.finding_mute_reason import FindingMuteReason

        return {
            "description": (str,),
            "expiration_date": (int,),
            "muted": (bool,),
            "reason": (FindingMuteReason,),
        }

    attribute_map = {
        "description": "description",
        "expiration_date": "expiration_date",
        "muted": "muted",
        "reason": "reason",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        expiration_date: Union[int, UnsetType] = unset,
        muted: Union[bool, UnsetType] = unset,
        reason: Union[FindingMuteReason, UnsetType] = unset,
        **kwargs,
    ):
        """
        Information about the mute status of this finding.

        :param description: Additional information about the reason why this finding is muted or unmuted.
            This attribute will not be included in the response if the description is not provided in the request body.
        :type description: str, optional

        :param expiration_date: The expiration date of the mute or unmute action.
            If the expiration date is not provided in the request body, this attribute will not be included in the response and the finding will be muted or unmuted indefinitely.
        :type expiration_date: int, optional

        :param muted: Whether this finding is muted or unmuted.
        :type muted: bool, optional

        :param reason: The reason why this finding is muted or unmuted.
        :type reason: FindingMuteReason, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if expiration_date is not unset:
            kwargs["expiration_date"] = expiration_date
        if muted is not unset:
            kwargs["muted"] = muted
        if reason is not unset:
            kwargs["reason"] = reason
        super().__init__(kwargs)
