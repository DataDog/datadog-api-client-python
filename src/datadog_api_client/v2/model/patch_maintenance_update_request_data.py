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
    from datadog_api_client.v2.model.patch_maintenance_update_request_data_attributes import (
        PatchMaintenanceUpdateRequestDataAttributes,
    )
    from datadog_api_client.v2.model.patch_maintenance_update_request_data_type import (
        PatchMaintenanceUpdateRequestDataType,
    )


class PatchMaintenanceUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_maintenance_update_request_data_attributes import (
            PatchMaintenanceUpdateRequestDataAttributes,
        )
        from datadog_api_client.v2.model.patch_maintenance_update_request_data_type import (
            PatchMaintenanceUpdateRequestDataType,
        )

        return {
            "attributes": (PatchMaintenanceUpdateRequestDataAttributes,),
            "id": (str,),
            "type": (PatchMaintenanceUpdateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: PatchMaintenanceUpdateRequestDataType,
        attributes: Union[PatchMaintenanceUpdateRequestDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object for editing a maintenance update.

        :param attributes: Attributes for editing a maintenance update.
        :type attributes: PatchMaintenanceUpdateRequestDataAttributes, optional

        :param id: The ID of the maintenance update to edit. Must match the ``update_id`` path parameter.
        :type id: str

        :param type: Maintenance updates resource type.
        :type type: PatchMaintenanceUpdateRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
