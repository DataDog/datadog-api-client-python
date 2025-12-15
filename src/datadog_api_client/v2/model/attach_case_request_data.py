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
    from datadog_api_client.v2.model.attach_case_request_data_relationships import AttachCaseRequestDataRelationships
    from datadog_api_client.v2.model.case_data_type import CaseDataType


class AttachCaseRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.attach_case_request_data_relationships import (
            AttachCaseRequestDataRelationships,
        )
        from datadog_api_client.v2.model.case_data_type import CaseDataType

        return {
            "id": (str,),
            "relationships": (AttachCaseRequestDataRelationships,),
            "type": (CaseDataType,),
        }

    attribute_map = {
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: CaseDataType,
        relationships: Union[AttachCaseRequestDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data of the case to attach security findings to.

        :param id: Unique identifier of the case.
        :type id: str

        :param relationships: Relationships of the case to attach security findings to.
        :type relationships: AttachCaseRequestDataRelationships, optional

        :param type: Cases resource type.
        :type type: CaseDataType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
