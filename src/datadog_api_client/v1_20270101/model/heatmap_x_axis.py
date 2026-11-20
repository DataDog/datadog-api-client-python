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


class HeatmapXAxis(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "num_buckets": (float,),
        }

    attribute_map = {
        "num_buckets": "num_buckets",
    }

    def __init__(self_, num_buckets: Union[float, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param num_buckets: Test-only generated schema for the dashboard versioning proof of concept.
        :type num_buckets: float, optional
        """
        if num_buckets is not unset:
            kwargs["num_buckets"] = num_buckets
        super().__init__(kwargs)
