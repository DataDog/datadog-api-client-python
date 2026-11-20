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


class RemediationGroupImageUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "action": (str,),
            "advisory_count": (int,),
            "exploitable_cve_count": (int,),
            "file_count": (int,),
            "grouping_location": (str,),
            "location_is_filename": (bool,),
            "remediation_kind": (str,),
            "target_version": (str,),
        }

    attribute_map = {
        "action": "action",
        "advisory_count": "advisory_count",
        "exploitable_cve_count": "exploitable_cve_count",
        "file_count": "file_count",
        "grouping_location": "grouping_location",
        "location_is_filename": "location_is_filename",
        "remediation_kind": "remediation_kind",
        "target_version": "target_version",
    }

    def __init__(
        self_,
        action: str,
        advisory_count: int,
        exploitable_cve_count: int,
        file_count: int,
        grouping_location: str,
        location_is_filename: bool,
        remediation_kind: str,
        target_version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        An image or package to upgrade, for a group of host and container vulnerabilities ( ``cloudvm.image_update`` ).
        The group gathers the open vulnerabilities of running production images that have a fix available, and groups
        them by ``grouping_location`` , ``remediation_kind`` , and ``action``.

        :param action: Name of the container image, base image, or package to upgrade. The value comes from the first of these
            attributes that the findings have: ``@remediation.container_image.latest_major.name`` ,
            ``@remediation.base_image.latest_major.name`` , or ``@remediation.recommended.name``.
        :type action: str

        :param advisory_count: Number of distinct values of ``@advisory.id`` across the group's findings.
        :type advisory_count: int

        :param exploitable_cve_count: Number of distinct values of ``@advisory.id`` across the group's findings that have
            ``@risk.has_exploit_available`` set to ``true``.
        :type exploitable_cve_count: int

        :param file_count: Number of distinct values of ``@code_location.filename`` across the group's findings.
        :type file_count: int

        :param grouping_location: File that contains the findings, from their ``@code_location.filename`` attribute. When no file is known,
            the value is the findings' ``@container_image.name``.
        :type grouping_location: str

        :param location_is_filename: Whether ``grouping_location`` is a ``@code_location.filename`` rather than a ``@container_image.name``.
        :type location_is_filename: bool

        :param remediation_kind: Kind of upgrade: ``image_update`` when the findings have a ``@remediation.container_image.latest_major.name`` ,
            ``base_image_bump`` when they have ``@vulnerability.is_inherited_from_base_image`` set to ``true`` , and
            ``package_update`` otherwise.
        :type remediation_kind: str

        :param target_version: Version to upgrade to: the ``@remediation.container_image.latest_major.tag`` or
            ``@remediation.base_image.latest_major.tag`` of the image in ``action`` , or else the highest
            ``@remediation.recommended.version`` across the group's findings. Omitted when no version is recommended
            or when the recommended versions can't be ordered.
        :type target_version: str, optional
        """
        if target_version is not unset:
            kwargs["target_version"] = target_version
        super().__init__(kwargs)

        self_.action = action
        self_.advisory_count = advisory_count
        self_.exploitable_cve_count = exploitable_cve_count
        self_.file_count = file_count
        self_.grouping_location = grouping_location
        self_.location_is_filename = location_is_filename
        self_.remediation_kind = remediation_kind
