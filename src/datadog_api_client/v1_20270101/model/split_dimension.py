# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SplitDimension(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "one_graph_per": (str,),
        }

    attribute_map = {
        "one_graph_per": "one_graph_per",
    }

    def __init__(self_, one_graph_per: str, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param one_graph_per: Test-only generated schema for the dashboard versioning proof of concept.
        :type one_graph_per: str
        """
        super().__init__(kwargs)

        self_.one_graph_per = one_graph_per
