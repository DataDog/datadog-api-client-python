# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.number_format_unit_custom_type import NumberFormatUnitCustomType


class NumberFormatUnitCustom(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.number_format_unit_custom_type import NumberFormatUnitCustomType

        return {
            "label": (str,),
            "type": (NumberFormatUnitCustomType,),
        }

    attribute_map = {
        "label": "label",
        "type": "type",
    }

    def __init__(self_, label: str, type: NumberFormatUnitCustomType, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param label: Test-only generated schema for the dashboard versioning proof of concept.
        :type label: str

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: NumberFormatUnitCustomType
        """
        super().__init__(kwargs)

        self_.label = label
        self_.type = type
