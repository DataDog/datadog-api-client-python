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
    from datadog_api_client.v2.model.workflow_data_update_attributes import WorkflowDataUpdateAttributes
    from datadog_api_client.v2.model.workflow_data_relationships import WorkflowDataRelationships
    from datadog_api_client.v2.model.workflow_data_type import WorkflowDataType


class WorkflowDataUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_data_update_attributes import WorkflowDataUpdateAttributes
        from datadog_api_client.v2.model.workflow_data_relationships import WorkflowDataRelationships
        from datadog_api_client.v2.model.workflow_data_type import WorkflowDataType

        return {
            "attributes": (WorkflowDataUpdateAttributes,),
            "id": (str,),
            "relationships": (WorkflowDataRelationships,),
            "type": (WorkflowDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }
    read_only_vars = {
        "relationships",
    }

    def __init__(
        self_,
        attributes: WorkflowDataUpdateAttributes,
        type: WorkflowDataType,
        id: Union[str, UnsetType] = unset,
        relationships: Union[WorkflowDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data related to the workflow being updated.

        :param attributes: The definition of ``WorkflowDataUpdateAttributes`` object.
        :type attributes: WorkflowDataUpdateAttributes

        :param id: The workflow identifier
        :type id: str, optional

        :param relationships: The definition of ``WorkflowDataRelationships`` object.
        :type relationships: WorkflowDataRelationships, optional

        :param type: The definition of ``WorkflowDataType`` object.
        :type type: WorkflowDataType
        """
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
