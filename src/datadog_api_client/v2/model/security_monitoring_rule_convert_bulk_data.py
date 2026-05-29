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
    from datadog_api_client.v2.model.security_monitoring_rule_convert_bulk_attributes import (
        SecurityMonitoringRuleConvertBulkAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_rule_convert_bulk_data_type import (
        SecurityMonitoringRuleConvertBulkDataType,
    )


class SecurityMonitoringRuleConvertBulkData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_convert_bulk_attributes import (
            SecurityMonitoringRuleConvertBulkAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_convert_bulk_data_type import (
            SecurityMonitoringRuleConvertBulkDataType,
        )

        return {
            "attributes": (SecurityMonitoringRuleConvertBulkAttributes,),
            "id": (str,),
            "type": (SecurityMonitoringRuleConvertBulkDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringRuleConvertBulkAttributes,
        type: SecurityMonitoringRuleConvertBulkDataType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for bulk converting security monitoring rules to Terraform.

        :param attributes: Attributes for bulk converting security monitoring rules to Terraform.
        :type attributes: SecurityMonitoringRuleConvertBulkAttributes

        :param id: Request ID.
        :type id: str, optional

        :param type: The type of the resource.
        :type type: SecurityMonitoringRuleConvertBulkDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
