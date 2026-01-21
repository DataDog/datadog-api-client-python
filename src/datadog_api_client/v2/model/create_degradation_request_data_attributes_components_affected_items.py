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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.status_pages_component_data_attributes_status import (
        StatusPagesComponentDataAttributesStatus,
    )


class CreateDegradationRequestDataAttributesComponentsAffectedItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_pages_component_data_attributes_status import (
            StatusPagesComponentDataAttributesStatus,
        )

        return {
            "id": (UUID,),
            "name": (str,),
            "status": (StatusPagesComponentDataAttributesStatus,),
        }

    attribute_map = {
        "id": "id",
        "name": "name",
        "status": "status",
    }
    read_only_vars = {
        "name",
    }

    def __init__(
        self_, id: UUID, status: StatusPagesComponentDataAttributesStatus, name: Union[str, UnsetType] = unset, **kwargs
    ):
        """


        :param id: The ID of the component. Must be a component of type ``component``.
        :type id: UUID

        :param name:
        :type name: str, optional

        :param status: The status of the component.
        :type status: StatusPagesComponentDataAttributesStatus
        """
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.id = id
        self_.status = status
