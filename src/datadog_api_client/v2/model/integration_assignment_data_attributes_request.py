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
    from datadog_api_client.v2.model.integration_assignment_data_attributes_request_action import (
        IntegrationAssignmentDataAttributesRequestAction,
    )
    from datadog_api_client.v2.model.integration_assignment_data_attributes_request_assignment import (
        IntegrationAssignmentDataAttributesRequestAssignment,
    )
    from datadog_api_client.v2.model.integration_assignment_data_attributes_request_type import (
        IntegrationAssignmentDataAttributesRequestType,
    )


class IntegrationAssignmentDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_assignment_data_attributes_request_action import (
            IntegrationAssignmentDataAttributesRequestAction,
        )
        from datadog_api_client.v2.model.integration_assignment_data_attributes_request_assignment import (
            IntegrationAssignmentDataAttributesRequestAssignment,
        )
        from datadog_api_client.v2.model.integration_assignment_data_attributes_request_type import (
            IntegrationAssignmentDataAttributesRequestType,
        )

        return {
            "action": (IntegrationAssignmentDataAttributesRequestAction,),
            "assignment": (IntegrationAssignmentDataAttributesRequestAssignment,),
            "type": (IntegrationAssignmentDataAttributesRequestType,),
        }

    attribute_map = {
        "action": "action",
        "assignment": "assignment",
        "type": "type",
    }

    def __init__(
        self_,
        action: IntegrationAssignmentDataAttributesRequestAction,
        assignment: IntegrationAssignmentDataAttributesRequestAssignment,
        type: IntegrationAssignmentDataAttributesRequestType,
        **kwargs,
    ):
        """


        :param action: Action to perform on the assignment. Can be "assign" or "un_assign".
        :type action: IntegrationAssignmentDataAttributesRequestAction

        :param assignment:
        :type assignment: IntegrationAssignmentDataAttributesRequestAssignment

        :param type: Type of the security issues. Can be "findings" or "vulnerabilities".
        :type type: IntegrationAssignmentDataAttributesRequestType
        """
        super().__init__(kwargs)

        self_.action = action
        self_.assignment = assignment
        self_.type = type
