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
    from datadog_api_client.v2.model.dora_list_deployments_request_attributes import (
        DORAListDeploymentsRequestAttributes,
    )
    from datadog_api_client.v2.model.dora_list_deployments_request_data_type import DORAListDeploymentsRequestDataType


class DORAListDeploymentsRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dora_list_deployments_request_attributes import (
            DORAListDeploymentsRequestAttributes,
        )
        from datadog_api_client.v2.model.dora_list_deployments_request_data_type import (
            DORAListDeploymentsRequestDataType,
        )

        return {
            "attributes": (DORAListDeploymentsRequestAttributes,),
            "type": (DORAListDeploymentsRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: DORAListDeploymentsRequestAttributes,
        type: Union[DORAListDeploymentsRequestDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The JSON:API data.

        :param attributes: Attributes to get a list of deployments.
        :type attributes: DORAListDeploymentsRequestAttributes

        :param type: The definition of ``DORAListDeploymentsRequestDataType`` object.
        :type type: DORAListDeploymentsRequestDataType, optional
        """
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.attributes = attributes
