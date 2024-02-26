# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MicrosoftTeamsIntegrationMetadataTeamsItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "ms_team_id": (str,),
            "ms_tenant_id": (str,),
            "redirect_url": (str,),
            "team_name": (str,),
        }

    attribute_map = {
        "ms_team_id": "ms_team_id",
        "ms_tenant_id": "ms_tenant_id",
        "redirect_url": "redirect_url",
        "team_name": "team_name",
    }

    def __init__(self_, ms_team_id: str, ms_tenant_id: str, redirect_url: str, team_name: str, **kwargs):
        """
        Item in the Microsoft Teams integration metadata teams array.

        :param ms_team_id: Team ID of the Microsoft Teams team
        :type ms_team_id: str

        :param ms_tenant_id: Microsoft Teams tenant ID
        :type ms_tenant_id: str

        :param redirect_url: URL redirecting to the Microsoft Teams team
        :type redirect_url: str

        :param team_name: Name of the Microsoft Teams team
        :type team_name: str
        """
        super().__init__(kwargs)

        self_.ms_team_id = ms_team_id
        self_.ms_tenant_id = ms_tenant_id
        self_.redirect_url = redirect_url
        self_.team_name = team_name
