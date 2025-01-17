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
    from datadog_api_client.v2.model.aws_assume_role_type import AWSAssumeRoleType


class AWSAssumeRoleUpdate(ModelNormal):
    validations = {
        "account_id": {},
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_assume_role_type import AWSAssumeRoleType

        return {
            "account_id": (str,),
            "generate_new_external_id": (bool,),
            "role": (str,),
            "type": (AWSAssumeRoleType,),
        }

    attribute_map = {
        "account_id": "account_id",
        "generate_new_external_id": "generate_new_external_id",
        "role": "role",
        "type": "type",
    }

    def __init__(
        self_,
        type: AWSAssumeRoleType,
        account_id: Union[str, UnsetType] = unset,
        generate_new_external_id: Union[bool, UnsetType] = unset,
        role: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``AWSAssumeRoleUpdate`` object.

        :param account_id: AWS account the connection is created for
        :type account_id: str, optional

        :param generate_new_external_id: The ``AWSAssumeRoleUpdate`` ``generate_new_external_id``.
        :type generate_new_external_id: bool, optional

        :param role: Role to assume
        :type role: str, optional

        :param type: The definition of ``AWSAssumeRoleType`` object.
        :type type: AWSAssumeRoleType
        """
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if generate_new_external_id is not unset:
            kwargs["generate_new_external_id"] = generate_new_external_id
        if role is not unset:
            kwargs["role"] = role
        super().__init__(kwargs)

        self_.type = type
