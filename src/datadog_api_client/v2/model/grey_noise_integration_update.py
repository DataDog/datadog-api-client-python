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
    from datadog_api_client.v2.model.grey_noise_credentials_update import GreyNoiseCredentialsUpdate
    from datadog_api_client.v2.model.grey_noise_integration_type import GreyNoiseIntegrationType
    from datadog_api_client.v2.model.grey_noise_api_key_update import GreyNoiseAPIKeyUpdate


class GreyNoiseIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.grey_noise_credentials_update import GreyNoiseCredentialsUpdate
        from datadog_api_client.v2.model.grey_noise_integration_type import GreyNoiseIntegrationType

        return {
            "credentials": (GreyNoiseCredentialsUpdate,),
            "type": (GreyNoiseIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: GreyNoiseIntegrationType,
        credentials: Union[GreyNoiseCredentialsUpdate, GreyNoiseAPIKeyUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``GreyNoiseIntegrationUpdate`` object.

        :param credentials: The definition of the ``GreyNoiseCredentialsUpdate`` object.
        :type credentials: GreyNoiseCredentialsUpdate, optional

        :param type: The definition of the ``GreyNoiseIntegrationType`` object.
        :type type: GreyNoiseIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
