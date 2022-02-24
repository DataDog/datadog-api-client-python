# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.user import User

    globals()["User"] = User


class UserListResponse(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "users": ([User],),
        }

    attribute_map = {
        "users": "users",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Array of Datadog users for a given organization.

        :param users: Array of users.
        :type users: [User], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UserListResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
