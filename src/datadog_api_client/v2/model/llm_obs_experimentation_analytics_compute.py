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


class LLMObsExperimentationAnalyticsCompute(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "metric": (str,),
            "name": (str,),
        }

    attribute_map = {
        "metric": "metric",
        "name": "name",
    }

    def __init__(self_, metric: str, name: Union[str, UnsetType] = unset, **kwargs):
        """
        A single metric computation definition.

        :param metric: Name of the metric to compute.
        :type metric: str

        :param name: Optional alias for this computation in the response.
        :type name: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.metric = metric
