# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class McpCrossAppAccessIssuerUrlUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "issuer_url": (str,),
        }

    attribute_map = {
        "issuer_url": "issuer_url",
    }

    def __init__(self_, issuer_url: str, **kwargs):
        """
        Attributes for the MCP Cross-App Access issuer URL update request.

        :param issuer_url: The Okta OIDC issuer URL for MCP Cross-App Access, for example
            ``https://your-subdomain.okta.com``. Provide an empty string to unset
            the issuer URL and opt the organization out of MCP Cross-App Access.
        :type issuer_url: str
        """
        super().__init__(kwargs)

        self_.issuer_url = issuer_url
