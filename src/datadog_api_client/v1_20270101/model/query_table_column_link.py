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


class QueryTableColumnLink(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "label": (str,),
            "url": (str,),
        }

    attribute_map = {
        "label": "label",
        "url": "url",
    }

    def __init__(self_, url: str, label: Union[str, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param label: Test-only generated schema for the dashboard versioning proof of concept.
        :type label: str, optional

        :param url: Test-only generated schema for the dashboard versioning proof of concept.
        :type url: str
        """
        if label is not unset:
            kwargs["label"] = label
        super().__init__(kwargs)

        self_.url = url
