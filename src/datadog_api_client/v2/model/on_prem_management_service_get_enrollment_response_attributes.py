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
    from datadog_api_client.v2.model.on_prem_management_service_get_enrollment_response_attributes_status import (
        OnPremManagementServiceGetEnrollmentResponseAttributesStatus,
    )


class OnPremManagementServiceGetEnrollmentResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_prem_management_service_get_enrollment_response_attributes_status import (
            OnPremManagementServiceGetEnrollmentResponseAttributesStatus,
        )

        return {
            "failure_reason": (str,),
            "runner_id": (str,),
            "status": (OnPremManagementServiceGetEnrollmentResponseAttributesStatus,),
        }

    attribute_map = {
        "failure_reason": "failure_reason",
        "runner_id": "runner_id",
        "status": "status",
    }

    def __init__(
        self_,
        failure_reason: str,
        runner_id: str,
        status: OnPremManagementServiceGetEnrollmentResponseAttributesStatus,
        **kwargs,
    ):
        """
        Attributes for the enrollment status.

        :param failure_reason: The reason for enrollment failure, if applicable.
        :type failure_reason: str

        :param runner_id: The runner identifier, if enrollment was successful.
        :type runner_id: str

        :param status: The status of the enrollment.
        :type status: OnPremManagementServiceGetEnrollmentResponseAttributesStatus
        """
        super().__init__(kwargs)

        self_.failure_reason = failure_reason
        self_.runner_id = runner_id
        self_.status = status
