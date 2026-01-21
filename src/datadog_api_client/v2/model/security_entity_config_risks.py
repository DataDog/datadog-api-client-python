# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityEntityConfigRisks(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "has_identity_risk": (bool,),
            "has_misconfiguration": (bool,),
            "has_privileged_role": (bool,),
            "is_privileged": (bool,),
            "is_production": (bool,),
            "is_publicly_accessible": (bool,),
        }

    attribute_map = {
        "has_identity_risk": "hasIdentityRisk",
        "has_misconfiguration": "hasMisconfiguration",
        "has_privileged_role": "hasPrivilegedRole",
        "is_privileged": "isPrivileged",
        "is_production": "isProduction",
        "is_publicly_accessible": "isPubliclyAccessible",
    }

    def __init__(
        self_,
        has_identity_risk: bool,
        has_misconfiguration: bool,
        has_privileged_role: bool,
        is_privileged: bool,
        is_production: bool,
        is_publicly_accessible: bool,
        **kwargs,
    ):
        """
        Configuration risks associated with the entity

        :param has_identity_risk: Whether the entity has identity risks
        :type has_identity_risk: bool

        :param has_misconfiguration: Whether the entity has misconfigurations
        :type has_misconfiguration: bool

        :param has_privileged_role: Whether the entity has privileged roles
        :type has_privileged_role: bool

        :param is_privileged: Whether the entity has privileged access
        :type is_privileged: bool

        :param is_production: Whether the entity is in a production environment
        :type is_production: bool

        :param is_publicly_accessible: Whether the entity is publicly accessible
        :type is_publicly_accessible: bool
        """
        super().__init__(kwargs)

        self_.has_identity_risk = has_identity_risk
        self_.has_misconfiguration = has_misconfiguration
        self_.has_privileged_role = has_privileged_role
        self_.is_privileged = is_privileged
        self_.is_production = is_production
        self_.is_publicly_accessible = is_publicly_accessible
