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


class SyntheticsTestResultRumContext(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "application_id": (str,),
            "session_id": (str,),
            "view_id": (str,),
        }

    attribute_map = {
        "application_id": "application_id",
        "session_id": "session_id",
        "view_id": "view_id",
    }

    def __init__(
        self_,
        application_id: Union[str, UnsetType] = unset,
        session_id: Union[str, UnsetType] = unset,
        view_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        RUM application context associated with a step or sub-test.

        :param application_id: RUM application identifier.
        :type application_id: str, optional

        :param session_id: RUM session identifier.
        :type session_id: str, optional

        :param view_id: RUM view identifier.
        :type view_id: str, optional
        """
        if application_id is not unset:
            kwargs["application_id"] = application_id
        if session_id is not unset:
            kwargs["session_id"] = session_id
        if view_id is not unset:
            kwargs["view_id"] = view_id
        super().__init__(kwargs)
