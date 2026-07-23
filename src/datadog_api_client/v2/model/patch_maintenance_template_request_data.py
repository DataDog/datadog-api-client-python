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
    from datadog_api_client.v2.model.patch_maintenance_template_request_data_attributes import (
        PatchMaintenanceTemplateRequestDataAttributes,
    )
    from datadog_api_client.v2.model.patch_maintenance_template_request_data_type import (
        PatchMaintenanceTemplateRequestDataType,
    )


class PatchMaintenanceTemplateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_maintenance_template_request_data_attributes import (
            PatchMaintenanceTemplateRequestDataAttributes,
        )
        from datadog_api_client.v2.model.patch_maintenance_template_request_data_type import (
            PatchMaintenanceTemplateRequestDataType,
        )

        return {
            "attributes": (PatchMaintenanceTemplateRequestDataAttributes,),
            "id": (str,),
            "type": (PatchMaintenanceTemplateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: PatchMaintenanceTemplateRequestDataType,
        attributes: Union[PatchMaintenanceTemplateRequestDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object for updating a maintenance template.

        :param attributes: The supported attributes for updating a maintenance template.
        :type attributes: PatchMaintenanceTemplateRequestDataAttributes, optional

        :param id: The ID of the maintenance template.
        :type id: str

        :param type: Maintenance templates resource type.
        :type type: PatchMaintenanceTemplateRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
