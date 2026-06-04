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
    from datadog_api_client.v2.model.customer_org_disable_status import CustomerOrgDisableStatus


class CustomerOrgDisableResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.customer_org_disable_status import CustomerOrgDisableStatus

        return {
            "status": (CustomerOrgDisableStatus,),
        }

    attribute_map = {
        "status": "status",
    }

    def __init__(self_, status: CustomerOrgDisableStatus, **kwargs):
        """
        Attributes describing the outcome of the disable action on the customer organization.

        :param status: Resulting lifecycle status of the organization after the disable action.
        :type status: CustomerOrgDisableStatus
        """
        super().__init__(kwargs)

        self_.status = status
