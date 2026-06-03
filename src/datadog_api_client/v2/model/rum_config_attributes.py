# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class RumConfigAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "disabled": (bool,),
            "enforced_application_tags": (bool,),
            "enforced_application_tags_updated_at": (datetime,),
            "enforced_application_tags_updated_by": (str,),
            "ootb_metrics_version": (int,),
            "ootb_metrics_version_installed_at": (datetime,),
            "retention_filters_enabled": (bool,),
            "retention_filters_enabled_updated_at": (datetime,),
            "retention_filters_enabled_updated_by": (str,),
        }

    attribute_map = {
        "disabled": "disabled",
        "enforced_application_tags": "enforced_application_tags",
        "enforced_application_tags_updated_at": "enforced_application_tags_updated_at",
        "enforced_application_tags_updated_by": "enforced_application_tags_updated_by",
        "ootb_metrics_version": "ootb_metrics_version",
        "ootb_metrics_version_installed_at": "ootb_metrics_version_installed_at",
        "retention_filters_enabled": "retention_filters_enabled",
        "retention_filters_enabled_updated_at": "retention_filters_enabled_updated_at",
        "retention_filters_enabled_updated_by": "retention_filters_enabled_updated_by",
    }

    def __init__(
        self_,
        enforced_application_tags: bool,
        retention_filters_enabled: bool,
        disabled: Union[bool, UnsetType] = unset,
        enforced_application_tags_updated_at: Union[datetime, UnsetType] = unset,
        enforced_application_tags_updated_by: Union[str, UnsetType] = unset,
        ootb_metrics_version: Union[int, UnsetType] = unset,
        ootb_metrics_version_installed_at: Union[datetime, UnsetType] = unset,
        retention_filters_enabled_updated_at: Union[datetime, UnsetType] = unset,
        retention_filters_enabled_updated_by: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the RUM configuration.

        :param disabled: Whether the RUM configuration is disabled for the organization.
        :type disabled: bool, optional

        :param enforced_application_tags: Whether application tags are enforced for the RUM applications in the organization.
        :type enforced_application_tags: bool

        :param enforced_application_tags_updated_at: Timestamp of when the enforced application tags setting was last updated.
        :type enforced_application_tags_updated_at: datetime, optional

        :param enforced_application_tags_updated_by: Handle of the user who last updated the enforced application tags setting.
        :type enforced_application_tags_updated_by: str, optional

        :param ootb_metrics_version: Version of the out-of-the-box metrics installed for the organization.
        :type ootb_metrics_version: int, optional

        :param ootb_metrics_version_installed_at: Timestamp of when the out-of-the-box metrics version was installed.
        :type ootb_metrics_version_installed_at: datetime, optional

        :param retention_filters_enabled: Whether retention filters are enabled for the organization.
        :type retention_filters_enabled: bool

        :param retention_filters_enabled_updated_at: Timestamp of when the retention filters setting was last updated.
        :type retention_filters_enabled_updated_at: datetime, optional

        :param retention_filters_enabled_updated_by: Handle of the user or job who last updated the retention filters setting.
        :type retention_filters_enabled_updated_by: str, optional
        """
        if disabled is not unset:
            kwargs["disabled"] = disabled
        if enforced_application_tags_updated_at is not unset:
            kwargs["enforced_application_tags_updated_at"] = enforced_application_tags_updated_at
        if enforced_application_tags_updated_by is not unset:
            kwargs["enforced_application_tags_updated_by"] = enforced_application_tags_updated_by
        if ootb_metrics_version is not unset:
            kwargs["ootb_metrics_version"] = ootb_metrics_version
        if ootb_metrics_version_installed_at is not unset:
            kwargs["ootb_metrics_version_installed_at"] = ootb_metrics_version_installed_at
        if retention_filters_enabled_updated_at is not unset:
            kwargs["retention_filters_enabled_updated_at"] = retention_filters_enabled_updated_at
        if retention_filters_enabled_updated_by is not unset:
            kwargs["retention_filters_enabled_updated_by"] = retention_filters_enabled_updated_by
        super().__init__(kwargs)

        self_.enforced_application_tags = enforced_application_tags
        self_.retention_filters_enabled = retention_filters_enabled
