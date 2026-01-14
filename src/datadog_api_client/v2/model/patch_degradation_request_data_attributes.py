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
    from datadog_api_client.v2.model.patch_degradation_request_data_attributes_components_affected_items import (
        PatchDegradationRequestDataAttributesComponentsAffectedItems,
    )
    from datadog_api_client.v2.model.patch_degradation_request_data_attributes_status import (
        PatchDegradationRequestDataAttributesStatus,
    )


class PatchDegradationRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_degradation_request_data_attributes_components_affected_items import (
            PatchDegradationRequestDataAttributesComponentsAffectedItems,
        )
        from datadog_api_client.v2.model.patch_degradation_request_data_attributes_status import (
            PatchDegradationRequestDataAttributesStatus,
        )

        return {
            "components_affected": ([PatchDegradationRequestDataAttributesComponentsAffectedItems],),
            "description": (str,),
            "status": (PatchDegradationRequestDataAttributesStatus,),
            "title": (str,),
        }

    attribute_map = {
        "components_affected": "components_affected",
        "description": "description",
        "status": "status",
        "title": "title",
    }

    def __init__(
        self_,
        components_affected: Union[
            List[PatchDegradationRequestDataAttributesComponentsAffectedItems], UnsetType
        ] = unset,
        description: Union[str, UnsetType] = unset,
        status: Union[PatchDegradationRequestDataAttributesStatus, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The supported attributes for updating a degradation.

        :param components_affected: The components affected by the degradation.
        :type components_affected: [PatchDegradationRequestDataAttributesComponentsAffectedItems], optional

        :param description: The description of the degradation.
        :type description: str, optional

        :param status: The status of the degradation.
        :type status: PatchDegradationRequestDataAttributesStatus, optional

        :param title: The title of the degradation.
        :type title: str, optional
        """
        if components_affected is not unset:
            kwargs["components_affected"] = components_affected
        if description is not unset:
            kwargs["description"] = description
        if status is not unset:
            kwargs["status"] = status
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
