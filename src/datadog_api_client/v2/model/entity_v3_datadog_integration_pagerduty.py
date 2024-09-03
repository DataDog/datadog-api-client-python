# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class EntityV3DatadogIntegrationPagerduty(ModelNormal):
    validations = {
        "service_url": {
            "min_length": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "service_url": (str,),
        }

    attribute_map = {
        "service_url": "serviceURL",
    }

    def __init__(self_, service_url: str, **kwargs):
        """
        An PagerDuty integration schema

        :param service_url: The service url for the PagerDuty integration.
        :type service_url: str
        """
        super().__init__(kwargs)

        self_.service_url = service_url
