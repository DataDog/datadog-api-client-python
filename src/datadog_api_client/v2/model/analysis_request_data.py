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
    from datadog_api_client.v2.model.analysis_request_data_attributes import AnalysisRequestDataAttributes
    from datadog_api_client.v2.model.analysis_request_data_type import AnalysisRequestDataType


class AnalysisRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.analysis_request_data_attributes import AnalysisRequestDataAttributes
        from datadog_api_client.v2.model.analysis_request_data_type import AnalysisRequestDataType

        return {
            "attributes": (AnalysisRequestDataAttributes,),
            "id": (str,),
            "type": (AnalysisRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AnalysisRequestDataAttributes,
        type: AnalysisRequestDataType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The primary data object in the analysis request.

        :param attributes: The attributes of the analysis request, containing the source code and rules to apply.
        :type attributes: AnalysisRequestDataAttributes

        :param id: An optional identifier for the analysis request resource.
        :type id: str, optional

        :param type: Analysis request resource type.
        :type type: AnalysisRequestDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
