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


class RemediationGroupPackageUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "advisory_count": (int,),
            "ecosystem": (str,),
            "exploitable_cve_count": (int,),
            "file_count": (int,),
            "package_name": (str,),
            "repository_id": (str,),
            "target_version": (str,),
        }

    attribute_map = {
        "advisory_count": "advisory_count",
        "ecosystem": "ecosystem",
        "exploitable_cve_count": "exploitable_cve_count",
        "file_count": "file_count",
        "package_name": "package_name",
        "repository_id": "repository_id",
        "target_version": "target_version",
    }

    def __init__(
        self_,
        advisory_count: int,
        ecosystem: str,
        exploitable_cve_count: int,
        file_count: int,
        package_name: str,
        repository_id: str,
        target_version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A package to update in a repository, for a group of library vulnerabilities ( ``sca.package_update`` ). The group
        gathers the open vulnerabilities of direct dependencies that have a recommended fix, and groups them by
        ``@git.repository_id`` , ``@vulnerability.stack.ecosystem`` , and ``@remediation.recommended.name``.

        :param advisory_count: Number of distinct values of ``@advisory.id`` across the group's findings.
        :type advisory_count: int

        :param ecosystem: Package ecosystem, the findings' ``@vulnerability.stack.ecosystem``.
        :type ecosystem: str

        :param exploitable_cve_count: Number of distinct values of ``@advisory.id`` across the group's findings that have
            ``@risk.has_exploit_available`` set to ``true``.
        :type exploitable_cve_count: int

        :param file_count: Number of distinct values of ``@package.declaration.block.filename`` , the files that declare the package.
        :type file_count: int

        :param package_name: Name of the package to update, the findings' ``@remediation.recommended.name``.
        :type package_name: str

        :param repository_id: Repository that depends on the package, the findings' ``@git.repository_id``.
        :type repository_id: str

        :param target_version: Version to update the package to, the highest ``@remediation.recommended.version`` across the group's
            findings. Omitted when no version is recommended or when the recommended versions can't be ordered.
        :type target_version: str, optional
        """
        if target_version is not unset:
            kwargs["target_version"] = target_version
        super().__init__(kwargs)

        self_.advisory_count = advisory_count
        self_.ecosystem = ecosystem
        self_.exploitable_cve_count = exploitable_cve_count
        self_.file_count = file_count
        self_.package_name = package_name
        self_.repository_id = repository_id
