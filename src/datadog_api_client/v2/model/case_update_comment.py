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
    from datadog_api_client.v2.model.case_update_comment_attributes import CaseUpdateCommentAttributes
    from datadog_api_client.v2.model.case_resource_type import CaseResourceType


class CaseUpdateComment(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_update_comment_attributes import CaseUpdateCommentAttributes
        from datadog_api_client.v2.model.case_resource_type import CaseResourceType

        return {
            "attributes": (CaseUpdateCommentAttributes,),
            "type": (CaseResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: CaseUpdateCommentAttributes, type: CaseResourceType, **kwargs):
        """
        Data object for updating a case comment.

        :param attributes: Attributes for updating a comment.
        :type attributes: CaseUpdateCommentAttributes

        :param type: JSON:API resource type for cases.
        :type type: CaseResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
