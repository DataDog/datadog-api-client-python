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
    from datadog_api_client.v2.model.change_request_branch_create_attributes import ChangeRequestBranchCreateAttributes
    from datadog_api_client.v2.model.change_request_branch_resource_type import ChangeRequestBranchResourceType


class ChangeRequestBranchCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_branch_create_attributes import (
            ChangeRequestBranchCreateAttributes,
        )
        from datadog_api_client.v2.model.change_request_branch_resource_type import ChangeRequestBranchResourceType

        return {
            "attributes": (ChangeRequestBranchCreateAttributes,),
            "type": (ChangeRequestBranchResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: ChangeRequestBranchCreateAttributes, type: ChangeRequestBranchResourceType, **kwargs
    ):
        """
        Data object to create a change request branch.

        :param attributes: Attributes for creating a change request branch.
        :type attributes: ChangeRequestBranchCreateAttributes

        :param type: Change request branch resource type.
        :type type: ChangeRequestBranchResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
