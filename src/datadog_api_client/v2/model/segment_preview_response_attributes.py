# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class SegmentPreviewResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "hits": (
                [
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
                    }
                ],
            ),
            "total_rows": (int,),
        }

    attribute_map = {
        "hits": "hits",
        "total_rows": "total_rows",
    }

    def __init__(self_, hits: List[Dict[str, Any]], total_rows: int, **kwargs):
        """
        Members of the previewed segment.

        :param hits: Rows of the preview, each as a map of column names to values.
        :type hits: [{str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}]

        :param total_rows: Total number of entities in the segment.
        :type total_rows: int
        """
        super().__init__(kwargs)

        self_.hits = hits
        self_.total_rows = total_rows
