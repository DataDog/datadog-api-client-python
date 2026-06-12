# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ApplicationSecurityServicesMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "num_services_with_appsec": (int,),
        }

    attribute_map = {
        "num_services_with_appsec": "num_services_with_appsec",
    }

    def __init__(self_, num_services_with_appsec: int, **kwargs):
        """
        Metadata returned alongside the list of services.

        :param num_services_with_appsec: The number of services with Application Security Management (Threats) enabled.
        :type num_services_with_appsec: int
        """
        super().__init__(kwargs)

        self_.num_services_with_appsec = num_services_with_appsec
