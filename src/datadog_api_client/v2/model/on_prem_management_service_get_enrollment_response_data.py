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
    from datadog_api_client.v2.model.on_prem_management_service_get_enrollment_response_attributes import (
        OnPremManagementServiceGetEnrollmentResponseAttributes,
    )
    from datadog_api_client.v2.model.on_prem_management_service_get_enrollment_response_type import (
        OnPremManagementServiceGetEnrollmentResponseType,
    )


class OnPremManagementServiceGetEnrollmentResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_prem_management_service_get_enrollment_response_attributes import (
            OnPremManagementServiceGetEnrollmentResponseAttributes,
        )
        from datadog_api_client.v2.model.on_prem_management_service_get_enrollment_response_type import (
            OnPremManagementServiceGetEnrollmentResponseType,
        )

        return {
            "attributes": (OnPremManagementServiceGetEnrollmentResponseAttributes,),
            "id": (str,),
            "type": (OnPremManagementServiceGetEnrollmentResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OnPremManagementServiceGetEnrollmentResponseAttributes,
        id: str,
        type: OnPremManagementServiceGetEnrollmentResponseType,
        **kwargs,
    ):
        """
        Data for the enrollment status.

        :param attributes: Attributes for the enrollment status.
        :type attributes: OnPremManagementServiceGetEnrollmentResponseAttributes

        :param id: The token hash identifier.
        :type id: str

        :param type: The type of the resource. The value should always be getEnrollmentResponse.
        :type type: OnPremManagementServiceGetEnrollmentResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
