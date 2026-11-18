# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ProductAnalyticsLaunchKPI(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "title": (str,),
        }

    attribute_map = {
        "id": "id",
        "title": "title",
    }

    def __init__(self_, id: str, title: str, **kwargs):
        """
        A KPI that the launch is meant to move.

        :param id: ID of the KPI, unique within the launch. Tracking plan events reference it.
        :type id: str

        :param title: Name of the KPI.
        :type title: str
        """
        super().__init__(kwargs)

        self_.id = id
        self_.title = title
