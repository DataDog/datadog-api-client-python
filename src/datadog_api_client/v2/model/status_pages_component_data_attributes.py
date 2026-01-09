# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.status_pages_component_data_attributes_components_items import (
        StatusPagesComponentDataAttributesComponentsItems,
    )
    from datadog_api_client.v2.model.status_pages_component_data_attributes_status import (
        StatusPagesComponentDataAttributesStatus,
    )
    from datadog_api_client.v2.model.create_component_request_data_attributes_type import (
        CreateComponentRequestDataAttributesType,
    )


class StatusPagesComponentDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_pages_component_data_attributes_components_items import (
            StatusPagesComponentDataAttributesComponentsItems,
        )
        from datadog_api_client.v2.model.status_pages_component_data_attributes_status import (
            StatusPagesComponentDataAttributesStatus,
        )
        from datadog_api_client.v2.model.create_component_request_data_attributes_type import (
            CreateComponentRequestDataAttributesType,
        )

        return {
            "components": ([StatusPagesComponentDataAttributesComponentsItems],),
            "created_at": (datetime,),
            "modified_at": (datetime,),
            "name": (str,),
            "position": (int,),
            "status": (StatusPagesComponentDataAttributesStatus,),
            "type": (CreateComponentRequestDataAttributesType,),
        }

    attribute_map = {
        "components": "components",
        "created_at": "created_at",
        "modified_at": "modified_at",
        "name": "name",
        "position": "position",
        "status": "status",
        "type": "type",
    }

    def __init__(
        self_,
        type: CreateComponentRequestDataAttributesType,
        components: Union[List[StatusPagesComponentDataAttributesComponentsItems], UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        position: Union[int, UnsetType] = unset,
        status: Union[StatusPagesComponentDataAttributesStatus, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param components:
        :type components: [StatusPagesComponentDataAttributesComponentsItems], optional

        :param created_at:
        :type created_at: datetime, optional

        :param modified_at:
        :type modified_at: datetime, optional

        :param name:
        :type name: str, optional

        :param position:
        :type position: int, optional

        :param status:
        :type status: StatusPagesComponentDataAttributesStatus, optional

        :param type:
        :type type: CreateComponentRequestDataAttributesType
        """
        if components is not unset:
            kwargs["components"] = components
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if name is not unset:
            kwargs["name"] = name
        if position is not unset:
            kwargs["position"] = position
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)

        self_.type = type
