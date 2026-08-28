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
    from datadog_api_client.v2.model.sca_request_data_attributes_tags_tool import ScaRequestDataAttributesTagsTool


class ScaRequestDataAttributesTags(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return (str,)

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sca_request_data_attributes_tags_tool import ScaRequestDataAttributesTagsTool

        return {
            "tool": (ScaRequestDataAttributesTagsTool,),
        }

    attribute_map = {
        "tool": "tool",
    }

    def __init__(self_, tool: Union[ScaRequestDataAttributesTagsTool, UnsetType] = unset, **kwargs):
        """
        A map of tags providing additional metadata for the SCA scan.

        :param tool: Tool metadata included in SCA tags.
        :type tool: ScaRequestDataAttributesTagsTool, optional
        """
        if tool is not unset:
            kwargs["tool"] = tool
        super().__init__(kwargs)
