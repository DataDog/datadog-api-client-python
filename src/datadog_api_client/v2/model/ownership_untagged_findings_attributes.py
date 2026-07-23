# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OwnershipUntaggedFindingsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "high_confidence": (int,),
            "low_confidence": (int,),
            "medium_confidence": (int,),
            "total": (int,),
        }

    attribute_map = {
        "high_confidence": "high_confidence",
        "low_confidence": "low_confidence",
        "medium_confidence": "medium_confidence",
        "total": "total",
    }

    def __init__(self_, high_confidence: int, low_confidence: int, medium_confidence: int, total: int, **kwargs):
        """
        The counts of findings without a team tag by ownership confidence.

        :param high_confidence: The number of high confidence findings without a team tag.
        :type high_confidence: int

        :param low_confidence: The number of low confidence findings without a team tag.
        :type low_confidence: int

        :param medium_confidence: The number of medium confidence findings without a team tag.
        :type medium_confidence: int

        :param total: The total number of findings without a team tag.
        :type total: int
        """
        super().__init__(kwargs)

        self_.high_confidence = high_confidence
        self_.low_confidence = low_confidence
        self_.medium_confidence = medium_confidence
        self_.total = total
