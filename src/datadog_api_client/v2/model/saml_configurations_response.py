# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.saml_configuration import SAMLConfiguration
    from datadog_api_client.v2.model.role import Role


class SAMLConfigurationsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saml_configuration import SAMLConfiguration
        from datadog_api_client.v2.model.role import Role

        return {
            "data": ([SAMLConfiguration],),
            "included": ([Role],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[List[SAMLConfiguration], UnsetType] = unset,
        included: Union[List[Role], UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing a list of SAML configurations.

        :param data: Array of SAML configurations. An organization has at most one SAML configuration.
        :type data: [SAMLConfiguration], optional

        :param included: Resources related to the SAML configurations, such as the default roles.
        :type included: [Role], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
