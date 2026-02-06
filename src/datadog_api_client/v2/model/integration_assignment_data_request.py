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
    from datadog_api_client.v2.model.integration_assignment_data_attributes_request import (
        IntegrationAssignmentDataAttributesRequest,
    )
    from datadog_api_client.v2.model.integration_assignment_type import IntegrationAssignmentType


class IntegrationAssignmentDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_assignment_data_attributes_request import (
            IntegrationAssignmentDataAttributesRequest,
        )
        from datadog_api_client.v2.model.integration_assignment_type import IntegrationAssignmentType

        return {
            "attributes": (IntegrationAssignmentDataAttributesRequest,),
            "id": (str,),
            "type": (IntegrationAssignmentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IntegrationAssignmentDataAttributesRequest,
        id: str,
        type: IntegrationAssignmentType,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: IntegrationAssignmentDataAttributesRequest

        :param id: Unique identifier of the integration assignment.
        :type id: str

        :param type: Integration assignment resource type.
        :type type: IntegrationAssignmentType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
