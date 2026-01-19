# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class WebIntegrationAccountCreateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "secrets": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "settings": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
        }

    attribute_map = {
        "name": "name",
        "secrets": "secrets",
        "settings": "settings",
    }

    def __init__(self_, name: str, secrets: Dict[str, Any], settings: Dict[str, Any], **kwargs):
        """
        Attributes for creating a web integration account.

        :param name: The name of the account.
        :type name: str

        :param secrets: Sensitive credentials for the account. The structure and required fields vary by integration type.
            These values are write-only and never returned in responses. Use the schema endpoint to determine
            which secret fields are required for your specific integration.
        :type secrets: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}

        :param settings: Integration-specific settings for the account. The structure and required fields vary by integration type.
            Use the schema endpoint (GET /api/v2/web-integrations/{integration_name}/accounts/schema) to retrieve
            the specific requirements for your integration before creating an account.
        :type settings: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}
        """
        super().__init__(kwargs)

        self_.name = name
        self_.secrets = secrets
        self_.settings = settings
