# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.opsgenie_service_region_type import OpsgenieServiceRegionType


class OpsgenieAccountCreateAttributes(ModelNormal):
    validations = {
        "api_key": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.opsgenie_service_region_type import OpsgenieServiceRegionType

        return {
            "api_key": (str,),
            "region": (OpsgenieServiceRegionType,),
        }

    attribute_map = {
        "api_key": "api_key",
        "region": "region",
    }

    def __init__(self_, api_key: str, region: OpsgenieServiceRegionType, **kwargs):
        """
        The Opsgenie account attributes for a create request.

        :param api_key: The Opsgenie API key for your Opsgenie account.
        :type api_key: str

        :param region: The region for the Opsgenie service.
        :type region: OpsgenieServiceRegionType
        """
        super().__init__(kwargs)

        self_.api_key = api_key
        self_.region = region
