# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class EntityV3DatadogIntegrationOpsgenie(ModelNormal):
    validations = {
        "region": {
            "min_length": 1,
        },
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
            "region": (str,),
            "service_url": (str,),
        }

    attribute_map = {
        "region": "region",
        "service_url": "serviceURL",
    }

    def __init__(self_, service_url: str, region: Union[str, UnsetType] = unset, **kwargs):
        """
        An Opsgenie integration schema

        :param region: The region for the Opsgenie integration.
        :type region: str, optional

        :param service_url: The service url for the Opsgenie integration.
        :type service_url: str
        """
        if region is not unset:
            kwargs["region"] = region
        super().__init__(kwargs)

        self_.service_url = service_url
