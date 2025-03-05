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
    from datadog_api_client.v2.model.aws_on_demand_attributes import AwsOnDemandAttributes
    from datadog_api_client.v2.model.aws_on_demand_type import AwsOnDemandType


class AwsOnDemandData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_on_demand_attributes import AwsOnDemandAttributes
        from datadog_api_client.v2.model.aws_on_demand_type import AwsOnDemandType

        return {
            "attributes": (AwsOnDemandAttributes,),
            "id": (str,),
            "type": (AwsOnDemandType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[AwsOnDemandAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[AwsOnDemandType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Single AWS on demand task.

        :param attributes: Attributes for the AWS on demand task.
        :type attributes: AwsOnDemandAttributes, optional

        :param id: The UUID of the task.
        :type id: str, optional

        :param type: The type of the on demand task. The value should always be ``aws_resource``.
        :type type: AwsOnDemandType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
