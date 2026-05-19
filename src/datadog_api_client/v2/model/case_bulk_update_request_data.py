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
    from datadog_api_client.v2.model.case_bulk_update_request_attributes import CaseBulkUpdateRequestAttributes
    from datadog_api_client.v2.model.case_bulk_resource_type import CaseBulkResourceType


class CaseBulkUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_bulk_update_request_attributes import CaseBulkUpdateRequestAttributes
        from datadog_api_client.v2.model.case_bulk_resource_type import CaseBulkResourceType

        return {
            "attributes": (CaseBulkUpdateRequestAttributes,),
            "type": (CaseBulkResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: CaseBulkUpdateRequestAttributes, type: CaseBulkResourceType, **kwargs):
        """
        Data object wrapping the bulk update type and attributes.

        :param attributes: Attributes for the bulk update, specifying which cases to update and the action to apply.
        :type attributes: CaseBulkUpdateRequestAttributes

        :param type: JSON:API resource type for bulk case operations.
        :type type: CaseBulkResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
