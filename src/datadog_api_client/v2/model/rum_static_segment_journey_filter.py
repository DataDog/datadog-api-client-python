# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RumStaticSegmentJourneyFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "attribute": (str,),
            "value": (str,),
        }

    attribute_map = {
        "attribute": "attribute",
        "value": "value",
    }

    def __init__(self_, attribute: str, value: str, **kwargs):
        """
        A filter within a journey query node.

        :param attribute: The attribute to filter on.
        :type attribute: str

        :param value: The value to match.
        :type value: str
        """
        super().__init__(kwargs)

        self_.attribute = attribute
        self_.value = value
