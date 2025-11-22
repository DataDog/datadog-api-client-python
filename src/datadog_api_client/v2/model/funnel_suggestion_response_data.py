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
    from datadog_api_client.v2.model.funnel_suggestion_response_data_attributes import (
        FunnelSuggestionResponseDataAttributes,
    )
    from datadog_api_client.v2.model.funnel_suggestion_response_data_type import FunnelSuggestionResponseDataType


class FunnelSuggestionResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.funnel_suggestion_response_data_attributes import (
            FunnelSuggestionResponseDataAttributes,
        )
        from datadog_api_client.v2.model.funnel_suggestion_response_data_type import FunnelSuggestionResponseDataType

        return {
            "attributes": (FunnelSuggestionResponseDataAttributes,),
            "id": (str,),
            "type": (FunnelSuggestionResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: FunnelSuggestionResponseDataType,
        attributes: Union[FunnelSuggestionResponseDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: FunnelSuggestionResponseDataAttributes, optional

        :param id:
        :type id: str, optional

        :param type:
        :type type: FunnelSuggestionResponseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
