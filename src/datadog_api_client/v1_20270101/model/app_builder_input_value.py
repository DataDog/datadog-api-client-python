# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.app_builder_input_value20270101_value import AppBuilderInputValue20270101Value


class AppBuilderInputValue(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.app_builder_input_value20270101_value import AppBuilderInputValue20270101Value

        return {
            "name": (str,),
            "value": (AppBuilderInputValue20270101Value,),
        }

    attribute_map = {
        "name": "name",
        "value": "value",
    }

    def __init__(self_, name: str, value: Union[AppBuilderInputValue20270101Value, str, float, bool], **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param value: Test-only generated schema for the dashboard versioning proof of concept.
        :type value: AppBuilderInputValue20270101Value
        """
        super().__init__(kwargs)

        self_.name = name
        self_.value = value
