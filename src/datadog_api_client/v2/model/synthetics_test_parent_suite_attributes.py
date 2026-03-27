# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SyntheticsTestParentSuiteAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "child_name": (str,),
            "child_public_id": (str,),
            "monitor_id": (int,),
            "name": (str,),
            "overall_state": (int,),
            "overall_state_modified": (str,),
            "public_id": (str,),
        }

    attribute_map = {
        "child_name": "child_name",
        "child_public_id": "child_public_id",
        "monitor_id": "monitor_id",
        "name": "name",
        "overall_state": "overall_state",
        "overall_state_modified": "overall_state_modified",
        "public_id": "public_id",
    }

    def __init__(
        self_,
        child_name: Union[str, UnsetType] = unset,
        child_public_id: Union[str, UnsetType] = unset,
        monitor_id: Union[int, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        overall_state: Union[int, UnsetType] = unset,
        overall_state_modified: Union[str, UnsetType] = unset,
        public_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing details about a parent suite of a Synthetic test.

        :param child_name: The name of the child test within the suite.
        :type child_name: str, optional

        :param child_public_id: The public ID of the child test within the suite.
        :type child_public_id: str, optional

        :param monitor_id: The associated monitor ID.
        :type monitor_id: int, optional

        :param name: Name of the parent suite.
        :type name: str, optional

        :param overall_state: The overall state of the parent suite.
        :type overall_state: int, optional

        :param overall_state_modified: Timestamp of when the overall state was last modified.
        :type overall_state_modified: str, optional

        :param public_id: The public ID of the parent suite.
        :type public_id: str, optional
        """
        if child_name is not unset:
            kwargs["child_name"] = child_name
        if child_public_id is not unset:
            kwargs["child_public_id"] = child_public_id
        if monitor_id is not unset:
            kwargs["monitor_id"] = monitor_id
        if name is not unset:
            kwargs["name"] = name
        if overall_state is not unset:
            kwargs["overall_state"] = overall_state
        if overall_state_modified is not unset:
            kwargs["overall_state_modified"] = overall_state_modified
        if public_id is not unset:
            kwargs["public_id"] = public_id
        super().__init__(kwargs)
