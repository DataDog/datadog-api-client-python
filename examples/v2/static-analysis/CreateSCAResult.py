"""
Post dependencies for analysis returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.sca_request import ScaRequest
from datadog_api_client.v2.model.sca_request_data import ScaRequestData
from datadog_api_client.v2.model.sca_request_data_attributes import ScaRequestDataAttributes
from datadog_api_client.v2.model.sca_request_data_attributes_commit import ScaRequestDataAttributesCommit
from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items import (
    ScaRequestDataAttributesDependenciesItems,
)
from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items import (
    ScaRequestDataAttributesDependenciesItemsLocationsItems,
)
from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items_file_position import (
    ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition,
)
from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items_position import (
    ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition,
)
from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_reachable_symbol_properties_items import (
    ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems,
)
from datadog_api_client.v2.model.sca_request_data_attributes_files_items import ScaRequestDataAttributesFilesItems
from datadog_api_client.v2.model.sca_request_data_attributes_relations_items import (
    ScaRequestDataAttributesRelationsItems,
)
from datadog_api_client.v2.model.sca_request_data_attributes_repository import ScaRequestDataAttributesRepository
from datadog_api_client.v2.model.sca_request_data_attributes_vulnerabilities_items import (
    ScaRequestDataAttributesVulnerabilitiesItems,
)
from datadog_api_client.v2.model.sca_request_data_attributes_vulnerabilities_items_affects_items import (
    ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems,
)
from datadog_api_client.v2.model.sca_request_data_type import ScaRequestDataType

body = ScaRequest(
    data=ScaRequestData(
        attributes=ScaRequestDataAttributes(
            commit=ScaRequestDataAttributesCommit(),
            dependencies=[
                ScaRequestDataAttributesDependenciesItems(
                    exclusions=[],
                    locations=[
                        ScaRequestDataAttributesDependenciesItemsLocationsItems(
                            block=ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition(
                                end=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                                start=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                            ),
                            name=ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition(
                                end=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                                start=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                            ),
                            namespace=ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition(
                                end=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                                start=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                            ),
                            version=ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition(
                                end=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                                start=ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(),
                            ),
                        ),
                    ],
                    reachable_symbol_properties=[
                        ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems(),
                    ],
                ),
            ],
            files=[
                ScaRequestDataAttributesFilesItems(),
            ],
            relations=[
                ScaRequestDataAttributesRelationsItems(
                    depends_on=[],
                ),
            ],
            repository=ScaRequestDataAttributesRepository(),
            vulnerabilities=[
                ScaRequestDataAttributesVulnerabilitiesItems(
                    affects=[
                        ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems(),
                    ],
                ),
            ],
        ),
        type=ScaRequestDataType.SCAREQUESTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_sca_result"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    api_instance.create_sca_result(body=body)
