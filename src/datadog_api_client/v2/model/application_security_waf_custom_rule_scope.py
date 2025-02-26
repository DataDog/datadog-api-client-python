# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ApplicationSecurityWafCustomRuleScope(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "env": (str,),
            "service": (str,),
        }

    attribute_map = {
        "env": "env",
        "service": "service",
    }

    def __init__(self_, env: str, service: str, **kwargs):
        """
        The scope of the WAF custom rule.

        :param env: The environment scope for the WAF custom rule.
        :type env: str

        :param service: The service scope for the WAF custom rule.
        :type service: str
        """
        super().__init__(kwargs)

        self_.env = env
        self_.service = service
