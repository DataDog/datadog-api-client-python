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


class SampledAnalysisQuerySample(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "limit": (float,),
        }

    attribute_map = {
        "limit": "limit",
    }

    def __init__(self_, limit: Union[float, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional
        """
        if limit is not unset:
            kwargs["limit"] = limit
        super().__init__(kwargs)
