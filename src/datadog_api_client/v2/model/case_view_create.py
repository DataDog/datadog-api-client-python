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
    from datadog_api_client.v2.model.case_view_create_attributes import CaseViewCreateAttributes
    from datadog_api_client.v2.model.case_view_resource_type import CaseViewResourceType


class CaseViewCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_view_create_attributes import CaseViewCreateAttributes
        from datadog_api_client.v2.model.case_view_resource_type import CaseViewResourceType

        return {
            "attributes": (CaseViewCreateAttributes,),
            "type": (CaseViewResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: CaseViewCreateAttributes, type: CaseViewResourceType, **kwargs):
        """
        Data object for creating a case view.

        :param attributes: Attributes required to create a case view.
        :type attributes: CaseViewCreateAttributes

        :param type: JSON:API resource type for case views.
        :type type: CaseViewResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
