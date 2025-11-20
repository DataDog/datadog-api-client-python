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
    from datadog_api_client.v2.model.restriction_query_update_attributes import RestrictionQueryUpdateAttributes
    from datadog_api_client.v2.model.logs_restriction_queries_type import LogsRestrictionQueriesType


class RestrictionQueryUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.restriction_query_update_attributes import RestrictionQueryUpdateAttributes
        from datadog_api_client.v2.model.logs_restriction_queries_type import LogsRestrictionQueriesType

        return {
            "attributes": (RestrictionQueryUpdateAttributes,),
            "type": (LogsRestrictionQueriesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[RestrictionQueryUpdateAttributes, UnsetType] = unset,
        type: Union[LogsRestrictionQueriesType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data related to the update of a restriction query.

        :param attributes: Attributes of the edited restriction query.
        :type attributes: RestrictionQueryUpdateAttributes, optional

        :param type: Restriction query resource type.
        :type type: LogsRestrictionQueriesType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
