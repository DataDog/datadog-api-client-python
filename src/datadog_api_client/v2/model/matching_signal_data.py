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
    from datadog_api_client.v2.model.matching_signal_attributes import MatchingSignalAttributes
    from datadog_api_client.v2.model.matching_signal_type import MatchingSignalType


class MatchingSignalData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.matching_signal_attributes import MatchingSignalAttributes
        from datadog_api_client.v2.model.matching_signal_type import MatchingSignalType

        return {
            "attributes": (MatchingSignalAttributes,),
            "id": (str,),
            "type": (MatchingSignalType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: MatchingSignalAttributes, id: str, type: MatchingSignalType, **kwargs):
        """
        A security signal that matches the queried event.

        :param attributes: Attributes of a matching security signal.
        :type attributes: MatchingSignalAttributes

        :param id: The ID of the matching signal.
        :type id: str

        :param type: The type of the resource. The value should always be ``matching_signal``.
        :type type: MatchingSignalType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
