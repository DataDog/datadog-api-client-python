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
    from datadog_api_client.v2.model.case_assign_attributes import CaseAssignAttributes
    from datadog_api_client.v2.model.case_resource_type import CaseResourceType


class CaseAssign(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_assign_attributes import CaseAssignAttributes
        from datadog_api_client.v2.model.case_resource_type import CaseResourceType

        return {
            "attributes": (CaseAssignAttributes,),
            "type": (CaseResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: CaseAssignAttributes, type: CaseResourceType, **kwargs):
        """
        Case assign

        :param attributes: Case assign attributes
        :type attributes: CaseAssignAttributes

        :param type: Case resource type
        :type type: CaseResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
