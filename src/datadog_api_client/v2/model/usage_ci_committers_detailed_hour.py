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
    from datadog_api_client.v2.model.usage_ci_committers_detailed_attributes import UsageCICommittersDetailedAttributes
    from datadog_api_client.v2.model.usage_data_point_type import UsageDataPointType


class UsageCICommittersDetailedHour(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_ci_committers_detailed_attributes import (
            UsageCICommittersDetailedAttributes,
        )
        from datadog_api_client.v2.model.usage_data_point_type import UsageDataPointType

        return {
            "attributes": (UsageCICommittersDetailedAttributes,),
            "id": (str,),
            "type": (UsageDataPointType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[UsageCICommittersDetailedAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[UsageDataPointType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The response containing attributions for the specified org.

        :param attributes: The response containing CI Committers Detailed attributes for specified organization.
        :type attributes: UsageCICommittersDetailedAttributes, optional

        :param id: A unique ID for the JSON API resource.
        :type id: str, optional

        :param type: The type of shape of the data.
        :type type: UsageDataPointType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
