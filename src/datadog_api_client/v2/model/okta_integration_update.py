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
    from datadog_api_client.v2.model.okta_credentials_update import OktaCredentialsUpdate
    from datadog_api_client.v2.model.okta_integration_type import OktaIntegrationType
    from datadog_api_client.v2.model.okta_api_token_update import OktaAPITokenUpdate


class OktaIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.okta_credentials_update import OktaCredentialsUpdate
        from datadog_api_client.v2.model.okta_integration_type import OktaIntegrationType

        return {
            "credentials": (OktaCredentialsUpdate,),
            "type": (OktaIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: OktaIntegrationType,
        credentials: Union[OktaCredentialsUpdate, OktaAPITokenUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``OktaIntegrationUpdate`` object.

        :param credentials: The definition of the ``OktaCredentialsUpdate`` object.
        :type credentials: OktaCredentialsUpdate, optional

        :param type: The definition of the ``OktaIntegrationType`` object.
        :type type: OktaIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
