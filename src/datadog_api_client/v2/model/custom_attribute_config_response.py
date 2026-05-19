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
    from datadog_api_client.v2.model.custom_attribute_config import CustomAttributeConfig


class CustomAttributeConfigResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_attribute_config import CustomAttributeConfig

        return {
            "data": (CustomAttributeConfig,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[CustomAttributeConfig, UnsetType] = unset, **kwargs):
        """
        Response containing a single custom attribute configuration.

        :param data: A custom attribute configuration that defines an organization-specific metadata field on cases. Custom attributes are scoped to a case type and can hold text, URLs, numbers, or predefined select options.
        :type data: CustomAttributeConfig, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
