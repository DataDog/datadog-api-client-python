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
    from datadog_api_client.v2.model.security_monitoring_rule_bulk_delete_response_attributes import (
        SecurityMonitoringRuleBulkDeleteResponseAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_rule_bulk_delete_response_data_type import (
        SecurityMonitoringRuleBulkDeleteResponseDataType,
    )


class SecurityMonitoringRuleBulkDeleteResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_bulk_delete_response_attributes import (
            SecurityMonitoringRuleBulkDeleteResponseAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_bulk_delete_response_data_type import (
            SecurityMonitoringRuleBulkDeleteResponseDataType,
        )

        return {
            "attributes": (SecurityMonitoringRuleBulkDeleteResponseAttributes,),
            "id": (str,),
            "type": (SecurityMonitoringRuleBulkDeleteResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SecurityMonitoringRuleBulkDeleteResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SecurityMonitoringRuleBulkDeleteResponseDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for the bulk delete response.

        :param attributes: Attributes for the bulk delete response.
        :type attributes: SecurityMonitoringRuleBulkDeleteResponseAttributes, optional

        :param id: The identifier of the bulk delete response.
        :type id: str, optional

        :param type: The resource type for a bulk delete response.
        :type type: SecurityMonitoringRuleBulkDeleteResponseDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
