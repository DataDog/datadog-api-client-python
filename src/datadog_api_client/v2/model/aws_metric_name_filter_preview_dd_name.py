# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSMetricNameFilterPreviewDDName(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "filtered": (bool,),
            "name": (str,),
        }

    attribute_map = {
        "filtered": "filtered",
        "name": "name",
    }

    def __init__(self_, filtered: bool, name: str, **kwargs):
        """
        A Datadog metric name and whether it is filtered.

        :param filtered: Whether this Datadog metric name is filtered out.
        :type filtered: bool

        :param name: The Datadog metric name.
        :type name: str
        """
        super().__init__(kwargs)

        self_.filtered = filtered
        self_.name = name
