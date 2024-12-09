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
    from datadog_api_client.v2.model.aws_new_external_id_response_attributes import AWSNewExternalIDResponseAttributes
    from datadog_api_client.v2.model.aws_new_external_id_response_data_type import AWSNewExternalIDResponseDataType


class AWSNewExternalIDResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_new_external_id_response_attributes import (
            AWSNewExternalIDResponseAttributes,
        )
        from datadog_api_client.v2.model.aws_new_external_id_response_data_type import AWSNewExternalIDResponseDataType

        return {
            "attributes": (AWSNewExternalIDResponseAttributes,),
            "id": (str,),
            "type": (AWSNewExternalIDResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: AWSNewExternalIDResponseDataType,
        attributes: Union[AWSNewExternalIDResponseAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS External ID response body.

        :param attributes: AWS External ID response body.
        :type attributes: AWSNewExternalIDResponseAttributes, optional

        :param id: The ``AWSNewExternalIDResponseData`` ``id``.
        :type id: str

        :param type: The ``AWSNewExternalIDResponseData`` ``type``.
        :type type: AWSNewExternalIDResponseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)
        id = kwargs.get("id", "external_id")

        self_.id = id
        self_.type = type
