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
    from datadog_api_client.v2.model.usage_attribution_types_attributes import UsageAttributionTypesAttributes
    from datadog_api_client.v2.model.usage_attribution_types_type import UsageAttributionTypesType


class UsageAttributionTypesBody(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_attribution_types_attributes import UsageAttributionTypesAttributes
        from datadog_api_client.v2.model.usage_attribution_types_type import UsageAttributionTypesType

        return {
            "attributes": (UsageAttributionTypesAttributes,),
            "id": (str,),
            "type": (UsageAttributionTypesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[UsageAttributionTypesAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[UsageAttributionTypesType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Usage attribution types data.

        :param attributes: List of usage attribution types.
        :type attributes: UsageAttributionTypesAttributes, optional

        :param id: Unique ID of the response.
        :type id: str, optional

        :param type: Type of usage attribution types data.
        :type type: UsageAttributionTypesType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
