# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class OverrideCreateDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "end": (datetime,),
            "start": (datetime,),
        }

    attribute_map = {
        "end": "end",
        "start": "start",
    }

    def __init__(self_, end: datetime, start: datetime, **kwargs):
        """
        The definition of ``OverrideCreateDataAttributes`` object.

        :param end: The end time of the override.
        :type end: datetime

        :param start: The start time of the override.
        :type start: datetime
        """
        super().__init__(kwargs)

        self_.end = end
        self_.start = start
