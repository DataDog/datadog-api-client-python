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
    from datadog_api_client.v2.model.monthly_resource_attributes import MonthlyResourceAttributes
    from datadog_api_client.v2.model.monthly_resource_type import MonthlyResourceType


class MonthlyResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monthly_resource_attributes import MonthlyResourceAttributes
        from datadog_api_client.v2.model.monthly_resource_type import MonthlyResourceType

        return {
            "attributes": (MonthlyResourceAttributes,),
            "id": (str,),
            "type": (MonthlyResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[MonthlyResourceAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[MonthlyResourceType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A resource's usage for the requested billing dimension and month.

        :param attributes: Resource usage and organization details for the requested month.
        :type attributes: MonthlyResourceAttributes, optional

        :param id: Identifier for the resource usage record. Treat this value as opaque.
        :type id: str, optional

        :param type: Type of a monthly resource usage record.
        :type type: MonthlyResourceType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
