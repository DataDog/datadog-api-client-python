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
    from datadog_api_client.v2.model.score_response_attributes import ScoreResponseAttributes
    from datadog_api_client.v2.model.score_type import ScoreType


class ScoreResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.score_response_attributes import ScoreResponseAttributes
        from datadog_api_client.v2.model.score_type import ScoreType

        return {
            "attributes": (ScoreResponseAttributes,),
            "id": (str,),
            "type": (ScoreType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: ScoreResponseAttributes, id: str, type: ScoreType, **kwargs):
        """
        Score data.

        :param attributes: Score attributes.
        :type attributes: ScoreResponseAttributes

        :param id: The unique ID of the score entity.
        :type id: str

        :param type: The JSON:API type for scores.
        :type type: ScoreType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
