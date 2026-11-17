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


class ProductAnalyticsFunnelStepSuggestionsResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "steps": ([str],),
        }

    attribute_map = {
        "steps": "steps",
    }

    def __init__(self_, steps: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Attributes of a step suggestions response.

        :param steps: Event queries of the suggested next steps, most relevant first.
        :type steps: [str], optional
        """
        if steps is not unset:
            kwargs["steps"] = steps
        super().__init__(kwargs)
