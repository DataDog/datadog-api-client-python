# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ListColumn(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "alias": (str,),
            "name": (str,),
        }

    attribute_map = {
        "alias": "alias",
        "name": "name",
    }

    def __init__(self_, name: str, alias: Union[str, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str
        """
        if alias is not unset:
            kwargs["alias"] = alias
        super().__init__(kwargs)

        self_.name = name
