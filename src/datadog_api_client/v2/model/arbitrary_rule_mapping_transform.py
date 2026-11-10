# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class ArbitraryRuleMappingTransform(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "mapping": (
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
            "synthetic_tag": (str,),
        }

    attribute_map = {
        "mapping": "mapping",
        "synthetic_tag": "synthetic_tag",
    }

    def __init__(self_, mapping: Dict[str, Any], synthetic_tag: str, **kwargs):
        """
        Only supported for ``proportional_timeseries`` and ``even_timeseries`` rules. Creates a synthetic tag from timeseries input rows before ``tag_transforms`` are applied.

        :param mapping: Recursive mapping node. Each ``match_on_values`` branch contains a value and a nested node.
        :type mapping: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}

        :param synthetic_tag: The name of the synthetic tag created by the mapping.
        :type synthetic_tag: str
        """
        super().__init__(kwargs)

        self_.mapping = mapping
        self_.synthetic_tag = synthetic_tag
