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


class AWSAssumeRole(ModelNormal):
    validations = {
        "account_id": {},
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_assume_role_type import AWSAssumeRoleType

        return {
            "account_id": (str,),
            "external_id": (str,),
            "principal_id": (str,),
            "role": (str,),
            "type": (AWSAssumeRoleType,),
        }

    attribute_map = {
        "account_id": "account_id",
        "external_id": "external_id",
        "principal_id": "principal_id",
        "role": "role",
        "type": "type",
    }
    read_only_vars = {
        "external_id",
        "principal_id",
    }

    def __init__(
        self_,
        account_id: str,
        role: str,
        type: AWSAssumeRoleType,
        external_id: Union[str, UnsetType] = unset,
        principal_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``AWSAssumeRole`` object.

        :param account_id: AWS account the connection is created for
        :type account_id: str

        :param external_id: External ID used to scope which connection can be used to assume the role
        :type external_id: str, optional

        :param principal_id: AWS account that will assume the role
        :type principal_id: str, optional

        :param role: Role to assume
        :type role: str

        :param type: The definition of ``AWSAssumeRoleType`` object.
        :type type: AWSAssumeRoleType
        """
        if external_id is not unset:
            kwargs["external_id"] = external_id
        if principal_id is not unset:
            kwargs["principal_id"] = principal_id
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.role = role
        self_.type = type
