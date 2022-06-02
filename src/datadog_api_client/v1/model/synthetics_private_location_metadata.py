# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsPrivateLocationMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_restricted_roles import SyntheticsRestrictedRoles

        return {
            "restricted_roles": (SyntheticsRestrictedRoles,),
        }

    attribute_map = {
        "restricted_roles": "restricted_roles",
    }

    def __init__(self, *args, **kwargs):
        """
        Object containing metadata about the private location.

        :param restricted_roles: A list of role identifiers that can be pulled from the Roles API, for restricting read and write access.
        :type restricted_roles: SyntheticsRestrictedRoles, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsPrivateLocationMetadata, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
