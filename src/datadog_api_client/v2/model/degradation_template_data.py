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
    from datadog_api_client.v2.model.degradation_template_data_attributes import DegradationTemplateDataAttributes
    from datadog_api_client.v2.model.degradation_template_data_relationships import DegradationTemplateDataRelationships
    from datadog_api_client.v2.model.patch_degradation_template_request_data_type import (
        PatchDegradationTemplateRequestDataType,
    )


class DegradationTemplateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.degradation_template_data_attributes import DegradationTemplateDataAttributes
        from datadog_api_client.v2.model.degradation_template_data_relationships import (
            DegradationTemplateDataRelationships,
        )
        from datadog_api_client.v2.model.patch_degradation_template_request_data_type import (
            PatchDegradationTemplateRequestDataType,
        )

        return {
            "attributes": (DegradationTemplateDataAttributes,),
            "id": (str,),
            "relationships": (DegradationTemplateDataRelationships,),
            "type": (PatchDegradationTemplateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: PatchDegradationTemplateRequestDataType,
        attributes: Union[DegradationTemplateDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[DegradationTemplateDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object for a degradation template.

        :param attributes: The attributes of a degradation template.
        :type attributes: DegradationTemplateDataAttributes, optional

        :param id: The ID of the degradation template.
        :type id: str, optional

        :param relationships: The relationships of a degradation template.
        :type relationships: DegradationTemplateDataRelationships, optional

        :param type: Degradation templates resource type.
        :type type: PatchDegradationTemplateRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
