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


class AWSResourcesConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "cloud_security_posture_management_collection": (bool,),
            "extended_collection": (bool,),
        }

    attribute_map = {
        "cloud_security_posture_management_collection": "cloud_security_posture_management_collection",
        "extended_collection": "extended_collection",
    }

    def __init__(
        self_,
        cloud_security_posture_management_collection: Union[bool, UnsetType] = unset,
        extended_collection: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS Resources config

        :param cloud_security_posture_management_collection: Whether Datadog collects cloud security posture management resources from your AWS account.
        :type cloud_security_posture_management_collection: bool, optional

        :param extended_collection: Whether Datadog collects additional attributes and configuration information about the resources in your AWS account. Required for ``cspm_resource_collection``.
        :type extended_collection: bool, optional
        """
        if cloud_security_posture_management_collection is not unset:
            kwargs["cloud_security_posture_management_collection"] = cloud_security_posture_management_collection
        if extended_collection is not unset:
            kwargs["extended_collection"] = extended_collection
        super().__init__(kwargs)
