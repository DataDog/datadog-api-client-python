# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class VercelTokenCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "auth_grant_code": (str,),
            "vercel_configuration_id": (str,),
        }

    attribute_map = {
        "auth_grant_code": "authGrantCode",
        "vercel_configuration_id": "vercelConfigurationId",
    }

    def __init__(self_, auth_grant_code: str, vercel_configuration_id: str, **kwargs):
        """
        Request to exchange a Vercel marketplace authorization code for a Datadog-managed access token.

        :param auth_grant_code: OAuth authorization code received from the Vercel marketplace flow.
        :type auth_grant_code: str

        :param vercel_configuration_id: Vercel configuration identifier returned by the marketplace flow.
        :type vercel_configuration_id: str
        """
        super().__init__(kwargs)

        self_.auth_grant_code = auth_grant_code
        self_.vercel_configuration_id = vercel_configuration_id
