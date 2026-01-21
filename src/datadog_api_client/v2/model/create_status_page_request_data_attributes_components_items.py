# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_status_page_request_data_attributes_components_items_components_items import (
        CreateStatusPageRequestDataAttributesComponentsItemsComponentsItems,
    )
    from datadog_api_client.v2.model.status_pages_component_group_attributes_components_items_status import (
        StatusPagesComponentGroupAttributesComponentsItemsStatus,
    )
    from datadog_api_client.v2.model.create_component_request_data_attributes_type import (
        CreateComponentRequestDataAttributesType,
    )


class CreateStatusPageRequestDataAttributesComponentsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_status_page_request_data_attributes_components_items_components_items import (
            CreateStatusPageRequestDataAttributesComponentsItemsComponentsItems,
        )
        from datadog_api_client.v2.model.status_pages_component_group_attributes_components_items_status import (
            StatusPagesComponentGroupAttributesComponentsItemsStatus,
        )
        from datadog_api_client.v2.model.create_component_request_data_attributes_type import (
            CreateComponentRequestDataAttributesType,
        )

        return {
            "components": ([CreateStatusPageRequestDataAttributesComponentsItemsComponentsItems],),
            "id": (UUID,),
            "name": (str,),
            "position": (int,),
            "status": (StatusPagesComponentGroupAttributesComponentsItemsStatus,),
            "type": (CreateComponentRequestDataAttributesType,),
        }

    attribute_map = {
        "components": "components",
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
        components: Union[List[CreateStatusPageRequestDataAttributesComponentsItemsComponentsItems], UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        position: Union[int, UnsetType] = unset,
        status: Union[StatusPagesComponentGroupAttributesComponentsItemsStatus, UnsetType] = unset,
        type: Union[CreateComponentRequestDataAttributesType, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param components: If creating a component of type ``group`` , the components to create within the group.
        :type components: [CreateStatusPageRequestDataAttributesComponentsItemsComponentsItems], optional

        :param id: The ID of the component.
        :type id: UUID, optional

        :param name: The name of the component.
        :type name: str, optional

        :param position: The zero-indexed position of the component.
        :type position: int, optional

        :param status: The status of the component.
        :type status: StatusPagesComponentGroupAttributesComponentsItemsStatus, optional

        :param type: The type of the component.
        :type type: CreateComponentRequestDataAttributesType, optional
        """
        if components is not unset:
            kwargs["components"] = components
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
