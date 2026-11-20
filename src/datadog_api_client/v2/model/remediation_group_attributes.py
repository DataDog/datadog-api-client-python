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
    from datadog_api_client.v2.model.remediation_group_findings import RemediationGroupFindings
    from datadog_api_client.v2.model.remediation_group_image_update import RemediationGroupImageUpdate
    from datadog_api_client.v2.model.remediation_group_package_update import RemediationGroupPackageUpdate


class RemediationGroupAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remediation_group_findings import RemediationGroupFindings
        from datadog_api_client.v2.model.remediation_group_image_update import RemediationGroupImageUpdate
        from datadog_api_client.v2.model.remediation_group_package_update import RemediationGroupPackageUpdate

        return {
            "findings": (RemediationGroupFindings,),
            "grouping_definition_id": (str,),
            "image_update": (RemediationGroupImageUpdate,),
            "package_update": (RemediationGroupPackageUpdate,),
            "title": (str,),
        }

    attribute_map = {
        "findings": "findings",
        "grouping_definition_id": "grouping_definition_id",
        "image_update": "image_update",
        "package_update": "package_update",
        "title": "title",
    }

    def __init__(
        self_,
        findings: RemediationGroupFindings,
        grouping_definition_id: str,
        title: str,
        image_update: Union[RemediationGroupImageUpdate, UnsetType] = unset,
        package_update: Union[RemediationGroupPackageUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a remediation group. Each group includes one kind object, ``package_update`` or ``image_update`` ,
        depending on its grouping definition.

        :param findings: Counts of the group's open findings. The counts include every finding in the group, including findings that
            don't match ``filter[query]``.
        :type findings: RemediationGroupFindings

        :param grouping_definition_id: Grouping definition that formed the group: ``sca.package_update`` or ``cloudvm.image_update``.
        :type grouping_definition_id: str

        :param image_update: An image or package to upgrade, for a group of host and container vulnerabilities ( ``cloudvm.image_update`` ).
            The group gathers the open vulnerabilities of running production images that have a fix available, and groups
            them by ``grouping_location`` , ``remediation_kind`` , and ``action``.
        :type image_update: RemediationGroupImageUpdate, optional

        :param package_update: A package to update in a repository, for a group of library vulnerabilities ( ``sca.package_update`` ). The group
            gathers the open vulnerabilities of direct dependencies that have a recommended fix, and groups them by
            ``@git.repository_id`` , ``@vulnerability.stack.ecosystem`` , and ``@remediation.recommended.name``.
        :type package_update: RemediationGroupPackageUpdate, optional

        :param title: Title of the group, which describes the change to make.
        :type title: str
        """
        if image_update is not unset:
            kwargs["image_update"] = image_update
        if package_update is not unset:
            kwargs["package_update"] = package_update
        super().__init__(kwargs)

        self_.findings = findings
        self_.grouping_definition_id = grouping_definition_id
        self_.title = title
