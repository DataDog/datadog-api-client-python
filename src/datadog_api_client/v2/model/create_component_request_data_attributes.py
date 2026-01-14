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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_component_request_data_attributes_components_items import (
        CreateComponentRequestDataAttributesComponentsItems,
    )
    from datadog_api_client.v2.model.create_component_request_data_attributes_type import (
        CreateComponentRequestDataAttributesType,
    )


class CreateComponentRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_component_request_data_attributes_components_items import (
            CreateComponentRequestDataAttributesComponentsItems,
        )
        from datadog_api_client.v2.model.create_component_request_data_attributes_type import (
            CreateComponentRequestDataAttributesType,
        )

        return {
            "components": ([CreateComponentRequestDataAttributesComponentsItems],),
            "name": (str,),
            "position": (int,),
            "type": (CreateComponentRequestDataAttributesType,),
        }

    attribute_map = {
        "components": "components",
        "name": "name",
        "position": "position",
        "type": "type",
    }

    def __init__(
        self_,
        name: str,
        position: int,
        type: CreateComponentRequestDataAttributesType,
        components: Union[List[CreateComponentRequestDataAttributesComponentsItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        The supported attributes for creating a component.

        :param components: If creating a component of type ``group`` , the components to create within the group.
        :type components: [CreateComponentRequestDataAttributesComponentsItems], optional

        :param name: The name of the component.
        :type name: str

        :param position: The zero-indexed position of the component.
        :type position: int

        :param type: The type of the component.
        :type type: CreateComponentRequestDataAttributesType
        """
        if components is not unset:
            kwargs["components"] = components
        super().__init__(kwargs)

        self_.name = name
        self_.position = position
        self_.type = type
