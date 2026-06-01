# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_org_settings_meta import IncidentOrgSettingsMeta


class IncidentOrgSettingsDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_org_settings_meta import IncidentOrgSettingsMeta

        return {
            "created": (datetime,),
            "modified": (datetime,),
            "settings": (IncidentOrgSettingsMeta,),
        }

    attribute_map = {
        "created": "created",
        "modified": "modified",
        "settings": "settings",
    }

    def __init__(self_, created: datetime, modified: datetime, settings: IncidentOrgSettingsMeta, **kwargs):
        """
        Attributes of an incident org settings resource in a response.

        :param created: Timestamp when the settings were created.
        :type created: datetime

        :param modified: Timestamp when the settings were last modified.
        :type modified: datetime

        :param settings: The settings configuration for an incident org settings resource.
        :type settings: IncidentOrgSettingsMeta
        """
        super().__init__(kwargs)

        self_.created = created
        self_.modified = modified
        self_.settings = settings
