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
    from datadog_api_client.v2.model.degradation_template_data_attributes_components_affected_items import (
        DegradationTemplateDataAttributesComponentsAffectedItems,
    )
    from datadog_api_client.v2.model.degradation_template_data_attributes_updates_items import (
        DegradationTemplateDataAttributesUpdatesItems,
    )


class DegradationTemplateDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.degradation_template_data_attributes_components_affected_items import (
            DegradationTemplateDataAttributesComponentsAffectedItems,
        )
        from datadog_api_client.v2.model.degradation_template_data_attributes_updates_items import (
            DegradationTemplateDataAttributesUpdatesItems,
        )

        return {
            "components_affected": ([DegradationTemplateDataAttributesComponentsAffectedItems],),
            "created_at": (datetime,),
            "degradation_title": (str,),
            "modified_at": (datetime,),
            "name": (str,),
            "updates": ([DegradationTemplateDataAttributesUpdatesItems],),
        }

    attribute_map = {
        "components_affected": "components_affected",
        "created_at": "created_at",
        "degradation_title": "degradation_title",
        "modified_at": "modified_at",
        "name": "name",
        "updates": "updates",
    }

    def __init__(
        self_,
        components_affected: Union[List[DegradationTemplateDataAttributesComponentsAffectedItems], UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        degradation_title: Union[str, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        updates: Union[List[DegradationTemplateDataAttributesUpdatesItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a degradation template.

        :param components_affected: The components affected by a degradation created from this template.
        :type components_affected: [DegradationTemplateDataAttributesComponentsAffectedItems], optional

        :param created_at: Timestamp of when the degradation template was created.
        :type created_at: datetime, optional

        :param degradation_title: The title used for a degradation created from this template.
        :type degradation_title: str, optional

        :param modified_at: Timestamp of when the degradation template was last modified.
        :type modified_at: datetime, optional

        :param name: The name of the degradation template.
        :type name: str, optional

        :param updates: The pre-filled updates for a degradation created from this template.
        :type updates: [DegradationTemplateDataAttributesUpdatesItems], optional
        """
        if components_affected is not unset:
            kwargs["components_affected"] = components_affected
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if degradation_title is not unset:
            kwargs["degradation_title"] = degradation_title
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if name is not unset:
            kwargs["name"] = name
        if updates is not unset:
            kwargs["updates"] = updates
        super().__init__(kwargs)
