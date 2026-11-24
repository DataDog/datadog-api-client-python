# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityAgentOutreachDomainAddRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "domain": (str,),
        }

    attribute_map = {
        "domain": "domain",
    }

    def __init__(self_, domain: str, **kwargs):
        """
        The email domain to allow.

        :param domain: The email domain to allow: a fully qualified domain name, like ``example.com``. Lowercased
            before being stored.
        :type domain: str
        """
        super().__init__(kwargs)

        self_.domain = domain
