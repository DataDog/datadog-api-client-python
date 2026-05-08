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
    from datadog_api_client.v2.model.replay_summary_data_attributes_response import ReplaySummaryDataAttributesResponse
    from datadog_api_client.v2.model.replay_summary_response_type import ReplaySummaryResponseType


class ReplaySummaryDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.replay_summary_data_attributes_response import (
            ReplaySummaryDataAttributesResponse,
        )
        from datadog_api_client.v2.model.replay_summary_response_type import ReplaySummaryResponseType

        return {
            "attributes": (ReplaySummaryDataAttributesResponse,),
            "id": (str,),
            "type": (ReplaySummaryResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: ReplaySummaryDataAttributesResponse, id: str, type: ReplaySummaryResponseType, **kwargs
    ):
        """
        Data object for a RUM replay summary response.

        :param attributes: Attributes of a RUM replay summary response.
        :type attributes: ReplaySummaryDataAttributesResponse

        :param id: Unique identifier of the generated summary.
        :type id: str

        :param type: RUM replay summary response resource type.
        :type type: ReplaySummaryResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
