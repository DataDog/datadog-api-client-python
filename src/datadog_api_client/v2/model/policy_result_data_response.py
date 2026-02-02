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
    from datadog_api_client.v2.model.policy_result_attributes_response import PolicyResultAttributesResponse
    from datadog_api_client.v2.model.policy_result_type import PolicyResultType


class PolicyResultDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.policy_result_attributes_response import PolicyResultAttributesResponse
        from datadog_api_client.v2.model.policy_result_type import PolicyResultType

        return {
            "attributes": (PolicyResultAttributesResponse,),
            "id": (str,),
            "type": (PolicyResultType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: PolicyResultAttributesResponse, id: str, type: PolicyResultType, **kwargs):
        """
        Data envelope for policy result response.

        :param attributes: Attributes of a policy evaluation result.
        :type attributes: PolicyResultAttributesResponse

        :param id: The unique identifier of the policy result.
        :type id: str

        :param type: The type of the resource. The value should always be ``policy_result``.
        :type type: PolicyResultType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
