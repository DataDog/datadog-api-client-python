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
    from datadog_api_client.v2.model.analysis_response_data_attributes import AnalysisResponseDataAttributes
    from datadog_api_client.v2.model.analysis_response_data_type import AnalysisResponseDataType


class AnalysisResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.analysis_response_data_attributes import AnalysisResponseDataAttributes
        from datadog_api_client.v2.model.analysis_response_data_type import AnalysisResponseDataType

        return {
            "attributes": (AnalysisResponseDataAttributes,),
            "id": (str,),
            "type": (AnalysisResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AnalysisResponseDataAttributes, id: str, type: AnalysisResponseDataType, **kwargs):
        """
        The primary data object in the analysis response.

        :param attributes: The attributes of the analysis response, containing rule results and any top-level errors.
        :type attributes: AnalysisResponseDataAttributes

        :param id: The unique identifier of the analysis response resource.
        :type id: str

        :param type: Analysis response resource type.
        :type type: AnalysisResponseDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
