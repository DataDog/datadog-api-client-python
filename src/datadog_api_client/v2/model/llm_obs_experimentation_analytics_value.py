# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class LLMObsExperimentationAnalyticsValue(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "by": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "metrics": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
        }

    attribute_map = {
        "by": "by",
        "metrics": "metrics",
    }

    def __init__(self_, metrics: Dict[str, Any], by: Union[Dict[str, Any], UnsetType] = unset, **kwargs):
        """
        A single analytics result bucket.

        :param by: The group-by field values for this bucket.
        :type by: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param metrics: Computed metric values for this bucket.
        :type metrics: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}
        """
        if by is not unset:
            kwargs["by"] = by
        super().__init__(kwargs)

        self_.metrics = metrics
