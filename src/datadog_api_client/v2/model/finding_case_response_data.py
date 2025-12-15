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
    from datadog_api_client.v2.model.finding_case_response_data_attributes import FindingCaseResponseDataAttributes
    from datadog_api_client.v2.model.finding_case_response_data_relationships import (
        FindingCaseResponseDataRelationships,
    )
    from datadog_api_client.v2.model.case_data_type import CaseDataType


class FindingCaseResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.finding_case_response_data_attributes import FindingCaseResponseDataAttributes
        from datadog_api_client.v2.model.finding_case_response_data_relationships import (
            FindingCaseResponseDataRelationships,
        )
        from datadog_api_client.v2.model.case_data_type import CaseDataType

        return {
            "attributes": (FindingCaseResponseDataAttributes,),
            "id": (str,),
            "relationships": (FindingCaseResponseDataRelationships,),
            "type": (CaseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: CaseDataType,
        attributes: Union[FindingCaseResponseDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[FindingCaseResponseDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data of the case.

        :param attributes: Attributes of the case.
        :type attributes: FindingCaseResponseDataAttributes, optional

        :param id: Unique identifier of the case.
        :type id: str, optional

        :param relationships: Relationships of the case.
        :type relationships: FindingCaseResponseDataRelationships, optional

        :param type: Cases resource type.
        :type type: CaseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
