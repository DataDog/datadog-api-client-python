# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.remediation_group_case_relationship_data import (
        RemediationGroupCaseRelationshipData,
    )


class RemediationGroupCaseRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remediation_group_case_relationship_data import (
            RemediationGroupCaseRelationshipData,
        )

        return {
            "data": (RemediationGroupCaseRelationshipData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[RemediationGroupCaseRelationshipData, none_type], **kwargs):
        """
        Relationship to the case that tracks the group's remediation.

        :param data: The group's case, or null when the group has no case yet.
        :type data: RemediationGroupCaseRelationshipData, none_type
        """
        super().__init__(kwargs)

        self_.data = data
