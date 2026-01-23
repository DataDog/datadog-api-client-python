# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class GlobalIncidentSettingsAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "analytics_dashboard_id": (str,),
            "created": (datetime,),
            "modified": (datetime,),
        }

    attribute_map = {
        "analytics_dashboard_id": "analytics_dashboard_id",
        "created": "created",
        "modified": "modified",
    }

    def __init__(self_, analytics_dashboard_id: str, created: datetime, modified: datetime, **kwargs):
        """
        Global incident settings attributes

        :param analytics_dashboard_id: The analytics dashboard ID
        :type analytics_dashboard_id: str

        :param created: Timestamp when the settings were created
        :type created: datetime

        :param modified: Timestamp when the settings were last modified
        :type modified: datetime
        """
        super().__init__(kwargs)

        self_.analytics_dashboard_id = analytics_dashboard_id
        self_.created = created
        self_.modified = modified
