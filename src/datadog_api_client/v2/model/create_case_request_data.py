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
    from datadog_api_client.v2.model.create_case_request_data_attributes import CreateCaseRequestDataAttributes
    from datadog_api_client.v2.model.create_case_request_data_relationships import CreateCaseRequestDataRelationships
    from datadog_api_client.v2.model.case_data_type import CaseDataType


class CreateCaseRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_case_request_data_attributes import CreateCaseRequestDataAttributes
        from datadog_api_client.v2.model.create_case_request_data_relationships import (
            CreateCaseRequestDataRelationships,
        )
        from datadog_api_client.v2.model.case_data_type import CaseDataType

        return {
            "attributes": (CreateCaseRequestDataAttributes,),
            "relationships": (CreateCaseRequestDataRelationships,),
            "type": (CaseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: CaseDataType,
        attributes: Union[CreateCaseRequestDataAttributes, UnsetType] = unset,
        relationships: Union[CreateCaseRequestDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data of the case to create.

        :param attributes: Attributes of the case to create.
        :type attributes: CreateCaseRequestDataAttributes, optional

        :param relationships: Relationships of the case to create.
        :type relationships: CreateCaseRequestDataRelationships, optional

        :param type: Cases resource type.
        :type type: CaseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
