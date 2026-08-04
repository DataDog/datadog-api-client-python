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
    from datadog_api_client.v2.model.create_degradation_template_request_data_attributes_components_affected_items import (
        CreateDegradationTemplateRequestDataAttributesComponentsAffectedItems,
    )
    from datadog_api_client.v2.model.create_degradation_template_request_data_attributes_updates_items import (
        CreateDegradationTemplateRequestDataAttributesUpdatesItems,
    )


class CreateDegradationTemplateRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_degradation_template_request_data_attributes_components_affected_items import (
            CreateDegradationTemplateRequestDataAttributesComponentsAffectedItems,
        )
        from datadog_api_client.v2.model.create_degradation_template_request_data_attributes_updates_items import (
            CreateDegradationTemplateRequestDataAttributesUpdatesItems,
        )

        return {
            "components_affected": ([CreateDegradationTemplateRequestDataAttributesComponentsAffectedItems],),
            "degradation_title": (str,),
            "name": (str,),
            "updates": ([CreateDegradationTemplateRequestDataAttributesUpdatesItems],),
        }

    attribute_map = {
        "components_affected": "components_affected",
        "degradation_title": "degradation_title",
        "name": "name",
        "updates": "updates",
    }

    def __init__(
        self_,
        name: str,
        components_affected: Union[
            List[CreateDegradationTemplateRequestDataAttributesComponentsAffectedItems], UnsetType
        ] = unset,
        degradation_title: Union[str, UnsetType] = unset,
        updates: Union[List[CreateDegradationTemplateRequestDataAttributesUpdatesItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes for creating a degradation template.

        :param components_affected: The components affected by a degradation created from this template.
        :type components_affected: [CreateDegradationTemplateRequestDataAttributesComponentsAffectedItems], optional

        :param degradation_title: The title used for a degradation created from this template.
        :type degradation_title: str, optional

        :param name: The name of the degradation template.
        :type name: str

        :param updates: The pre-filled updates for a degradation created from this template.
        :type updates: [CreateDegradationTemplateRequestDataAttributesUpdatesItems], optional
        """
        if components_affected is not unset:
            kwargs["components_affected"] = components_affected
        if degradation_title is not unset:
            kwargs["degradation_title"] = degradation_title
        if updates is not unset:
            kwargs["updates"] = updates
        super().__init__(kwargs)

        self_.name = name
