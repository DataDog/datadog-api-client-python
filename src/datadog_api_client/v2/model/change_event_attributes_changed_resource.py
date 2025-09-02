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
    from datadog_api_client.v2.model.change_event_attributes_changed_resource_type import (
        ChangeEventAttributesChangedResourceType,
    )


class ChangeEventAttributesChangedResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_event_attributes_changed_resource_type import (
            ChangeEventAttributesChangedResourceType,
        )

        return {
            "name": (str,),
            "type": (ChangeEventAttributesChangedResourceType,),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
    }

    def __init__(
        self_,
        name: Union[str, UnsetType] = unset,
        type: Union[ChangeEventAttributesChangedResourceType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A uniquely identified resource.

        :param name: The name of the changed resource.
        :type name: str, optional

        :param type: The type of the changed resource.
        :type type: ChangeEventAttributesChangedResourceType, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
