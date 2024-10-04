# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MSTeamsIntegrationMetadataTeamsItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "ms_channel_id": (str,),
            "ms_channel_name": (str,),
            "ms_tenant_id": (str,),
            "redirect_url": (str,),
        }

    attribute_map = {
        "ms_channel_id": "ms_channel_id",
        "ms_channel_name": "ms_channel_name",
        "ms_tenant_id": "ms_tenant_id",
        "redirect_url": "redirect_url",
    }

    def __init__(self_, ms_channel_id: str, ms_channel_name: str, ms_tenant_id: str, redirect_url: str, **kwargs):
        """
        Item in the Microsoft Teams integration metadata teams array.

        :param ms_channel_id: Microsoft Teams channel ID.
        :type ms_channel_id: str

        :param ms_channel_name: Microsoft Teams channel name.
        :type ms_channel_name: str

        :param ms_tenant_id: Microsoft Teams tenant ID.
        :type ms_tenant_id: str

        :param redirect_url: URL redirecting to the Microsoft Teams channel.
        :type redirect_url: str
        """
        super().__init__(kwargs)

        self_.ms_channel_id = ms_channel_id
        self_.ms_channel_name = ms_channel_name
        self_.ms_tenant_id = ms_tenant_id
        self_.redirect_url = redirect_url
