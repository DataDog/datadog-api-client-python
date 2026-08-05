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
    from datadog_api_client.v2.model.patch_degradation_template_request_data_attributes_components_affected_items import (
        PatchDegradationTemplateRequestDataAttributesComponentsAffectedItems,
    )
    from datadog_api_client.v2.model.patch_degradation_template_request_data_attributes_updates_items import (
        PatchDegradationTemplateRequestDataAttributesUpdatesItems,
    )


class PatchDegradationTemplateRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_degradation_template_request_data_attributes_components_affected_items import (
            PatchDegradationTemplateRequestDataAttributesComponentsAffectedItems,
        )
        from datadog_api_client.v2.model.patch_degradation_template_request_data_attributes_updates_items import (
            PatchDegradationTemplateRequestDataAttributesUpdatesItems,
        )

        return {
            "components_affected": ([PatchDegradationTemplateRequestDataAttributesComponentsAffectedItems],),
            "degradation_title": (str,),
            "name": (str,),
            "updates": ([PatchDegradationTemplateRequestDataAttributesUpdatesItems],),
        }

    attribute_map = {
        "components_affected": "components_affected",
        "degradation_title": "degradation_title",
        "name": "name",
        "updates": "updates",
    }

    def __init__(
        self_,
        components_affected: Union[
            List[PatchDegradationTemplateRequestDataAttributesComponentsAffectedItems], UnsetType
        ] = unset,
        degradation_title: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        updates: Union[List[PatchDegradationTemplateRequestDataAttributesUpdatesItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        The supported attributes for updating a degradation template.

        :param components_affected: The components affected by a degradation created from this template.
        :type components_affected: [PatchDegradationTemplateRequestDataAttributesComponentsAffectedItems], optional

        :param degradation_title: The title used for a degradation created from this template.
        :type degradation_title: str, optional

        :param name: The name of the degradation template.
        :type name: str, optional

        :param updates: The pre-filled updates for a degradation created from this template.
        :type updates: [PatchDegradationTemplateRequestDataAttributesUpdatesItems], optional
        """
        if components_affected is not unset:
            kwargs["components_affected"] = components_affected
        if degradation_title is not unset:
            kwargs["degradation_title"] = degradation_title
        if name is not unset:
            kwargs["name"] = name
        if updates is not unset:
            kwargs["updates"] = updates
        super().__init__(kwargs)
