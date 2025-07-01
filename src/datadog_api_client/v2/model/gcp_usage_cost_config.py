# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.gcp_usage_cost_config_attributes import GCPUsageCostConfigAttributes
    from datadog_api_client.v2.model.gcp_usage_cost_config_type import GCPUsageCostConfigType


class GCPUsageCostConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcp_usage_cost_config_attributes import GCPUsageCostConfigAttributes
        from datadog_api_client.v2.model.gcp_usage_cost_config_type import GCPUsageCostConfigType

        return {
            "attributes": (GCPUsageCostConfigAttributes,),
            "id": (str,),
            "type": (GCPUsageCostConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: GCPUsageCostConfigAttributes,
        type: GCPUsageCostConfigType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        GCP Usage Cost config.

        :param attributes: Attributes for a GCP Usage Cost config.
        :type attributes: GCPUsageCostConfigAttributes

        :param id: The ID of the GCP Usage Cost config.
        :type id: str, optional

        :param type: Type of GCP Usage Cost config.
        :type type: GCPUsageCostConfigType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
