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
    from datadog_api_client.v2.model.scorecard_list_response_attributes import ScorecardListResponseAttributes
    from datadog_api_client.v2.model.scorecard_list_type import ScorecardListType


class ScorecardListResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.scorecard_list_response_attributes import ScorecardListResponseAttributes
        from datadog_api_client.v2.model.scorecard_list_type import ScorecardListType

        return {
            "attributes": (ScorecardListResponseAttributes,),
            "id": (str,),
            "type": (ScorecardListType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: ScorecardListResponseAttributes, id: str, type: ScorecardListType, **kwargs):
        """
        Scorecard data.

        :param attributes: Scorecard attributes.
        :type attributes: ScorecardListResponseAttributes

        :param id: The unique ID of the scorecard.
        :type id: str

        :param type: The JSON:API type for scorecard list.
        :type type: ScorecardListType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
