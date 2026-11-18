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


class ProductAnalyticsLaunchFunnelStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "funnel_tile_def": (
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
                none_type,
            ),
        }

    attribute_map = {
        "funnel_tile_def": "funnel_tile_def",
    }

    def __init__(self_, funnel_tile_def: Union[Dict[str, Any], none_type, UnsetType] = unset, **kwargs):
        """
        Funnel linked to the launch.

        :param funnel_tile_def: Definition of the funnel widget, as a JSON object.
        :type funnel_tile_def: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional
        """
        if funnel_tile_def is not unset:
            kwargs["funnel_tile_def"] = funnel_tile_def
        super().__init__(kwargs)
