# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.aws_on_demand_create_attributes import AwsOnDemandCreateAttributes
    from datadog_api_client.v2.model.aws_on_demand_type import AwsOnDemandType


class AwsOnDemandCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_on_demand_create_attributes import AwsOnDemandCreateAttributes
        from datadog_api_client.v2.model.aws_on_demand_type import AwsOnDemandType

        return {
            "attributes": (AwsOnDemandCreateAttributes,),
            "type": (AwsOnDemandType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: AwsOnDemandCreateAttributes, type: AwsOnDemandType, **kwargs):
        """
        Object for a single AWS on demand task.

        :param attributes: Attributes for the AWS on demand task.
        :type attributes: AwsOnDemandCreateAttributes

        :param type: The type of the on demand task. The value should always be ``aws_resource``.
        :type type: AwsOnDemandType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
