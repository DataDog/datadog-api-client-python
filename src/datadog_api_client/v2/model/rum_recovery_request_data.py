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
    from datadog_api_client.v2.model.rum_recovery_request_attributes import RumRecoveryRequestAttributes
    from datadog_api_client.v2.model.rum_recovery_request_type import RumRecoveryRequestType


class RumRecoveryRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_recovery_request_attributes import RumRecoveryRequestAttributes
        from datadog_api_client.v2.model.rum_recovery_request_type import RumRecoveryRequestType

        return {
            "attributes": (RumRecoveryRequestAttributes,),
            "id": (str,),
            "type": (RumRecoveryRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: RumRecoveryRequestAttributes, id: str, type: RumRecoveryRequestType, **kwargs):
        """
        JSON:API resource.

        :param attributes: Recovery progress. Batch-only attributes are omitted for targeted requests; request_type is also omitted for targeted requests.
        :type attributes: RumRecoveryRequestAttributes

        :param id: Resource identifier.
        :type id: str

        :param type: JSON:API resource type.
        :type type: RumRecoveryRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
