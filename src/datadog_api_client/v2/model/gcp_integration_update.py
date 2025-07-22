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
    from datadog_api_client.v2.model.gcp_credentials_update import GCPCredentialsUpdate
    from datadog_api_client.v2.model.gcp_integration_type import GCPIntegrationType
    from datadog_api_client.v2.model.gcp_service_account_update import GCPServiceAccountUpdate


class GCPIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcp_credentials_update import GCPCredentialsUpdate
        from datadog_api_client.v2.model.gcp_integration_type import GCPIntegrationType

        return {
            "credentials": (GCPCredentialsUpdate,),
            "type": (GCPIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: GCPIntegrationType,
        credentials: Union[GCPCredentialsUpdate, GCPServiceAccountUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``GCPIntegrationUpdate`` object.

        :param credentials: The definition of the ``GCPCredentialsUpdate`` object.
        :type credentials: GCPCredentialsUpdate, optional

        :param type: The definition of the ``GCPIntegrationType`` object.
        :type type: GCPIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
