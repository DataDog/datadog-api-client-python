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
    from datadog_api_client.v2.model.rum_sdk_config_rum_attributes import RumSdkConfigRumAttributes


class RumSdkConfigAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_sdk_config_rum_attributes import RumSdkConfigRumAttributes

        return {
            "rum": (RumSdkConfigRumAttributes,),
        }

    attribute_map = {
        "rum": "rum",
    }

    def __init__(self_, rum: RumSdkConfigRumAttributes, **kwargs):
        """
        Attributes of the RUM SDK configuration.

        :param rum: The RUM SDK settings for a configuration.
        :type rum: RumSdkConfigRumAttributes
        """
        super().__init__(kwargs)

        self_.rum = rum
