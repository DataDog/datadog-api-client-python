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
    from datadog_api_client.v2.model.status_pages_component_group_attributes_components_items_status import (
        StatusPagesComponentGroupAttributesComponentsItemsStatus,
    )
    from datadog_api_client.v2.model.status_pages_component_group_attributes_components_items_type import (
        StatusPagesComponentGroupAttributesComponentsItemsType,
    )


class StatusPageAsIncludedAttributesComponentsItemsComponentsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_pages_component_group_attributes_components_items_status import (
            StatusPagesComponentGroupAttributesComponentsItemsStatus,
        )
        from datadog_api_client.v2.model.status_pages_component_group_attributes_components_items_type import (
            StatusPagesComponentGroupAttributesComponentsItemsType,
        )

        return {
            "id": (str,),
            "name": (str,),
            "position": (int,),
            "status": (StatusPagesComponentGroupAttributesComponentsItemsStatus,),
            "type": (StatusPagesComponentGroupAttributesComponentsItemsType,),
        }

    attribute_map = {
        "id": "id",
        "name": "name",
        "position": "position",
        "status": "status",
        "type": "type",
    }
    read_only_vars = {
        "id",
        "status",
    }

    def __init__(
        self_,
        id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        position: Union[int, UnsetType] = unset,
        status: Union[StatusPagesComponentGroupAttributesComponentsItemsStatus, UnsetType] = unset,
        type: Union[StatusPagesComponentGroupAttributesComponentsItemsType, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param id:
        :type id: str, optional

        :param name:
        :type name: str, optional

        :param position:
        :type position: int, optional

        :param status:
        :type status: StatusPagesComponentGroupAttributesComponentsItemsStatus, optional

        :param type:
        :type type: StatusPagesComponentGroupAttributesComponentsItemsType, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        if position is not unset:
            kwargs["position"] = position
        if status is not unset:
            kwargs["status"] = status
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
