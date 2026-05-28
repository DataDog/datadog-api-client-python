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
    from datadog_api_client.v2.model.issue_definition_data_attributes import IssueDefinitionDataAttributes
    from datadog_api_client.v2.model.issue_definition_data_type import IssueDefinitionDataType


class IssueDefinitionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_definition_data_attributes import IssueDefinitionDataAttributes
        from datadog_api_client.v2.model.issue_definition_data_type import IssueDefinitionDataType

        return {
            "attributes": (IssueDefinitionDataAttributes,),
            "id": (str,),
            "type": (IssueDefinitionDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: IssueDefinitionDataType,
        attributes: Union[IssueDefinitionDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single issue definition entry returned by the issues endpoint.

        :param attributes: Attributes of a single End User Device Monitoring issue definition.
        :type attributes: IssueDefinitionDataAttributes, optional

        :param id: Stable identifier of the issue definition, used in the ``issues`` field of a device record.
        :type id: str

        :param type: Issue definitions resource type.
        :type type: IssueDefinitionDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
