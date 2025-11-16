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
    from datadog_api_client.v2.model.funnel_response_data_attributes import FunnelResponseDataAttributes
    from datadog_api_client.v2.model.funnel_response_data_type import FunnelResponseDataType


class FunnelResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.funnel_response_data_attributes import FunnelResponseDataAttributes
        from datadog_api_client.v2.model.funnel_response_data_type import FunnelResponseDataType

        return {
            "attributes": (FunnelResponseDataAttributes,),
            "id": (str,),
            "type": (FunnelResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: FunnelResponseDataType,
        attributes: Union[FunnelResponseDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: FunnelResponseDataAttributes, optional

        :param id:
        :type id: str, optional

        :param type:
        :type type: FunnelResponseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
