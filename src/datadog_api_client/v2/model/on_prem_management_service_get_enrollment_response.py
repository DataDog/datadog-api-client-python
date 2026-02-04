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
    from datadog_api_client.v2.model.on_prem_management_service_get_enrollment_response_data import (
        OnPremManagementServiceGetEnrollmentResponseData,
    )


class OnPremManagementServiceGetEnrollmentResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_prem_management_service_get_enrollment_response_data import (
            OnPremManagementServiceGetEnrollmentResponseData,
        )

        return {
            "data": (OnPremManagementServiceGetEnrollmentResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OnPremManagementServiceGetEnrollmentResponseData, **kwargs):
        """
        Response for getting an enrollment status.

        :param data: Data for the enrollment status.
        :type data: OnPremManagementServiceGetEnrollmentResponseData
        """
        super().__init__(kwargs)

        self_.data = data
