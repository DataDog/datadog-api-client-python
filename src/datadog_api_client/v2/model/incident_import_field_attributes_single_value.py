# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class IncidentImportFieldAttributesSingleValue(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "value": (str, none_type),
        }

    attribute_map = {
        "value": "value",
    }

    def __init__(self_, value: Union[str, none_type, UnsetType] = unset, **kwargs):
        """
        A field with a single value selected.

        :param value: The single value selected for this field.
        :type value: str, none_type, optional
        """
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
