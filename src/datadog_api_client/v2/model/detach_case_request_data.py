# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.detach_case_request_data_relationships import DetachCaseRequestDataRelationships
    from datadog_api_client.v2.model.case_data_type import CaseDataType


class DetachCaseRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.detach_case_request_data_relationships import (
            DetachCaseRequestDataRelationships,
        )
        from datadog_api_client.v2.model.case_data_type import CaseDataType

        return {
            "relationships": (DetachCaseRequestDataRelationships,),
            "type": (CaseDataType,),
        }

    attribute_map = {
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_, type: CaseDataType, relationships: Union[DetachCaseRequestDataRelationships, UnsetType] = unset, **kwargs
    ):
        """
        Data for detaching security findings from their case.

        :param relationships: Relationships detaching security findings from their case.
        :type relationships: DetachCaseRequestDataRelationships, optional

        :param type: Cases resource type.
        :type type: CaseDataType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
