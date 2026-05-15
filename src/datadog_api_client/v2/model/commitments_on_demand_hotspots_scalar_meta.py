# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CommitmentsOnDemandHotspotsScalarMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "on_demand_filters": (str,),
        }

    attribute_map = {
        "on_demand_filters": "on_demand_filters",
    }

    def __init__(self_, on_demand_filters: str, **kwargs):
        """
        Metadata for the on-demand hot-spots scalar response.

        :param on_demand_filters: Active on-demand filters applied to the response.
        :type on_demand_filters: str
        """
        super().__init__(kwargs)

        self_.on_demand_filters = on_demand_filters
