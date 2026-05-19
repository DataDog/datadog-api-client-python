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
    from datadog_api_client.v2.model.case_update_priority_attributes import CaseUpdatePriorityAttributes
    from datadog_api_client.v2.model.case_resource_type import CaseResourceType


class CaseUpdatePriority(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_update_priority_attributes import CaseUpdatePriorityAttributes
        from datadog_api_client.v2.model.case_resource_type import CaseResourceType

        return {
            "attributes": (CaseUpdatePriorityAttributes,),
            "type": (CaseResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: CaseUpdatePriorityAttributes, type: CaseResourceType, **kwargs):
        """
        Case priority status

        :param attributes: Case update priority attributes
        :type attributes: CaseUpdatePriorityAttributes

        :param type: Case resource type
        :type type: CaseResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
