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
    from datadog_api_client.v2.model.synthetics_network_test import SyntheticsNetworkTest
    from datadog_api_client.v2.model.synthetics_network_test_response_type import SyntheticsNetworkTestResponseType


class SyntheticsNetworkTestResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_network_test import SyntheticsNetworkTest
        from datadog_api_client.v2.model.synthetics_network_test_response_type import SyntheticsNetworkTestResponseType

        return {
            "attributes": (SyntheticsNetworkTest,),
            "id": (str,),
            "type": (SyntheticsNetworkTestResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    read_only_vars = {
        "id",
    }

    def __init__(
        self_,
        attributes: Union[SyntheticsNetworkTest, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SyntheticsNetworkTestResponseType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Network Path test response data.

        :param attributes: Object containing details about a Network Path test.
        :type attributes: SyntheticsNetworkTest, optional

        :param id: The public ID of the Network Path test.
        :type id: str, optional

        :param type: Type of response, ``network_test``.
        :type type: SyntheticsNetworkTestResponseType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
