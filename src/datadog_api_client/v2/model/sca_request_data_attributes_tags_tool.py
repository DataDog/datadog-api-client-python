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
    from datadog_api_client.v2.model.sca_request_data_attributes_tags_tool_generator import (
        ScaRequestDataAttributesTagsToolGenerator,
    )


class ScaRequestDataAttributesTagsTool(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sca_request_data_attributes_tags_tool_generator import (
            ScaRequestDataAttributesTagsToolGenerator,
        )

        return {
            "generator": (ScaRequestDataAttributesTagsToolGenerator,),
        }

    attribute_map = {
        "generator": "generator",
    }

    def __init__(self_, generator: Union[ScaRequestDataAttributesTagsToolGenerator, UnsetType] = unset, **kwargs):
        """
        Tool metadata included in SCA tags.

        :param generator: Metadata about the tool that generated the SCA tags.
        :type generator: ScaRequestDataAttributesTagsToolGenerator, optional
        """
        if generator is not unset:
            kwargs["generator"] = generator
        super().__init__(kwargs)
