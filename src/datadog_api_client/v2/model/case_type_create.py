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
    from datadog_api_client.v2.model.case_type_resource_attributes import CaseTypeResourceAttributes
    from datadog_api_client.v2.model.case_type_resource_type import CaseTypeResourceType


class CaseTypeCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_type_resource_attributes import CaseTypeResourceAttributes
        from datadog_api_client.v2.model.case_type_resource_type import CaseTypeResourceType

        return {
            "attributes": (CaseTypeResourceAttributes,),
            "type": (CaseTypeResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: CaseTypeResourceAttributes, type: CaseTypeResourceType, **kwargs):
        """
        Case type

        :param attributes: Case Type resource attributes
        :type attributes: CaseTypeResourceAttributes

        :param type: Case type resource type
        :type type: CaseTypeResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
