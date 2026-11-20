# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class PowerpackBackendTemplateVariable(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "prefix": (str,),
            "values": ([str],),
        }

    attribute_map = {
        "name": "name",
        "prefix": "prefix",
        "values": "values",
    }

    def __init__(self_, name: str, values: List[str], prefix: Union[str, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param prefix: Test-only generated schema for the dashboard versioning proof of concept.
        :type prefix: str, optional

        :param values: Test-only generated schema for the dashboard versioning proof of concept.
        :type values: [str]
        """
        if prefix is not unset:
            kwargs["prefix"] = prefix
        super().__init__(kwargs)

        self_.name = name
        self_.values = values
