# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ownership_confidence_level import OwnershipConfidenceLevel


class OwnershipSettingsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ownership_confidence_level import OwnershipConfidenceLevel

        return {
            "auto_tag": (bool,),
            "confidence_level": (OwnershipConfidenceLevel,),
            "version": (int,),
        }

    attribute_map = {
        "auto_tag": "auto_tag",
        "confidence_level": "confidence_level",
        "version": "version",
    }

    def __init__(self_, auto_tag: bool, confidence_level: OwnershipConfidenceLevel, version: int, **kwargs):
        """
        The attributes of the ownership settings response.

        :param auto_tag: Whether automatic ownership tagging is enabled.
        :type auto_tag: bool

        :param confidence_level: The ownership confidence level.
        :type confidence_level: OwnershipConfidenceLevel

        :param version: The current version of the ownership settings.
        :type version: int
        """
        super().__init__(kwargs)

        self_.auto_tag = auto_tag
        self_.confidence_level = confidence_level
        self_.version = version
