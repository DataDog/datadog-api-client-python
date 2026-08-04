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
    from datadog_api_client.v2.model.patch_degradation_template_request_data_attributes_components_affected_items_status import (
        PatchDegradationTemplateRequestDataAttributesComponentsAffectedItemsStatus,
    )


class DegradationTemplateDataAttributesComponentsAffectedItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_degradation_template_request_data_attributes_components_affected_items_status import (
            PatchDegradationTemplateRequestDataAttributesComponentsAffectedItemsStatus,
        )

        return {
            "id": (str,),
            "name": (str,),
            "status": (PatchDegradationTemplateRequestDataAttributesComponentsAffectedItemsStatus,),
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
        self_,
        id: str,
        status: PatchDegradationTemplateRequestDataAttributesComponentsAffectedItemsStatus,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A component affected by a degradation created from this template.

        :param id: The ID of the component.
        :type id: str

        :param name: The name of the component.
        :type name: str, optional

        :param status: The status of the component.
        :type status: PatchDegradationTemplateRequestDataAttributesComponentsAffectedItemsStatus
        """
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.id = id
        self_.status = status
