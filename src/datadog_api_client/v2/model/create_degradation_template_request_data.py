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
    from datadog_api_client.v2.model.create_degradation_template_request_data_attributes import (
        CreateDegradationTemplateRequestDataAttributes,
    )
    from datadog_api_client.v2.model.patch_degradation_template_request_data_type import (
        PatchDegradationTemplateRequestDataType,
    )


class CreateDegradationTemplateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_degradation_template_request_data_attributes import (
            CreateDegradationTemplateRequestDataAttributes,
        )
        from datadog_api_client.v2.model.patch_degradation_template_request_data_type import (
            PatchDegradationTemplateRequestDataType,
        )

        return {
            "attributes": (CreateDegradationTemplateRequestDataAttributes,),
            "type": (PatchDegradationTemplateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: PatchDegradationTemplateRequestDataType,
        attributes: Union[CreateDegradationTemplateRequestDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object for creating a degradation template.

        :param attributes: The attributes for creating a degradation template.
        :type attributes: CreateDegradationTemplateRequestDataAttributes, optional

        :param type: Degradation templates resource type.
        :type type: PatchDegradationTemplateRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
