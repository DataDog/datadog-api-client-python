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
    from datadog_api_client.v2.model.rum_rate_limit_config_attributes import RumRateLimitConfigAttributes
    from datadog_api_client.v2.model.rum_rate_limit_config_type import RumRateLimitConfigType


class RumRateLimitConfigData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_rate_limit_config_attributes import RumRateLimitConfigAttributes
        from datadog_api_client.v2.model.rum_rate_limit_config_type import RumRateLimitConfigType

        return {
            "attributes": (RumRateLimitConfigAttributes,),
            "id": (str,),
            "type": (RumRateLimitConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: RumRateLimitConfigAttributes, id: str, type: RumRateLimitConfigType, **kwargs):
        """
        The RUM rate limit configuration object.

        :param attributes: The RUM rate limit configuration properties.
        :type attributes: RumRateLimitConfigAttributes

        :param id: The identifier of the scope the rate limit configuration applies to.
        :type id: str

        :param type: The type of the resource, always ``rum_rate_limit_config``.
        :type type: RumRateLimitConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
