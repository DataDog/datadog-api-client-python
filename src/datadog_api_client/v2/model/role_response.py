# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RoleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.role import Role

        return {
            "data": (Role,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self, *args, **kwargs):
        """
        Response containing information about a single role.

        :param data: Role object returned by the API.
        :type data: Role, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RoleResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
