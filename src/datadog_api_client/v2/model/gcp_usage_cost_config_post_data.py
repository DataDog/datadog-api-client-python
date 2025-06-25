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
    from datadog_api_client.v2.model.gcp_usage_cost_config_post_request_attributes import (
        GCPUsageCostConfigPostRequestAttributes,
    )
    from datadog_api_client.v2.model.gcp_usage_cost_config_post_request_type import GCPUsageCostConfigPostRequestType


class GCPUsageCostConfigPostData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcp_usage_cost_config_post_request_attributes import (
            GCPUsageCostConfigPostRequestAttributes,
        )
        from datadog_api_client.v2.model.gcp_usage_cost_config_post_request_type import (
            GCPUsageCostConfigPostRequestType,
        )

        return {
            "attributes": (GCPUsageCostConfigPostRequestAttributes,),
            "type": (GCPUsageCostConfigPostRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: GCPUsageCostConfigPostRequestAttributes, type: GCPUsageCostConfigPostRequestType, **kwargs
    ):
        """
        GCP Usage Cost config post data.

        :param attributes: Attributes for GCP Usage Cost config post request.
        :type attributes: GCPUsageCostConfigPostRequestAttributes

        :param type: Type of GCP Usage Cost config post request.
        :type type: GCPUsageCostConfigPostRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
