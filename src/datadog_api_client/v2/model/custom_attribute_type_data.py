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
    from datadog_api_client.v2.model.custom_attribute_select_option import CustomAttributeSelectOption


class CustomAttributeTypeData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_attribute_select_option import CustomAttributeSelectOption

        return {
            "options": ([CustomAttributeSelectOption],),
        }

    attribute_map = {
        "options": "options",
    }

    def __init__(self_, options: Union[List[CustomAttributeSelectOption], UnsetType] = unset, **kwargs):
        """
        Type-specific configuration for the custom attribute. For SELECT-type attributes, this contains the list of allowed options.

        :param options: Options for SELECT type custom attributes.
        :type options: [CustomAttributeSelectOption], optional
        """
        if options is not unset:
            kwargs["options"] = options
        super().__init__(kwargs)
