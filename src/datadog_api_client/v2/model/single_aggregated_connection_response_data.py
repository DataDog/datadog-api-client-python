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
    from datadog_api_client.v2.model.single_aggregated_connection_response_data_attributes import (
        SingleAggregatedConnectionResponseDataAttributes,
    )
    from datadog_api_client.v2.model.single_aggregated_connection_response_data_type import (
        SingleAggregatedConnectionResponseDataType,
    )


class SingleAggregatedConnectionResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.single_aggregated_connection_response_data_attributes import (
            SingleAggregatedConnectionResponseDataAttributes,
        )
        from datadog_api_client.v2.model.single_aggregated_connection_response_data_type import (
            SingleAggregatedConnectionResponseDataType,
        )

        return {
            "attributes": (SingleAggregatedConnectionResponseDataAttributes,),
            "id": (str,),
            "type": (SingleAggregatedConnectionResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SingleAggregatedConnectionResponseDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SingleAggregatedConnectionResponseDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object describing an aggregated connection.

        :param attributes: Attributes for an aggregated connection.
        :type attributes: SingleAggregatedConnectionResponseDataAttributes, optional

        :param id: A unique identifier for the aggregated connection based on the group by values.
        :type id: str, optional

        :param type: Aggregated connection resource type.
        :type type: SingleAggregatedConnectionResponseDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
