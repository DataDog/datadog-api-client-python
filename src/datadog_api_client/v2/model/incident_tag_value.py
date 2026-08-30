# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentTagValue(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "tag": (str,),
            "values": ([str],),
        }

    attribute_map = {
        "tag": "tag",
        "values": "values",
    }

    def __init__(self_, tag: str, values: List[str], **kwargs):
        """
        An incident tag and its accepted values.

        :param tag: The incident tag to match.
        :type tag: str

        :param values: The accepted values for the incident tag.
        :type values: [str]
        """
        super().__init__(kwargs)

        self_.tag = tag
        self_.values = values
