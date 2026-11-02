# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class JourneyMapTarget(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "end": (str,),
            "start": (str,),
        }

    attribute_map = {
        "end": "end",
        "start": "start",
    }

    def __init__(self_, end: str, start: str, **kwargs):
        """
        The pair of journey steps the paths are visualized between.

        :param end: Key of the end step in ``search.node_objects``.
        :type end: str

        :param start: Key of the start step in ``search.node_objects``.
        :type start: str
        """
        super().__init__(kwargs)

        self_.end = end
        self_.start = start
