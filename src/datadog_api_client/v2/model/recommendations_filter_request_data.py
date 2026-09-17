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
    from datadog_api_client.v2.model.recommendations_filter_request_data_attributes import (
        RecommendationsFilterRequestDataAttributes,
    )
    from datadog_api_client.v2.model.recommendations_filter_request_data_type import (
        RecommendationsFilterRequestDataType,
    )


class RecommendationsFilterRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.recommendations_filter_request_data_attributes import (
            RecommendationsFilterRequestDataAttributes,
        )
        from datadog_api_client.v2.model.recommendations_filter_request_data_type import (
            RecommendationsFilterRequestDataType,
        )

        return {
            "attributes": (RecommendationsFilterRequestDataAttributes,),
            "id": (str,),
            "type": (RecommendationsFilterRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: RecommendationsFilterRequestDataType,
        attributes: Union[RecommendationsFilterRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API resource containing the cost recommendations filter. This legacy search contract
        uses the resource ID for the filter expression rather than as a persistent resource identifier.

        :param attributes: Attributes used to filter and sort cost recommendations.
        :type attributes: RecommendationsFilterRequestDataAttributes, optional

        :param id: Filter expression applied to the recommendations. The server treats an omitted ID as ``*``
            and returns all recommendations.
        :type id: str, optional

        :param type: Legacy JSON:API resource type required by the cost recommendations search decoder.
        :type type: RecommendationsFilterRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
