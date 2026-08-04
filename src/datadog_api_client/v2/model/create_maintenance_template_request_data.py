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
    from datadog_api_client.v2.model.create_maintenance_template_request_data_attributes import (
        CreateMaintenanceTemplateRequestDataAttributes,
    )
    from datadog_api_client.v2.model.patch_maintenance_template_request_data_type import (
        PatchMaintenanceTemplateRequestDataType,
    )


class CreateMaintenanceTemplateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_maintenance_template_request_data_attributes import (
            CreateMaintenanceTemplateRequestDataAttributes,
        )
        from datadog_api_client.v2.model.patch_maintenance_template_request_data_type import (
            PatchMaintenanceTemplateRequestDataType,
        )

        return {
            "attributes": (CreateMaintenanceTemplateRequestDataAttributes,),
            "type": (PatchMaintenanceTemplateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: PatchMaintenanceTemplateRequestDataType,
        attributes: Union[CreateMaintenanceTemplateRequestDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object for creating a maintenance template.

        :param attributes: The attributes for creating a maintenance template.
        :type attributes: CreateMaintenanceTemplateRequestDataAttributes, optional

        :param type: Maintenance templates resource type.
        :type type: PatchMaintenanceTemplateRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
