# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.logs_archive_order_attributes import LogsArchiveOrderAttributes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.logs_archive_order_definition_type import LogsArchiveOrderDefinitionType


@dataclass
class LogsArchiveOrderDefinitionJSON:
    archive_ids: Union[List[str], UnsetType] = unset


class LogsArchiveOrderDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_archive_order_definition_type import LogsArchiveOrderDefinitionType

        return {
            "attributes": (LogsArchiveOrderAttributes,),
            "type": (LogsArchiveOrderDefinitionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = LogsArchiveOrderDefinitionJSON

    def __init__(self_, attributes: LogsArchiveOrderAttributes, type: LogsArchiveOrderDefinitionType, **kwargs):
        """
        The definition of an archive order.

        :param attributes: The attributes associated with the archive order.
        :type attributes: LogsArchiveOrderAttributes

        :param type: Type of the archive order definition.
        :type type: LogsArchiveOrderDefinitionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
