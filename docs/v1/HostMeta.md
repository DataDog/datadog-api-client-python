# HostMeta

Metadata associated with your host.

## Properties

| Name                | Type                                                  | Description                                 | Notes      |
| ------------------- | ----------------------------------------------------- | ------------------------------------------- | ---------- |
| **agent_checks**    | [**[AgentCheck]**](AgentCheck.md)                     | A list of Agent checks running on the host. | [optional] |
| **agent_version**   | **str**                                               | The Datadog Agent version.                  | [optional] |
| **cpu_cores**       | **int**                                               | The number of cores.                        | [optional] |
| **fbsd_v**          | **[str]**                                             | An array of Mac versions.                   | [optional] |
| **gohai**           | **str**                                               | JSON string containing system information.  | [optional] |
| **install_method**  | [**HostMetaInstallMethod**](HostMetaInstallMethod.md) |                                             | [optional] |
| **mac_v**           | **[str]**                                             | An array of Mac versions.                   | [optional] |
| **machine**         | **str**                                               | The machine architecture.                   | [optional] |
| **nix_v**           | **[str]**                                             | Array of Unix versions.                     | [optional] |
| **platform**        | **str**                                               | The OS platform.                            | [optional] |
| **processor**       | **str**                                               | The processor.                              | [optional] |
| **python_v**        | **str**                                               | The Python version.                         | [optional] |
| **socket_fqdn**     | **str**                                               | The socket fqdn.                            | [optional] |
| **socket_hostname** | **str**                                               | The socket hostname.                        | [optional] |
| **win_v**           | **[str]**                                             | An array of Windows versions.               | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
