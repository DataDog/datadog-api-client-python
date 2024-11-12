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
    from datadog_api_client.v2.model.aws_logs_services_response_attributes import AWSLogsServicesResponseAttributes
    from datadog_api_client.v2.model.aws_logs_services_response_data_type import AWSLogsServicesResponseDataType


class AWSLogsServicesResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_logs_services_response_attributes import AWSLogsServicesResponseAttributes
        from datadog_api_client.v2.model.aws_logs_services_response_data_type import AWSLogsServicesResponseDataType

        return {
            "attributes": (AWSLogsServicesResponseAttributes,),
            "id": (str,),
            "type": (AWSLogsServicesResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: AWSLogsServicesResponseDataType,
        attributes: Union[AWSLogsServicesResponseAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS Logs Services response body

        :param attributes: AWS Logs Services response body
        :type attributes: AWSLogsServicesResponseAttributes, optional

        :param id: The ``AWSLogsServicesResponseData`` ``id``.
        :type id: str

        :param type: The ``AWSLogsServicesResponseData`` ``type``.
        :type type: AWSLogsServicesResponseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)
        id = kwargs.get("id", "logs_services")

        self_.id = id
        self_.type = type
