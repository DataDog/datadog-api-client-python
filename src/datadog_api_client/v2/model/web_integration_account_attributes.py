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


class WebIntegrationAccountAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
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
        "settings": "settings",
    }

    def __init__(self_, name: str, settings: Dict[str, Any], **kwargs):
        """
        Attributes for a web integration account.

        :param name: The name of the account.
        :type name: str

        :param settings: Integration-specific settings for the account. The structure and required fields vary by integration type.
            Use the schema endpoint to retrieve the specific requirements for each integration.
        :type settings: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}
        """
        super().__init__(kwargs)

        self_.name = name
        self_.settings = settings
