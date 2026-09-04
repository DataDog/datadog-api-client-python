# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TimeseriesAnomalyInvestigationFindingSynonym(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "key": (str,),
            "values": ([str],),
        }

    attribute_map = {
        "key": "key",
        "values": "values",
    }

    def __init__(self_, key: str, values: List[str], **kwargs):
        """
        Tag grouped under an influential tag by synonym analysis.

        :param key: Synonymous tag key.
        :type key: str

        :param values: Values associated with the synonymous tag.
        :type values: [str]
        """
        super().__init__(kwargs)

        self_.key = key
        self_.values = values
