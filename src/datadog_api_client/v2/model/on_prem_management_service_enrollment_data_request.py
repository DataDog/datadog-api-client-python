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
    from datadog_api_client.v2.model.on_prem_management_service_enrollment_attributes import (
        OnPremManagementServiceEnrollmentAttributes,
    )
    from datadog_api_client.v2.model.on_prem_management_service_enrollment_type import (
        OnPremManagementServiceEnrollmentType,
    )


class OnPremManagementServiceEnrollmentDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_prem_management_service_enrollment_attributes import (
            OnPremManagementServiceEnrollmentAttributes,
        )
        from datadog_api_client.v2.model.on_prem_management_service_enrollment_type import (
            OnPremManagementServiceEnrollmentType,
        )

        return {
            "attributes": (OnPremManagementServiceEnrollmentAttributes,),
            "type": (OnPremManagementServiceEnrollmentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OnPremManagementServiceEnrollmentAttributes,
        type: OnPremManagementServiceEnrollmentType,
        **kwargs,
    ):
        """
        Data for creating an enrollment.

        :param attributes: Attributes for creating an enrollment.
        :type attributes: OnPremManagementServiceEnrollmentAttributes

        :param type: The type of the resource. The value should always be enrollment.
        :type type: OnPremManagementServiceEnrollmentType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
