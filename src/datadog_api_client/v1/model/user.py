# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class User(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.access_role import AccessRole

        return {
            "access_role": (AccessRole,),
            "disabled": (bool,),
            "email": (str,),
            "handle": (str,),
            "icon": (str,),
            "name": (str,),
            "verified": (bool,),
        }

    attribute_map = {
        "access_role": "access_role",
        "disabled": "disabled",
        "email": "email",
        "handle": "handle",
        "icon": "icon",
        "name": "name",
        "verified": "verified",
    }
    read_only_vars = {
        "icon",
        "verified",
    }

    def __init__(self, *args, **kwargs):
        """
        Create, edit, and disable users.

        :param access_role: The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user).
        :type access_role: AccessRole, optional

        :param disabled: The new disabled status of the user.
        :type disabled: bool, optional

        :param email: The new email of the user.
        :type email: str, optional

        :param handle: The user handle, must be a valid email.
        :type handle: str, optional

        :param icon: Gravatar icon associated to the user.
        :type icon: str, optional

        :param name: The name of the user.
        :type name: str, optional

        :param verified: Whether or not the user logged in Datadog at least once.
        :type verified: bool, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(User, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
