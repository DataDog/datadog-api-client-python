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
    from datadog_api_client.v2.model.create_status_page_email_access_policy_request_data_attributes import (
        CreateStatusPageEmailAccessPolicyRequestDataAttributes,
    )
    from datadog_api_client.v2.model.status_page_email_access_policy_type import StatusPageEmailAccessPolicyType


class CreateStatusPageEmailAccessPolicyRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_status_page_email_access_policy_request_data_attributes import (
            CreateStatusPageEmailAccessPolicyRequestDataAttributes,
        )
        from datadog_api_client.v2.model.status_page_email_access_policy_type import StatusPageEmailAccessPolicyType

        return {
            "attributes": (CreateStatusPageEmailAccessPolicyRequestDataAttributes,),
            "type": (StatusPageEmailAccessPolicyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CreateStatusPageEmailAccessPolicyRequestDataAttributes,
        type: StatusPageEmailAccessPolicyType,
        **kwargs,
    ):
        """
        The data object for creating a status page email access policy.

        :param attributes: Attributes for creating a status page email access policy.
        :type attributes: CreateStatusPageEmailAccessPolicyRequestDataAttributes

        :param type: Status page email access policy resource type.
        :type type: StatusPageEmailAccessPolicyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
